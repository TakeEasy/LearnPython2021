# 计算密集型
# from multiprocessing import Process
# from threading import Thread
# import os,time
#
#
# def work():
#     res = 0
#     for i in range(10000000):
#         res *= i
#
# if __name__ == '__main__':
#     l = []
#     print(os.cpu_count())  # 获取当前计算机CPU个数
#     start_time = time.time()
#     for i in range(12):
#         p = Process(target=work)  # 1.4679949283599854
#         t = Thread(target=work)  # 5.698534250259399
#         t.start()
#         # p.start()
#         # l.append(p)
#         l.append(t)
#     for p in l:
#         p.join()
#     print(time.time()-start_time)



# IO密集型
from multiprocessing import Process
from threading import Thread
import os,time


def work():
    time.sleep(2)

if __name__ == '__main__':
    l = []
    print(os.cpu_count())  # 获取当前计算机CPU个数
    start_time = time.time()
    for i in range(4000):
        # p = Process(target=work)  # 21.149890184402466
        t = Thread(target=work)  # 3.007986068725586
        t.start()
        # p.start()
        # l.append(p)
        l.append(t)
    for p in l:
        p.join()
    print(time.time()-start_time)













