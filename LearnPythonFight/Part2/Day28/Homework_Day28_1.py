class School:
    school_name = 'GUPT'

    def __init__(self, nick_name, addr):
        self.nick_name = nick_name
        self.addr = addr
        self.classes = []

    def related(self, class_name):
        self.classed.append(class_name)

    def tell_classes(self):
        for related_class in self.classes:
            print(f'{self.nick_name}:{related_class.name}:{related_class.courses}')


class Class:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def related_course(self, course):
        self.courses.append(course)

    def tell_courses(self):
        for course in self.courses:
            print(f'{self.name}:{course}')


class Course:
    def __init__(self, name, period, price):
        self.name = name
        self.period = period
        self.price = price

    def tell_info(self):
        print(f'{self.name}:{self.period}:{self.price}')


class Student:
    pass
