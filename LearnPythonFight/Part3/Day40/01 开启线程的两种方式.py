# from multiprocessing import Process
# from threading import Thread
# import time
#
#
# def task(name):
#     print('%s is running'%name)
#     time.sleep(1)
#     print('%s is over'%name)
#
#
# # 开启线程不需要在main下面执行代码 直接书写就可以
# # 但是我们还是习惯性的将启动命令写在main下面
# t = Thread(target=task,args=('egon',))
# # p = Process(target=task,args=('jason',))
# # p.start()
# t.start()  # 创建线程的开销非常小 几乎是代码一执行线程就已经创建了
# print('主')



from threading import Thread
import time


class MyThead(Thread):
    def __init__(self, name):
        """针对刷个下划线开头双下滑线结尾(__init__)的方法 统一读成 双下init"""
        # 重写了别人的方法 又不知道别人的方法里有啥 你就调用父类的方法
        super().__init__()
        self.name = name

    def run(self):
        print('%s is running'%self.name)
        time.sleep(1)
        print('egon DSB')


if __name__ == '__main__':
    t = MyThead('egon')
    t.start()
    print('主')












