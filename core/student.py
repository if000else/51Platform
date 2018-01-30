'''

enable sign up before login...
1.submit homework
2.see my score
3.see my rank in class

'''

from core import dbapi

class Student(object):
    def __init__(self,qq):
        self.qq = qq
        # self.password = password
        self.session = dbapi.Session_class()
        # get user info
        self.obj_stu = self.session.query(dbapi.Students).filter_by(qq=self.qq).first()
        self.objs_class = self.obj_stu.class_reship # get user's class
        self.info()
    def submit_homwork(self):
        '''
        submit homework (change table 'scores.submit_state' to 1 )
        :return:
        '''
        # show all homework
        score = self.obj_stu.score_back
        if score: # exist
            for s in score: # s-->obj of Scores()
                submit = 'no'
                if s.submit_state == 1:
                    submit = 'yes'
                    print("Find a result submitted:")
                    print('user:%s homework:%s submit:%s mark:%s'
                          %(self.obj_stu.name,s.hmwork_reship.name,submit,s.mark)
                          )
                    print("This homework has submitted!")
                else:
                    print('user:%s homework:%s submit:%s mark:%s'
                          % (self.obj_stu.name, s.hmwork_reship.name, submit,s.mark)
                          )
                    tip = input("Are you sure to submit homework? yes/no")
                    if tip == 'yes':
                        s.submit_state = 1
                        self.session.commit() # sync
                        print("Updating...")
                        print("Finish!")
        else:
            print("No homework to submit!")

    def show_all_scores(self):
        # # name course score homework
        score_list = self.obj_stu.score_back #
        if score_list:
            for item in score_list: # score obj
                if item.mark:
                    print(self.obj_stu.name,item.hmwork_reship.name,item.mark)
        else:
            print("Nothing to show!")

    def show_all_rank(self):
        print("You have join [%s] class"%len(self.objs_class))
        for cla in self.objs_class:
            students = cla.stu_back
            print("There are [%s] people in your class [%s]"%(len(students),cla.name))


    def info(self):
        print("Welcome! Student [%s]"%self.obj_stu.name)
        if not self.objs_class:
            print("You haven't choose any class!")