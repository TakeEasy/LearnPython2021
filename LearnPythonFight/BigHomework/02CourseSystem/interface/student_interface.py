from db import models


def student_register_interface(username, password):
    student_obj = models.Student.select(username)
    if student_obj:
        return False, '该学生已经存在'

    student_obj = models.Student(username, password)
    student_obj.save()
    return True, '注册成功'


def student_login_interface(username, password):
    student_obj = models.Student.select(username)
    if not student_obj:
        return False, '用户不存在'
    if password == student_obj.pwd:
        return True, '登录成功'
    else:
        return False, '密码错误'


def choose_school_interface(schoolname, studentname):
    student_obj = models.Student.select(studentname)
    if student_obj.school:
        return False, '当前学生已经选择过学校'
    student_obj.add_school(schoolname)
    return True, f'选择[{schoolname}]成功'


def get_course_list_interface(studentname):
    student_obj = models.Student.select(studentname)
    schoolname = student_obj.school
    if not schoolname:
        return False, '当前学生还没有选择学校'

    school_obj = models.School.select(schoolname)

    course_list = school_obj.course_list
    if course_list:
        return True, course_list
    else:
        return False, '当前学校没有开设课程'


def choose_course_interface(coursename, studentname):
    student_obj = models.Student.select(studentname)
    if coursename in student_obj.course:
        return False, '当前学生已经选择过该课程'
    student_obj.add_course(coursename)
    return True, f'选择[{coursename}]成功'


def check_score_interface(studentname):
    student_obj = models.Student.select(studentname)
    if student_obj.score:
        return student_obj.score
    else:
        return None
