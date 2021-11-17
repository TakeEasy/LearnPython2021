'''
admin逻辑接口层
'''
from db import models


def admin_register_interface(username, password):
    admin_obj = models.Admin.select(username)
    if admin_obj:
        return False, '用户已经存在'

    admin_obj = models.Admin(username, password)
    admin_obj.save()
    return True, '注册成功'


def admin_login_interface(username, password):
    admin_obj = models.Admin.select(username)
    if not admin_obj:
        return False, '用户不存在'
    if password == admin_obj.pwd:
        return True, '登录成功'
    else:
        return False, '密码错误'


def create_school_interface(schoolname, schooladdr, adminname):
    school_obj = models.School.select(schoolname)
    if school_obj:
        return False, '学校已经存在'

    admin_obj = models.Admin.select(adminname)
    admin_obj.create_school(schoolname, schooladdr)
    return True, f'学校[{schoolname}]创建成功'


def create_course_interface(schoolname, coursename, adminname):
    school_obj = models.School.select(schoolname)
    if coursename in school_obj.course_list:
        return False, '该课程已经在该学校存在'

    admin_obj = models.Admin.select(adminname)

    admin_obj.create_course(school_obj, coursename)

    return True, f'课程[{coursename}]在校区[{schoolname}]创建成功'


def create_teacher_interface(teachername, adminname, teacher_pwd='666666'):
    teacher_obj = models.Teacher.select(teachername)
    if teacher_obj:
        return False, '该老师已经存在'

    admin_obj = models.Admin.select(adminname)
    admin_obj.create_teacher(teachername, teacher_pwd)
    return True, f'老师[{teachername}]创建成功'
