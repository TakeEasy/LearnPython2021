'''
作业：
1、编写课上讲解的有参装饰器准备明天默写
2：还记得我们用函数对象的概念，制作一个函数字典的操作吗，来来来，我们有更高大上的做法，在文件开头声明一个空字典，然后在每个函数前加上装饰器，完成自动添加到字典的操作
3、 编写日志装饰器，实现功能如：一旦函数f1执行，则将消息2017-07-21 11:12:11 f1 run写入到日志文件中，日志文件路径可以指定
注意：时间格式的获取
import time
time.strftime('%Y-%m-%d %X')
4、基于迭代器的方式，用while循环迭代取值字符串、列表、元组、字典、集合、文件对象
5、自定义迭代器实现range功能



====================本周选做作业如下====================
编写小说阅读程序实现下属功能
# 一：程序运行开始时显示
    0 账号注册
    1 充值功能
    2 阅读小说


# 二： 针对文件db.txt，内容格式为："用户名:密码:金额",完成下述功能
2.1、账号注册
2.2、充值功能

# 三：文件story_class.txt存放类别与小说文件路径，如下,读出来后可用eval反解出字典
{"0":{"0":["倚天屠狗记.txt",3],"1":["沙雕英雄转.txt",10]},"1":{"0":["令人羞耻的爱.txt",6],"1":["二狗的妻子与大草原的故事.txt",5]},}

3.1、用户登录成功后显示如下内容，根据用户选择，显示对应品类的小说编号、小说名字、以及小说的价格
"""
0 玄幻武侠
1 都市爱情
2 高效养猪36技
"""

3.2、用户输入具体的小说编号，提示是否付费，用户输入y确定后，扣费并显示小说内容，如果余额不足则提示余额不足

# 四：为功能2.2、3.1、3.2编写认证功能装饰器，要求必须登录后才能执行操作

# 五：为功能2.2、3.2编写记录日志的装饰器，日志格式为："时间 用户名 操作(充值or消费) 金额"



# 附加：
# 可以拓展作者模块，作者可以上传自己的作品




'''

from functools import wraps
import time
import os

IF_LOGIN = False
LOGIN_NAME = ''
LOGIN_TIME = 0
TAG = True

DB_PATH = 'userinfo/userinfo.db'


def update_file(filepath, old_content, new_content):
    swap_filepath = '{0}{1}'.format(filepath, '.swap')
    with open(filepath, mode='rt', encoding='utf-8') as fr, \
            open(swap_filepath, mode='wt', encoding='utf-8') as fw:
        for line in fr:
            fw.write(line.replace(old_content, new_content))
    os.remove(filepath)
    os.rename(swap_filepath, filepath)


def logger(logpath):
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            with open(logpath, mode='at', encoding='utf-8') as fsignup:
                fsignup.write('{0}:run {1}:0{2}'.format(time.strftime('%Y-%m-%d %X'), func.__name__, '\n'))
            return res

        return wrapper

    return deco


def login_user_print(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        global IF_LOGIN
        global LOGIN_NAME
        if IF_LOGIN:
            print('{0:*^20}'.format(LOGIN_NAME))
        else:
            print('{0:*^20}'.format('请先登录'))
        res = func(*args, **kwargs)
        print('{0:*^20}'.format(''))
        return res

    return wrapper


def loginner(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        global IF_LOGIN
        global LOGIN_NAME
        global LOGIN_TIME
        global DB_PATH
        if not IF_LOGIN:
            input_username = input('请输入用户名:').strip()
            input_pwd = input('请输入密码:').strip()
            with open(DB_PATH, mode='rt', encoding='utf-8') as fr:
                for line in fr:
                    l = line.strip().split(':')
                    # print('{0},{1}'.format(l[0], l[1]))
                    if input_username == l[0] and input_pwd == l[1]:
                        IF_LOGIN = True
                        LOGIN_NAME = l[0]
                        LOGIN_TIME = time.time()
                        print('登录成功!!!')
                        break
                else:
                    IF_LOGIN = False
                    LOGIN_NAME = ''
                    LOGIN_TIME = 0
                    print('用户名密码错误')

        if IF_LOGIN:
            res = func(*args, **kwargs)
            return res

    return wrapper


def atm_signup(dbpath, user_name, user_pwd):
    with open(dbpath, mode='rt', encoding='utf-8') as f:
        for line in f:
            userinfo_l = line.strip().split(':')
            if user_name == userinfo_l[0]:
                return False
        else:
            with open(dbpath, mode='at', encoding='utf-8') as fsignup:
                fsignup.write('{0}:{1}:0{2}'.format(user_name, user_pwd, '\n'))
            return True


def atm_save_money(dbpath, user_name, money):
    list_userinfo = []
    with open(dbpath, mode='rt', encoding='utf-8') as fr:
        for line in fr:
            userinfo_l = line.strip().split(':')
            if user_name == userinfo_l[0]:
                list_userinfo = userinfo_l
    new_list_userinfo = list_userinfo.copy()
    new_list_userinfo[2] = str(int(new_list_userinfo[2]) + money)
    if int(new_list_userinfo[2]) < 0:
        return False
    update_file(dbpath, ':'.join(list_userinfo), ':'.join(new_list_userinfo))
    return True


def atm_show_money(dbpath, user_name):
    list_userinfo = []
    with open(dbpath, mode='rt', encoding='utf-8') as fr:
        for line in fr:
            userinfo_l = line.strip().split(':')
            if user_name == userinfo_l[0]:
                list_userinfo = userinfo_l
        return list_userinfo[2]


def user_signup():
    global DB_PATH
    input_username = input('请输入注册用户名:').strip()
    input_pwd = input('请输入注册密码:').strip()
    if atm_signup(DB_PATH, input_username, input_pwd):
        print('注册成功!!!')
    else:
        print('注册失败!!!')


@loginner
def user_givemoney():
    global LOGIN_NAME
    global DB_PATH
    input_money = input('请输入充值金额:').strip()
    if input_money.isdigit() and int(input_money) >= 0:
        if atm_save_money(DB_PATH, LOGIN_NAME, int(input_money)):
            print('存入成功!')
            print('当前余额:{0}'.format(atm_show_money(DB_PATH, LOGIN_NAME)))
        else:
            print('存入失败!')
    else:
        print('请输入有效充值金额')


@loginner
def user_readbook():
    pass


def user_quit():
    global TAG
    TAG = False
    print('推出洛 8888')


@login_user_print
def print_menu(menu):
    for k, v in menu.items():
        print('{0}:{1}'.format(k, v[0]))


MENU = {'0': ['账号注册', user_signup], '1': ['充值', user_givemoney], '2': ['阅读小说', user_readbook], 'q': ['退出', user_quit]}

while TAG:
    print_menu(MENU)
    user_cmd = input('请输入指令:').strip()
    if user_cmd in MENU:
        user_ops = MENU.get(user_cmd)[1]
        user_ops()
    else:
        print('请输入有效指令')
