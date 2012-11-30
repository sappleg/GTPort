import sys
from views.Login import Login
from views.StudentHomepage import StudentHomepage
from views.FacultyHomepage import FacultyHomepage
from views.AdminHomepage import AdminHomepage

class Driver:

    def __init__(self):
        login = Login(self)

    def launch_homepage(self,counts):
        if counts[0]:
            shp = StudentHomepage()
        elif counts[1]:
            fhp = FacultyHomepage()
        elif counts[2]:
            ahp = AdminHomepage()

if __name__=="__main__":
    driver = Driver()
