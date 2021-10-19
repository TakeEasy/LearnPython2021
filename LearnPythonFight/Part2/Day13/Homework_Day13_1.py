'''
# 1、编写文件修改功能，调用函数时，传入三个参数（修改的文件路径，要修改的内容，修改后的内容）既可完成文件的修改

# 2、编写tail工具

# 3、编写登录功能

# 4、编写注册功能

# 5、编写用户认证功能

# 选做题：编写ATM程序实现下述功能，数据来源于文件db.txt
# 1、充值功能：用户输入充值钱数，db.txt中该账号钱数完成修改
# 2、转账功能：用户A向用户B转账1000元，db.txt中完成用户A账号减钱，用户B账号加钱
# 3、提现功能：用户输入提现金额，db.txt中该账号钱数减少
# 4、查询余额功能：输入账号查询余额

# 选做题中的选做题：登录功能
# 用户登录成功后，内存中记录下该状态，上述功能以当前登录状态为准，必须先登录才能操作

'''
import time
import os


def update_file(filepath, old_content, new_content):
    swap_filepath = '{0}{1}'.format(filepath, '.swap')
    with open(filepath, mode='rt', encoding='utf-8') as fr, \
            open(swap_filepath, mode='wt', encoding='utf-8') as fw:
        for line in fr:
            fw.write(line.replace(old_content, new_content))
    os.remove(filepath)
    os.rename(swap_filepath, filepath)


def tail(filepath):
    with open(filepath, mode='rb') as f:
        f.seek(0, 2)
        while True:
            new_line = f.readline()
            if len(new_line) == 0:
                time.sleep(0.2)
            else:
                print(new_line.decode(encoding='utf-8'))


def atm_login(dbpath, user_name, user_pwd):
    with open(dbpath, mode='rt', encoding='utf-8') as f:
        for line in f:
            userinfo_l = line.strip().split(':')
            if user_name == userinfo_l[0] and user_pwd == userinfo_l[1]:
                return True
        else:
            return False


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


MSG = '''
0: 退出
1: 登录
2: 注册
'''
ATM_MSG = '''
0:退出登录
1:充值
2:转账
3:提现
4:查询余额
'''


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


def atm_move_money(dbpath, user_name, moveto_user, money):
    if money <= 0:
        return False
    else:
        if atm_save_money(dbpath, user_name, 0 - money):
            if atm_save_money(dbpath, moveto_user, money):
                return True
            else:
                return False
        else:
            return False


def atm_show_money(dbpath, user_name):
    list_userinfo = []
    with open(dbpath, mode='rt', encoding='utf-8') as fr:
        for line in fr:
            userinfo_l = line.strip().split(':')
            if user_name == userinfo_l[0]:
                list_userinfo = userinfo_l
        return list_userinfo[2]


tag = True
if_login = False
try_count = 0
DB_PATH = 'userinfo/userinfo.db'
login_username = ''
login_userpwd = ''
while tag:
    if not if_login:
        print(MSG)
        user_cmd = input('请输入指令:').strip()
        if user_cmd == '1':
            if try_count < 3:
                input_username = input('请输入用户名:').strip()
                input_userpwd = input('请输入密码:').strip()
                if atm_login(DB_PATH, input_username, input_userpwd):
                    if_login = True
                    try_count = 0
                    login_username = input_username
                    login_userpwd = input_userpwd
                    print('登录成功,即将进入ATM页面')
                    continue
                else:
                    login_username = ''
                    login_userpwd = ''
                    if_login = False
                    try_count += 1
                    print('用户名密码错误 还可重试{0}次'.format(3 - try_count))
            else:
                print('尝试登录次数超出 退出洛')
                break
        elif user_cmd == '2':
            input_username = input('请输入注册用户名:').strip()
            input_userpwd = input('请输入注册密码:').strip()
            if atm_signup(DB_PATH, input_username, input_userpwd):
                print('注册成功')
            else:
                print('用户已经存在,注册失败')
        elif user_cmd == '0':
            print('推出洛 88')
            break
        else:
            print('请输入有效指令')
    else:
        print(ATM_MSG)
        user_cmd = input('请输入指令:').strip()
        if user_cmd == '1':
            input_money = input('请输入充值金额:').strip()
            if input_money.isdigit() and int(input_money) >= 0:
                if atm_save_money(DB_PATH, login_username, int(input_money)):
                    print('存入成功!')
                    print('当前余额:{0}'.format(atm_show_money(DB_PATH, login_username)))
                else:
                    print('存入失败!')
            else:
                print('请输入数字')
        elif user_cmd == '2':
            input_money = input('请输入转账金额:').strip()
            input_moveto_username = input('请输入转入账户名称:').strip()
            if input_money.isdigit() and int(input_money) >= 0:
                if atm_move_money(DB_PATH, login_username, input_moveto_username, int(input_money)):
                    print('转账成功!')
                    print('当前余额:{0}'.format(atm_show_money(DB_PATH, login_username)))
                else:
                    print('转账失败!')
            else:
                print('只能输入正数')
        elif user_cmd == '3':
            input_money = input('请输入提现金额:').strip()
            if input_money.isdigit() and int(input_money) >= 0:
                if atm_save_money(DB_PATH, login_username, 0 - int(input_money)):
                    print('提取成功!')
                    print('当前余额:{0}'.format(atm_show_money(DB_PATH, login_username)))
                else:
                    print('提取失败!')
            else:
                print('请输入数字')
        elif user_cmd == '4':
            print('当前余额:{0}'.format(atm_show_money(DB_PATH, login_username)))
        elif user_cmd == '0':
            login_username = ''
            login_userpwd = ''
            if_login = False
            try_count = 0
        else:
            print('请输入有效指令')
