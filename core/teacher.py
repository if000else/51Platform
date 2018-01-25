# 1.管理班级,可创建班级,根据学员qq号把学员加入班级
'''
login:
1.create class
    select classes table
    add:name char 32
    select classes table
2.create teacher
    select teachers table
    add:name char 32
    select teachers table
3.create student
    select classes table
    choose class
    select students table
    add stu qq
    select classes table
4.create course
    select teachers table
    add:name char 32
    select teachers table
5.active a class
    show class, if class exclude course,select
    if not teacher,add,
    if not course,add,
    if
6.start a lesson
7.assess homework

'''
from core import dbapi

class Teacher(object):
    def __init__(self,name):
        self.name = name
        # self.password = password
        self.session = dbapi.Session_class()
    def add_student(self):
        obj = self.session.query(dbapi.Classes).first()
        print(obj.name)
        self.session.commit()
    def create_teacher(self):
        obj = self.session.query(dbapi.Classes).first()
        print(obj.name)
        self.session.commit()
    def create_class(self):
        obj = self.session.query(dbapi.Classes).first()
        print(obj.name)
        self.session.commit()
    def create_course(self):
        obj = self.session.query(dbapi.Classes).first()
        print(obj.name)
        self.session.commit()
    def active_class(self):
        obj = self.session.query(dbapi.Classes).first()
        print(obj.name)
        self.session.commit()
    def having_lession(self):
        obj = self.session.query(dbapi.Classes).first()
        print(obj.name)
        self.session.commit()
    def info(self):
        print("hi, i am teacher [%s]!"%self.name)

