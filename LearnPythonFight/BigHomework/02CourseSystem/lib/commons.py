'''
公共方法
'''


def auth(role):
    def login_auth(func):
        from core import admin, student, teacher
        from functools import wraps
        @wraps(func)
        def wrapper(*args, **kwargs):
            if role == 'admin':
                if admin.admin_info['user']:
                    res = func(*args, **kwargs)
                    return res
                else:
                    admin.login()
            elif role == 'student':
                if student.student_info['user']:
                    res = func(*args, **kwargs)
                    return res
                else:
                    student.login()
            elif role == 'teacher':
                if teacher.teacher_info['user']:
                    res = func(*args, **kwargs)
                    return res
                else:
                    teacher.login()

            else:
                print('当前视图没有权限')

        return wrapper

    return login_auth
