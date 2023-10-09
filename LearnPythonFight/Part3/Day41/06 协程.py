# import time
#
# # 串行执行计算密集型的任务   1.2372429370880127
# def func1():
#     for i in range(10000000):
#         i + 1
#
# def func2():
#     for i in range(10000000):
#         i + 1
#
# start_time = time.time()
# func1()
# func2()
# print(time.time() - start_time)

# 切换 + yield  2.1247239112854004
# import time
#
#
# def func1():
#     while True:
#         10000000 + 1
#         yield
#
#
# def func2():
#     g = func1()  # 先初始化出生成器
#     for i in range(10000000):
#         i + 1
#         next(g)
#
# start_time = time.time()
# func2()
# print(time.time() - start_time)

from gevent import monkey;monkey.patch_all()
import time
from gevent import spawn

"""
gevent模块本身无法检测常见的一些io操作
在使用的时候需要你额外的导入一句话
from gevent import monkey
monkey.patch_all()
又由于上面的两句话在使用gevent模块的时候是肯定要导入的
所以还支持简写
from gevent import monkey;monkey.patch_all()
"""


def heng():
    print('哼')
    time.sleep(2)
    print('哼')


def ha():
    print('哈')
    time.sleep(3)
    print('哈')

def heiheihei():
    print('heiheihei')
    time.sleep(5)
    print('heiheihei')


start_time = time.time()
g1 = spawn(heng)
g2 = spawn(ha)
g3 = spawn(heiheihei)
g1.join()
g2.join()  # 等待被检测的任务执行完毕 再往后继续执行
g3.join()
# heng()
# ha()
# print(time.time() - start_time)  # 5.005702018737793
print(time.time() - start_time)  # 3.004199981689453   5.005439043045044
