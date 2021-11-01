'''
一：编写函数，（函数执行的时间用time.sleep(n)模拟）
二：编写装饰器，为函数加上统计时间的功能
三：编写装饰器，为函数加上认证的功能

四：编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），要求登录成功一次，后续的函数都无需再输入用户名和密码
注意：从文件中读出字符串形式的字典，可以用eval('{"name":"egon","password":"123"}')转成字典格式

五：编写装饰器，为多个函数加上认证功能，要求登录成功一次，在超时时间内无需重复登录，超过了超时时间，则必须重新登录


六：选做题
# 思考题（选做），叠加多个装饰器，加载顺序与运行顺序，可以将上述实现的装饰器叠加起来自己验证一下
# @deco1 # index=deco1(deco2.wrapper的内存地址)
# @deco2 # deco2.wrapper的内存地址=deco2(deco3.wrapper的内存地址)
# @deco3 # deco3.wrapper的内存地址=deco3(index)
# def index():
#     pass

'''
import time

USERINFO_PATH = 'userinfo/userinfo'
if_login = False
login_username = ''
login_time = 0
login_expire_sec = 60


def auth_expire(func):
    def wrapper(*args, **kwargs):
        global if_login
        global login_time
        global login_username
        global login_expire_sec

        if if_login and time.time() - login_time > login_expire_sec:
            if_login = False
            login_username = ''
            login_time = 0
        res = func(*args, **kwargs)
        return res

    return wrapper


def loginner(func):
    def wrapper(*args, **kwargs):
        global if_login
        global login_username
        global login_time
        global USERINFO_PATH
        if if_login == False:
            input_username = input('请输入用户名:').strip()
            input_pwd = input('请输入密码:').strip()
            with open(USERINFO_PATH, mode='rt', encoding='utf-8') as fr:
                for line in fr:
                    l = line.strip().split(':')
                    # print('{0},{1}'.format(l[0], l[1]))
                    if input_username == l[0] and input_pwd == l[1]:
                        if_login = True
                        login_username = l[0]
                        login_time = time.time()
                        break
                else:
                    if_login = False
                    login_username = ''
                    print('用户名密码错误')

        if if_login:
            res = func(*args, **kwargs)
            return res

    return wrapper


def how_long_func(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print('跑了{0}秒'.format(end_time - start_time))
        return res

    return wrapper


@loginner
@how_long_func
def do_something(a, b):
    time.sleep(10)
    print('{0},{1}'.format(a, b))


do_something('zzzz', 'asdfasf')
