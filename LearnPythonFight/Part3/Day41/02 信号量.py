from threading import Thread, Semaphore
import time
import random


"""
利用random模块实现打印随机验证码(搜狗的一道笔试题)
"""
sm = Semaphore(5)  # 括号内写数字 写几就表示开设几个坑位


def task(name):
    sm.acquire()
    print('%s 正在蹲坑'% name)
    time.sleep(random.randint(1, 5))
    sm.release()


if __name__ == '__main__':
    for i in range(20):
        t = Thread(target=task, args=('伞兵%s号'%i, ))
        t.start()



