'''
公共接口
'''
import os
from config import settings
from db import models


def get_all_school_interface():
    school_dir = os.path.join(
        settings.DB_PATH, 'School'
    )
    if not os.path.exists(school_dir):
        return False, '没有学校先创建学校'
    school_list = os.listdir(school_dir)
    return True, school_list


def login_interface(username, password, user_type):
    user_obj = None
    if user_type == 'admin':
        user_obj = models.Admin.select(username)
    elif user_type == 'student':
        user_obj = models.Student.select(username)
    elif user_type == 'teacher':
        user_obj = models.Teacher.select(username)
    else:
        return False, '请输入正确用户角色'
    if not user_obj:
        return False, '用户不存在'
    if password == user_obj.pwd:
        return True, '登录成功'
    else:
        return False, '密码错误'


def get_course_from_school_interface(schoolname):
    school_obj = models.School.select(schoolname)
    if school_obj.course_list:
        return True, school_obj.course_list
    else:
        return False, '该学校没有课程'
