'''
主视图
'''

from core import admin, student, teacher

func_dic = {
    '1': admin.admin_view,
    '2': student.student_view,
    '3': teacher.teacher_view,
}


def run():
    while True:
        print('''
        --------欢迎来到选课系统--------
            1.管理员功能
            2.学生功能
            3.老师功能
        -----------end---------------
        ''')

        choice = input('请输入功能编号:').strip()
        if choice == 'q':
            break
        if choice not in func_dic:
            print('输入错误,重新来')
            continue
        func_dic.get(choice)()
