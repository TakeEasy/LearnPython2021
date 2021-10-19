'''
#一：今日作业：
#1、编写文件copy工具

#2、编写登录程序，账号密码来自于文件

#3、编写注册程序，账号密码来存入文件

#二：周末综合作业：
# 2.1：编写用户登录接口
#1、输入账号密码完成验证，验证通过后输出"登录成功"
#2、可以登录不同的用户
#3、同一账号输错三次锁定，（提示：锁定的用户存入文件中，这样才能保证程序关闭后，该用户仍然被锁定）


# 2.2：编写程序实现用户注册后（注册到文件中），可以登录（登录信息来自于文件）
提示：
while True:
    msg = """
    0 退出
    1 登录
    2 注册
    """
    print(msg)
    cmd = input('请输入命令编号>>: ').strip()
    if not cmd.isdigit():
        print('必须输入命令编号的数字，傻叉')
        continue

    if cmd == '0':
        break
    elif cmd == '1':
        # 登录功能代码（附加：可以把之前的循环嵌套，三次输错退出引入过来）
        pass
    elif cmd == '2':
        # 注册功能代码
        pass
    else:
        print('输入的命令不存在')

    # 思考：上述这个if分支的功能否使用其他更为优美地方式实现


'''
import os

MSG = '''
0: 退出
1: 登录
2: 注册
'''
signin_count = 0
signin_success = False
with open('userinfo/userinfo', mode='rb') as f:
    res = f.read()
    print(res)
while True:
    print(MSG)
    str_usercmd = input('请输入指令:').strip()
    if str_usercmd == '1':  # 登录
        while signin_count < 3 and not signin_success:
            signin_username = input('请输入用户名:').strip()
            signin_userpwd = input('请输入密码:').strip()
            with open('userinfo/userinfo', mode='rt', encoding='utf-8') as f:
                for line in f:
                    userinfo_l = line.strip().split(':')
                    if signin_username == userinfo_l[0] and signin_userpwd == userinfo_l[1]:
                        signin_count = 0
                        signin_success = True
                        break
                else:
                    print('账号密码错误 请重试 还可以重试{0}次'.format(2 - signin_count))
                    signin_count += 1
        if signin_count == 0 and signin_success == True:
            print('登录成功 88')
        else:
            print('登录失败 88')
    elif str_usercmd == '2':  # 注册
        signup_username = input('请输入注册用户名:').strip()
        signup_userpwd = input('请输入注册密码:').strip()
        with open('userinfo/userinfo', mode='rt', encoding='utf-8') as f:
            for line in f:
                userinfo_l = line.strip().split(':')
                if signup_username == userinfo_l[0]:
                    print('你想注册的用户已经存在 请重新注册')
                    break
            else:
                with open('userinfo/userinfo', mode='at', encoding='utf-8') as fsignup:
                    fsignup.write('{0}:{1}{2}'.format(signup_username, signup_userpwd, '\n'))
                print('注册成功')
    elif str_usercmd == '0':
        print('退出洛')
        break
    else:
        print('请输入正确指令')
