'''

'''
from db import db_handler


class Base:
    @classmethod
    def select(cls, username):
        obj = db_handler.select_data(cls, username)
        return obj

    def save(self):
        db_handler.save(self)


class Admin(Base):
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd

    def create_school(self, schoolname, schooladdr):
        school_obj = School(schoolname, schooladdr)
        school_obj.save()

    def create_course(self, schoolobj, coursename):
        course_obj = Course(coursename)
        course_obj.save()
        schoolobj.course_list.append(coursename)
        schoolobj.save()

    def create_teacher(self, teachername, teacherpwd):
        teacher_obj = Teacher(teachername, teacherpwd)
        teacher_obj.save()


class School(Base):
    def __init__(self, name, addr):
        self.user = name
        self.addr = addr
        self.course_list = []


class Student(Base):
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd
        self.school = None
        self.course_list = []
        self.score = {}
        self.payed = {}

    def add_school(self, schoolname):
        self.school = schoolname
        self.save()

    def add_course(self, coursename):
        self.course_list.append(coursename)
        self.score[coursename] = 0
        self.save()
        course_obj = Course.select(coursename)
        course_obj.student_list.append(self.user)
        course_obj.save()


class Course(Base):
    def __init__(self, coursename):
        self.user = coursename
        self.student_list = []


class Teacher(Base):
    def __init__(self, teachername, teacherpwd):
        self.user = teachername
        self.pwd = teacherpwd
        self.course_list = []

    def add_course(self, coursename):
        self.course_list.append(coursename)
        self.save()

    def show_course(self):
        return self.course_list

    def get_student(self, coursename):
        course_obj = Course.select(coursename)
        return course_obj.student_list

    def change_score(self, studentname, coursename, score):
        student_obj = Student.select(studentname)
        student_obj.score[coursename] = score
        student_obj.save()
