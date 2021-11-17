'''
管理员视图
'''
from interface import admin_interface, common_interface

from lib import commons

admin_info = {
    'user': None
}


def register():
    while True:
        input_username = input('请输入用户名:').strip()
        input_password = input('请输入密码:').strip()
        input_re_password = input('请确认密码:').strip()
        if input_password == input_re_password:
            flag, msg = admin_interface.admin_register_interface(input_username, input_password)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('两次密码不一致重新来')


def login():
    while True:
        input_username = input('请输入用户名:').strip()
        input_password = input('请输入密码:').strip()
        flag, msg = common_interface.login_interface(input_username, input_password,user_type='admin')
        if flag:
            print(msg)
            admin_info['user'] = input_username
            break
        else:
            print(msg)


@commons.auth('admin')
def create_school():
    while True:
        input_schoolname = input('请输入学校名称:').strip()
        input_schooladdr = input('请输入学校地址:').strip()
        flag, msg = admin_interface.create_school_interface(input_schoolname, input_schooladdr, admin_info['user'])
        if flag:
            print(msg)
            break
        else:
            print(msg)


@commons.auth('admin')
def create_course():
    while True:
        flag, school_list_or_msg = common_interface.get_all_school_interface()
        if not flag:
            print(school_list_or_msg)
            break

        for index, school_name in enumerate(school_list_or_msg):
            print(f'编号:{index} 学校名:{school_name}')

        choice = input('请输入学校编号').strip()
        if not choice.isdigit():
            print('请输入数字')
            continue
        choice = int(choice)

        if choice not in range(len(school_list_or_msg)):
            print('请输入正确编号')
            continue

        school_name = school_list_or_msg[choice]

        input_coursename = input('请输入课程名称:').strip()
        flag, msg = admin_interface.create_course_interface(school_name, input_coursename, admin_info['user'])
        if flag:
            print('msg')
            break
        else:
            print('msg')


@commons.auth('admin')
def create_teacher():
    while True:
        input_teachername = input('请输入老师名:').strip()
        # default_pwd = '666666'
        flag, msg = admin_interface.create_teacher_interface(input_teachername, admin_info['user'])
        if flag:
            print(msg)
            break
        else:
            print(msg)


func_dict = {
    '1': register,
    '2': login,
    '3': create_school,
    '4': create_course,
    '5': create_teacher,
}


def admin_view():
    while True:
        print('''
            1.注册
            2.登录
            3.创建学校
            4.创建课程(先选择学校)
            5.创建讲师
        ''')
        choice = input('请输入功能编号:').strip()
        if choice == 'q':
            break
        if choice not in func_dict:
            print('输入错误,重新来')
            continue
        func_dict.get(choice)()
