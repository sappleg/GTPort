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
#from models.Admin import Admin
from views.CreateAccount import CreateAccount

class Driver:
    student = Student()
    faculty = Faculty()

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
            ahp = AdminHomepage(self)

    def launch_homepage_next(self,selection,user_type):
        if user_type == "student":
            if selection == 0:
                spi = StudentPI(self.student.getUsername())
            elif selection == 1:
                ss = StudentServices()
        elif user_type == "instructor":
            if selection == 0:
                fpi = FacultyPI(self, self.faculty.getUsername())
            elif selection == 1:
                fs = FacultyServices()
        elif user_type == "admin":
            if selection == 0:
                print("View Adminsitrative Report")
            elif selection == 1:
                print("Add New Course")

if __name__=="__main__":
    driver = Driver()
