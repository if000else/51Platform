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
                        teacher = Teacher(user)
                        teacher.info()
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
                        student = Student(user)
                        student.info()
                else:
                    print("User does not exist!")
        else:
            print("Invalid!")


if __name__ == '__main__':
    main()



