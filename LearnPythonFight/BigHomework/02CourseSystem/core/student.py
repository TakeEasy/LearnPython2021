'''
学生视图
'''
from interface import student_interface, common_interface
from lib import commons

student_info = {
    'user': None
}


def register():
    while True:
        input_username = input('请输入用户名:').strip()
        input_password = input('请输入密码:').strip()
        input_re_password = input('请确认密码:').strip()
        if input_password == input_re_password:
            flag, msg = student_interface.student_register_interface(input_username, input_password)
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
        flag, msg = common_interface.login_interface(input_username, input_password, user_type='student')
        if flag:
            print(msg)
            student_info['user'] = input_username
            break
        else:
            print(msg)


@commons.auth('student')
def choose_school():
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
        flag, msg = student_interface.choose_school_interface(school_name, student_info['user'])
        if flag:
            print('msg')
            break
        else:
            print('msg')


@commons.auth('student')
def choose_course():
    while True:
        flag, course_list_or_msg = student_interface.get_course_list_interface(student_info['user'])
        if not flag:
            print(course_list_or_msg)
            break
        for index, course_name in enumerate(course_list_or_msg):
            print(f'编号:{index} 课程名:{course_name}')

        choice = input('请输入学校编号').strip()
        if not choice.isdigit():
            print('请输入数字')
            continue
        choice = int(choice)

        if choice not in range(len(course_list_or_msg)):
            print('请输入正确编号')
            continue
        course_name = course_list_or_msg[choice]
        flag, msg = student_interface.choose_course_interface(course_name, student_info['user'])
        if flag:
            print('msg')
            break
        else:
            print('msg')


@commons.auth('student')
def check_score():
    score = student_interface.check_score_interface(
        student_info['user']
    )
    if not score:
        print('没有选择课程')
    print(score)


func_dict = {
    '1': register,
    '2': login,
    '3': choose_school,
    '4': choose_course,
    '5': check_score,
}


def admin_view():
    while True:
        print('''
            1.注册
            2.登录功能
            3.选择校区
            4.选择课程
            5.查看分数
        ''')
        choice = input('请输入功能编号:').strip()
        if choice == 'q':
            break
        if choice not in func_dict:
            print('输入错误,重新来')
            continue
        func_dict.get(choice)()
