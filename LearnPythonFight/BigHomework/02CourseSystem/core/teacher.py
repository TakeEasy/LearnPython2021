'''
老师视图
'''

from interface import teacher_interface, common_interface
from lib import commons

teacher_info = {
    'user': None
}


def register():
    pass


def login():
    while True:
        input_username = input('请输入用户名:').strip()
        input_password = input('请输入密码:').strip()
        flag, msg = common_interface.login_interface(input_username, input_password, user_type='teacher')
        if flag:
            print(msg)
            teacher_info['user'] = input_username
            break
        else:
            print(msg)


@commons.auth('teacher')
def check_course():
    flag, course_list_or_msg = teacher_interface.get_course_interface(teacher_info['user'])
    print(course_list_or_msg)


@commons.auth('teacher')
def choose_course():
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
        flag, course_list_or_msg = common_interface.get_course_from_school_interface(school_name)
        if not flag:
            print(course_list_or_msg)
            break

        for index, course_name in enumerate(course_list_or_msg):
            print(f'编号:{index} 课程名:{course_name}')

        choice = input('请输入课程编号').strip()
        if not choice.isdigit():
            print('请输入数字')
            continue
        choice = int(choice)

        if choice not in range(len(course_list_or_msg)):
            print('请输入正确编号')
            continue
        course_name = course_list_or_msg[choice]

        flag, msg = teacher_interface.add_course(course_name, teacher_info['user'])
        if flag:
            print(msg)
            break
        else:
            print(msg)


@commons.auth('teacher')
def check_stu_from_course():
    while True:
        flag, course_list_or_msg = teacher_interface.get_course_interface(teacher_info['user'])
        if not flag:
            print(course_list_or_msg)
            break

        for index, course_name in enumerate(course_list_or_msg):
            print(f'编号:{index} 课程名:{course_name}')

        choice = input('请输入课程编号').strip()
        if not choice.isdigit():
            print('请输入数字')
            continue
        choice = int(choice)

        if choice not in range(len(course_list_or_msg)):
            print('请输入正确编号')
            continue
        course_name = course_list_or_msg[choice]
        flag, student_list_or_msg = teacher_interface.get_student_from_course(course_name, teacher_info['user'])
        if flag:
            print(student_list_or_msg)
            break
        else:
            print(student_list_or_msg)


@commons.auth('teacher')
def change_score_from_stu():
    while True:
        flag, course_list_or_msg = teacher_interface.get_course_interface(teacher_info['user'])
        if not flag:
            print(course_list_or_msg)
            break

        for index, course_name in enumerate(course_list_or_msg):
            print(f'编号:{index} 课程名:{course_name}')

        choice = input('请输入课程编号').strip()
        if not choice.isdigit():
            print('请输入数字')
            continue
        choice = int(choice)

        if choice not in range(len(course_list_or_msg)):
            print('请输入正确编号')
            continue
        course_name = course_list_or_msg[choice]
        flag, student_list_or_msg = teacher_interface.get_student_from_course_interface(course_name,
                                                                                        teacher_info['user'])
        if not flag:
            print(student_list_or_msg)
            break

        for index, student_name in enumerate(student_list_or_msg):
            print(f'编号:{index} 学生名:{student_name}')

        choice = input('请输入学生编号').strip()
        if not choice.isdigit():
            print('请输入数字')
            continue
        choice = int(choice)

        if choice not in range(len(student_list_or_msg)):
            print('请输入正确编号')
            continue
        student_name = student_list_or_msg[choice]

        input_score = input('请输入学生分数:').strip()
        if not input_score.isdigit():
            print('请输入数字')
            continue
        input_score = int(input_score)

        flag, msg = teacher_interface.change_student_score_interface(student_name, course_name, input_score,
                                                                     teacher_info['user'])
        if flag:
            print(msg)
            break
        else:
            print(msg)


func_dict = {
    '1': register,
    '2': login,
    '3': check_course,
    '4': choose_course,
    '5': check_stu_from_course,
    '6': change_score_from_stu,
}


def teacher_view():
    while True:
        print('''
            1.登录
            2.查看教授课程
            3.选择教授课程
            4.查看课程下学生
            5.修改学生分数
        ''')
        choice = input('请输入功能编号:').strip()
        if choice == 'q':
            break
        if choice not in func_dict:
            print('输入错误,重新来')
            continue
        func_dict.get(choice)()
