from threading import Thread, active_count, current_thread
import os,time


def task(n):
    # print('hello world',os.getpid())
    print('hello world',current_thread().name)
    time.sleep(n)


if __name__ == '__main__':
    t = Thread(target=task,args=(1,))
    t1 = Thread(target=task,args=(2,))
    t.start()
    t1.start()
    t.join()
    print('主',active_count())  # 统计当前正在活跃的线程数
    # print('主',os.getpid())
    # print('主',current_thread().name)  # 获取线程名字