import sys
from views.Login import Login
from views.StudentHomepage import StudentHomepage
from views.FacultyHomepage import FacultyHomepage
from views.AdminHomepage import AdminHomepage
from views.StudentPI import StudentPI
from views.FacultyPI import FacultyPI
from views.StudentServices import StudentServices
from views.FacultyServices import FacultyServices
from models.Student import Student
from models.Faculty import Faculty
from models.Admin import Admin
from views.CreateAccount import CreateAccount
from views.SelectDepartment import SelectDepartment
from views.AdminReport import AdminReport
from views.StudentReport import StudentReport

class Driver:
    student = Student()
    faculty = Faculty()
    admin = Admin()

    def __init__(self):
        login = Login(self)

    def create_account(self):
        ca = CreateAccount(self)

    def return_login(self):
        login = Login(self)

    def launch_homepage(self,counts,username):
        if counts[0]:
            self.student.setUsername(username)
            shp = StudentHomepage(self)
        elif counts[1]:
            self.faculty.setUsername(username)
            fhp = FacultyHomepage(self)
        elif counts[2]:
            self.admin.setUsername(username)
            ahp = AdminHomepage(self)

    def launch_homepage_next(self,selection,user_type):
        if user_type == "student":
            if selection == 0:
                spi = StudentPI(self.student.getUsername(),self)
            elif selection == 1:
                ss = StudentServices(self)
        elif user_type == "instructor":
            if selection == 0:
                fpi = FacultyPI(self, self.faculty.getUsername())
            elif selection == 1:
                fs = FacultyServices(self)
        elif user_type == "admin":
            if selection == 0:
                ar = AdminReport(self, self.admin.getUsername())

    def register_courses(self):
        sd = SelectDepartment(self)

    def find_tutors(self):
        print("placeholder")
        #ft = FindTutors(self)

    def tutor_logbook(self):
        print("placeholder1")

    def grading_pattern(self):
        gp = StudentReport(self, self.student.getUsername())

    def assign_grades(self):
        print("placeholder4")

    def assign_tutors(self):
        print("placeholder5")

    def view_student_performance(self):
        print("placeholder6")

if __name__=="__main__":
    driver = Driver()
