# 1.管理班级,可创建班级,根据学员qq号把学员加入班级

from core import dbapi

class Teacher(object):
    def __init__(self,name):
        self.name = name
        # self.password = password
        self.session = dbapi.Session_class()
        # get user info
        self.obj_teac = self.session.query(dbapi.Teachers).filter_by(name=self.name).first()
        self.info()
    def create_student(self):
        '''
        add a new student to database with qq,name,password
        :return:
        '''
        import re
        qq = input("Input qq number:").strip()
        name = input("Input name:").strip()
        psd = input("Input password:").strip()
        qq = re.search(r'^[^0]\d*', qq).group()
        try:
            student = dbapi.Students(qq=qq,name=name)
            psd_obj = dbapi.Password(md5=psd,stu_qq=qq)
            self.session.add(student)
            self.session.commit()
            print("Updating table students...")
            self.session.add(psd_obj)
            self.session.commit()
            print("Updating table password...")
        except Exception as e:
            self.session.rollback()
            print("Failed with error:",e)
        else:
            print("Updated successfully!")

    def create_teacher(self):
        name = input("Input name:").strip()
        psd = input("Input password:").strip()
        try:
            teacher = dbapi.Teachers(name=name)
            print("Updating table teachers...")
            self.session.add(teacher)
            self.session.commit()
            teacher_obj = self.session.query(dbapi.Teachers).filter_by(name=name).first()
            passwd = dbapi.Password(md5=psd,teacher_id=teacher_obj.id)
            print("Updating table password...")
            self.session.add(passwd)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            print("Failed with error:",e)
        else:
            print("Updated successfully!")

    def create_class(self):
        name = input("Input name:").strip()
        try:
            new_class = dbapi.Classes(name=name)
            print("Updating table classes...")
            self.session.add(new_class)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            print("Failed with error:", e)
        else:
            print("Updated successfully!")

    def create_course(self):
        name = input("Input name:").strip()
        try:
            course = dbapi.Courses(name=name)
            print("Updating table classes...")
            self.session.add(course)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            print("Failed with error:", e)
        else:
            print("Updated successfully!")

    def active_class(self):
        '''
        associate course,teacher with a specific class
        :return:
        '''
        try:
            choice_list = []
            print("class".center(20,'-'))
            classes = self.session.query(dbapi.Classes).all()
            for c in classes:
                if not c.course_id: # un select class name
                    print("Class ID:%s Name:%s"%(c.id,c.name))
            inp = input(">>:").strip()
            choice_list.append(inp)

            print("teacher".center(20, '-'))
            tea_objs = self.session.query(dbapi.Teachers).all()
            for t in tea_objs:
                if not t.teac_back: # has join a class
                    print("ID:%s Name:[%s]" % (t.id, t.name))
            inp = input(">>:").strip()
            choice_list.append(inp)

            print("course".center(20,'-'))
            course_objs = self.session.query(dbapi.Courses).all()
            for cour in course_objs:
                print("ID:%s Name:[%s]" % (cour.id, cour.name))
            inp = input(">>:").strip()
            choice_list.append(inp)

            cla_obj = self.session.query(dbapi.Classes).filter_by(id=choice_list[0]).first()
            cla_obj.teacher_id =choice_list[1]
            cla_obj.course_id =choice_list[2]
            print("Updating table classes...")
            self.session.commit()
        except Exception as e:
            print('Failed with error:',e)
        else:
            print("Success!")

    def manage_student(self):
        '''
        add or delete student in my class
        :return:
        '''
        try:
            cla_objs = self.obj_teac.teac_back
            if cla_objs and len(cla_objs) == 1: # has own a class
                cla_obj = cla_objs[0] # get my class obj
                stu_objs = cla_obj.stu_back  # students obj in my class
                print("There are [%s] students in your class" % len(stu_objs))
                choose = input("add/del students?")
                if choose == 'add':
                    in_list = input("Input qq number of student(part with space):").strip().split()
                    add_list = cla_obj.stu_back
                    for qq_in in in_list:
                        find = self.session.query(dbapi.Students).filter_by(qq=qq_in).first()
                        if not find:
                            print("Add qq [%s] failed,not in students table!" % qq_in)
                        else:  # exist this qq number
                            add_list.append(find)
                    print("Updating ...")
                    cla_obj.stu_back = add_list # bind students to my class

                elif choose == 'del':
                    del_qq = input("Input qq number you want to remove:")
                    del_obj = self.session.query(dbapi.Students).filter_by(qq=del_qq).first()
                    cla_obj.stu_back.remove(del_obj)
                    print("Updating ...")
                    self.session.commit()

                else:
                    print("Invalid input!")
        except Exception as e:
            self.session.rollback()
            print('Failed with error:', e)
        else:
            print("Finished!")

    def having_lession(self):
        '''
        spawn a record of current class (both teacher and students),
        assign homework for students
        :return:
        '''
        from _datetime import datetime
        now = datetime.now()
        try:
            cla_objs = self.obj_teac.teac_back
            if cla_objs and len(cla_objs) == 1:
                cla_obj = cla_objs[0]
                # create record to table records
                record = dbapi.Records(date=now,class_id=cla_obj.id)
                print("%s,teacher [%s] is teaching [%s] in class [%s]"
                      %(now,self.obj_teac.name,cla_obj.course_reship.name,cla_obj.name))
                print("Updating...")
                self.session.add(record)
                self.session.commit()

                # create homework to table hmwork
                print("Please assign homework for students.")
                h_name = input("Homework name:").strip()
                desc = input("Input description:").strip()
                homework = dbapi.Hmwork(name=h_name,description=desc,class_id=cla_obj.id)
                print("Updating...")
                self.session.add(homework)
                self.session.commit()

                # create score to table scores
                h_obj = self.session.query(dbapi.Hmwork).filter_by(name=h_name).first()
                print("Updating...")
                for student in cla_obj.stu_back:
                    score = dbapi.Scores(stu_qq=student.qq,hmwork_id=h_obj.id)
                    self.session.add(score)
                    self.session.commit()
        except Exception as e:
            self.session.rollback()
            print('Failed with error:', e)
        else:
            print("Finished!")

    def review_homework(self):
        '''
        assess homework of students
        :return:
        '''
        try:
            cla_objs = self.obj_teac.teac_back
            if cla_objs and len(cla_objs)==1 :  # has own a class
                cla_obj = cla_objs[0]
                stu_objs = cla_obj.stu_back
                print("There are %s students in your class" % len(stu_objs))

                print("What is the homework you want to review?")
                for i in cla_obj.hmwork_back:
                    print("H_id:%s H_name:%s H_desc:%s"%(i.id,i.name,i.description))
                h_id = input("Input homework ID>>:")
                for stu in stu_objs:
                    score_obj = self.session.query(dbapi.Scores).filter_by(
                        stu_qq=stu.qq).filter_by(
                        hmwork_id=h_id).first()
                    if score_obj and score_obj.submit_state:
                        submit = 'yes'
                        print('''
                        name:%s submit_state:%s mark:%s
                        '''%(stu.name,submit,score_obj.mark))
                        new_mark = input("New mark(<=100):")
                        score_obj.mark = new_mark
                        print("Updating...")
                        self.session.commit()
                    else:
                        print("The student [%s] haven't submit!"%stu.name)
            else:
                print("You are not responsible for any class!")
        except Exception as e:
            self.session.rollback()
            print('Failed with error:', e)
        else:
            print("Finished!")

    def info(self):
        print("hi,teacher [%s]!"%self.name)
        if not self.obj_teac.teac_back:
            print("You haven't join a class")

