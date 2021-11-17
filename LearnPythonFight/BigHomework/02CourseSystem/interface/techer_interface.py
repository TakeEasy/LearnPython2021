from db import models


def get_course_interface(teachername):
    teacher_obj = models.Teacher.select(teachername)
    if teacher_obj.course_list:
        return True, teacher_obj.course_list
    else:
        return False, '该老师没有安排课程'


def add_course_interface(coursename, teachername):
    teacher_obj = models.Teacher.select(teachername)
    if coursename in teacher_obj.course_list:
        return False, '该老师已经在教此课程'
    else:
        teacher_obj.add_course(coursename)
        return True, f'添加[{coursename}]成功'


def get_student_from_course_interface(coursename, teachername):
    teacher_obj = models.Teacher.select(teachername)
    student_list = teacher_obj.get_student(coursename)
    if student_list:
        return True, student_list
    else:
        return False, '该课程没有学生'


def change_student_score_interface(studentname, coursename, score, teachername):
    teacher_obj = models.Teacher.select(teachername)
    teacher_obj.change_score(studentname, coursename, score)
    return True, '修改成功'
