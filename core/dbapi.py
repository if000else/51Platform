from sqlalchemy import create_engine,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,DATETIME,Table
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("mysql+pymysql://root:123456@10.0.0.6/platform?charset=utf8",echo=False)
Base = declarative_base()

# table map

# mul to mul, self management by system
class_m2m_stu = Table('class_m2m_stu', Base.metadata,
                        Column('stu_qq',String(20),ForeignKey('students.qq')),
                        Column('class_id',Integer,ForeignKey('classes.id')),
                        )

class Students(Base):
    '''
    students table
    '''
    __tablename__ = 'students'
    qq = Column(String(20),nullable=False,primary_key=True)
    name = Column(String(32))
    # m2m with classes
    class_reship = relationship('Classes',secondary=class_m2m_stu,backref='stu_back')

class Teachers(Base):
    '''
    teachers table
    '''
    __tablename__ = 'teachers'
    id = Column(Integer,autoincrement=True,primary_key=True)
    name = Column(String(32),nullable=False)

class Password(Base):
    '''
    password table
    '''
    __tablename__ = 'password'
    id = Column(Integer,autoincrement=True,primary_key=True)
    md5 = Column(String(64),nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    # backref
    # teac_reship = relationship("Teachers", backref="teac_back")
    stu_qq = Column(String(20), ForeignKey('students.qq'))
    # backref
    # stu_reship = relationship("Students", backref="stu_back")

class Classes(Base):
    '''
    classes table
    '''
    __tablename__ = 'classes'
    id = Column(Integer,autoincrement=True,primary_key=True)
    name = Column(String(32),nullable=False)

    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    # backref
    teac_reship = relationship("Teachers", backref="teac_back")

    course_id = Column(Integer, ForeignKey('courses.id'))
    # backref
    course_reship = relationship("Courses", backref="course_back")

    record_id = Column(Integer, ForeignKey('records.id'))
    # backref
    reco_reship = relationship("Records", backref="reco_back")

    hmwork_id = Column(Integer, ForeignKey('hmwork.id'))
    # backref
    hmwork_reship = relationship("Hmwork", backref="hmwork_back")

class Records(Base):
    '''
    records table
    '''
    __tablename__ = 'records'
    id = Column(Integer,autoincrement=True,primary_key=True)
    date = Column(DATETIME,nullable=False)

class Hmwork(Base):
    '''
    hmwork table
    '''
    __tablename__ = 'hmwork'
    id = Column(Integer,autoincrement=True,primary_key=True)
    name = Column(String(64),nullable=False)
    # stu_qq = Column(String(20),ForeignKey('students.qq'))
    # mark = Column(Integer)
    # submit_state = Column(String(3))
    # #backref
    # stu_reship = relationship("Students",backref="stu_back")
    # def __repr__(self):
    #     return "<detail:(%s|%s|%s|%s)>" % (self.name,self.stu_qq,self.mark,self.submit_state)

class Courses(Base):
    '''
    courses table
    '''
    __tablename__ = 'courses'
    id = Column(Integer,autoincrement=True,primary_key=True)
    name = Column(String(32),nullable=False)

class Scores(Base):
    '''
    score table
    '''
    __tablename__ = 'scores'
    id = Column(Integer,autoincrement=True,primary_key=True)
    mark = Column(Integer)
    submit_state = Column(Integer) # 1 refers 'yes'
    stu_qq = Column(String(20),ForeignKey('students.qq'))
    hmwork_id = Column(Integer,ForeignKey('hmwork.id'))

    # stu_reship = relationship("Students", backref="stu_back")
    # hmwork_reship = relationship("Hmwork", backref="hmwork_back")
    def __repr__(self):
        return '%s|%s|%s|%s'%(self.mark,self.submit_state,self.stu_qq,self.hmwork_id)


Base.metadata.create_all(engine)  # create table structure
Session_class = sessionmaker(bind=engine)

Session = Session_class() # new a instance

# objs = Session.query(Classes).all()
# for i in objs:
#     score = Session.query(Scores).filter(Scores.hmwork_id==i.hmwork_reship.id).first()
#     print(score)
#
# Session.commit()


