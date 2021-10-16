'''
作业（必做题）：
#1. 使用while循环输出1 2 3 4 5 6     8 9 10
#2. 求1-100的所有数的和
#3. 输出 1-100 内的所有奇数
#4. 输出 1-100 内的所有偶数
#5. 求1-2+3-4+5 ... 99的所有数的和
#6. 用户登陆（三次机会重试）
#7：猜年龄游戏
    要求：
    允许用户最多尝试3次，3次都没猜对的话，就直接退出，如果猜对了，打印恭喜信息并退出

#8：猜年龄游戏升级版（选做题）
要求：
    允许用户最多尝试3次
    每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y或y, 就继续让其猜3次，以此往复，如果回答N或n，就退出程序
    如何猜对了，就直接退出



'''

'''#1. 使用while循环输出1 2 3 4 5 6     8 9 10'''
i = 1
while i <= 10:
    print(i)
    i += 1

'''#2. 求1-100的所有数的和'''
i = 1
all_i = 0
while i <= 100:
    all_i += i
    i += 1
print(all_i)

'''#3. 输出 1-100 内的所有奇数'''
i = 1
while i <= 100:
    if i % 2 == 1:
        print(i)
    i += 1

'''#4. 输出 1-100 内的所有偶数'''
i = 1
while i <= 100:
    if i % 2 == 0:
        print(i)
    i += 1

'''#5. 求1-2+3-4+5 ... 99的所有数的和'''
i = 1
all_i = 0
while i <= 99:
    if i % 2 == 1:
        all_i += i
    else:
        all_i -= i
    i += 1
print(all_i)

'''#6. 用户登陆（三次机会重试）'''
USER_INFO_DICT = {'username': 'year', 'pwd': 'year93926'}
i = 0
while i < 3:
    username_input = input('请输入用户名:')
    userpwd_input = input('请输入密码:')
    if username_input == USER_INFO_DICT['username'] and userpwd_input == USER_INFO_DICT['pwd']:
        print('登录成功')
        break
    else:
        i += 1
        print('登录失败 还可重试{0}次'.format(3 - i))
else:
    print('没有机会了88')

'''#8：猜年龄游戏升级版（选做题）
要求：
    允许用户最多尝试3次
    每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y或y, 就继续让其猜3次，以此往复，如果回答N或n，就退出程序
    如何猜对了，就直接退出'''

CORRECT_AGE = 18
i = 0
while i < 3:
    userage_input = int(input('猜猜我的年龄:'))
    if userage_input == CORRECT_AGE:
        print('恭喜你 猜对了')
        break
    else:
        i += 1
        can_gust_time = 3 - i
        if can_gust_time > 0:
            print('猜错了 还剩{0}次机会'.format(can_gust_time))
        else:
            if_want_continue = input('还是猜错了 如果想继续 输入Y/y 获得额外3次机会:')
            if if_want_continue == 'Y' or if_want_continue == 'y':
                i = 0
                continue
            else:
                print('游戏结束')
