import sys
from views.Login import Login
from views.StudentHomepage import StudentHomepage
from views.FacultyHomepage import FacultyHomepage
from views.AdminHomepage import AdminHomepage
from views.StudentPI import StudentPI
from views.FacultyPI import FacultyPI
from views.StudentServices import StudentServices
from views.FacultyServices import FacultyServices

class Driver:

    def __init__(self):
        login = Login(self)

    def launch_homepage(self,counts):
        if counts[0]:
            shp = StudentHomepage(self)
        elif counts[1]:
            fhp = FacultyHomepage(self)
        elif counts[2]:
            ahp = AdminHomepage(self)

    def launch_homepage_next(self,selection,user_type):
        if user_type == "student":
            if selection == 0:
                spi = StudentPI()
            elif selection == 1:
                ss = StudentServices()
        elif user_type == "instructor":
            if selection == 0:
                fpi = FacutlyPI()
            elif selection == 1:
                fs = FacultyServices()
        elif user_type == "admin":
            if selection == 0:
                print("View Adminsitrative Report")
            elif selection == 1:
                print("Add New Course")

if __name__=="__main__":
    driver = Driver()
