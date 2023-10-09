from threading import Thread, Event
import time


event = Event()  # 造了一个红绿灯


def light():
    print('红灯亮着的')
    time.sleep(3)
    print('绿灯亮了')
    # 告诉等待红灯的人可以走了
    event.set()


def car(name):
    print('%s 车正在灯红灯'%name)
    event.wait()  # 等待别人给你发信号
    print('%s 车加油门飙车走了'%name)


if __name__ == '__main__':
    t = Thread(target=light)
    t.start()

    for i in range(20):
        t = Thread(target=car, args=('%s'%i, ))
        t.start()

