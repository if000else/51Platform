'''

enable sign up before login...
1.submit homework
2.see my score
3.see my rank in class

'''

from core import dbapi

class Student(object):
    def __init__(self,name):
        self.name = name
        # self.password = password
        self.session = dbapi.Session_class()
    def submit_homwork(self):
        obj = self.session.query(dbapi.Classes).first()
        print(obj.name)
    def show_all_scores(self):
        obj = self.session.query(dbapi.Classes).first()
        print(obj.name)
    def show_all_rank(self):
        pass
    def info(self):
        print("hi, i am student [%s]"%self.name)