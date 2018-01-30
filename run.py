from core import dbapi
from core.teacher import Teacher
from core.student import Student


session = dbapi.Session_class()

def main():
    while True:
        print("Welcome to 51PlatForm")
        print("1.teacher \n2.student")
        roll = input("Choose roll:").strip()
        if roll == '1':
            teacher_flag = True
            while teacher_flag:
                user = input("Input login name:").strip()
                psd = input("Input password:").strip()
                teac_obj = session.query(dbapi.Teachers).filter(
                    dbapi.Teachers.name==user).first()
                if teac_obj:
                    psd_obj = session.query(dbapi.Password).filter(
                        dbapi.Password.teacher_id == teac_obj.id).first()
                    if psd == psd_obj.md5:
                        print("Login successfully")
                        teacher_op(user)
                        break
                else:
                    print("User does not exist!")


        elif roll == '2':
            student_flag = True
            while student_flag:
                user = input("Input qq number:").strip()
                psd = input("Input password:").strip()
                stu_obj = session.query(dbapi.Students).filter(
                    dbapi.Students.qq == user).first()
                if stu_obj:
                    psd_obj = session.query(dbapi.Password).filter(
                        dbapi.Password.stu_qq == stu_obj.qq).first()
                    if psd == psd_obj.md5:
                        print("Login successfully")
                        student_op(user)
                        break
                else:
                    print("User does not exist!")
        else:
            print("Invalid!")

def student_op(qq):
    student = Student(qq)
    print('''
    1.submit my homework
    2.show my scores
    3.show my rank in my class
    4.exit
    ''')
    while True:
        inp = input("Input function>>:")
        if inp == '1':
            student.submit_homwork()
        elif inp == '2':
            student.show_all_scores()
        elif inp == '3':
            student.show_all_rank()
        elif inp == '4':
            break
        else:
            print("Valid!")
def teacher_op(name):
    teacher = Teacher(name)
    print('''
    1.create a student
    2.create a class
    3.create a course
    4.create a teacher
    5.manage students in my class
    6.active a class
    7.have a lesson
    8.review homework
    9.exit
    ''')
    while True:
        inp = input("Input function>>:")
        if inp == '1':
            teacher.create_student()
        elif inp == '2':
            teacher.create_class()
        elif inp == '3':
            teacher.create_course()
        elif inp == '4':
            teacher.create_teacher()
        elif inp == '5':
            teacher.manage_student()
        elif inp == '6':
            teacher.active_class()
        elif inp == '7':
            teacher.having_lession()
        elif inp == '8':
            teacher.review_homework()
        elif inp == '9':
            break
        else:
            print("Invalid!")
if __name__ == '__main__':
    main()



