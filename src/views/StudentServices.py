#!/usr/bin/python3.2
'''
Created on Nov 12, 2012

@author: spencer
'''
from tkinter import *
from tkinter.messagebox import showwarning
import pymysql

# This is a class called Login. We will be able to use this class to create
# several instances of this view. Therefore we could have several users
# accessing our application at once (prob not necessary for this project)
# but it will help with code flow as well
class StudentServices:

    # This is the constructor of the login view. Here I create the Tk object,
    # username and password variables (specific to each instance of Login). I also
    # construct the view and run it through the computer's clock cycles (makeWindow
    # and mainloop)
    def __init__(self,driver, un):
        self.Driver = driver
        self.username = un

        self.root = Tk()
        self.root.title('Student Services')

        self.makeWindow()
        self.root.mainloop()

    # This method is used to construct the actual view. Names of variables
    # should be intuitive. Three frames are used to control the layout of the
    # view using Tk's 'pack' method.
    def makeWindow(self):

        buttonFrame = Frame(self.root)
        buttonFrame.pack(side=BOTTOM)

        registerButton = Button(buttonFrame, text="Register for Courses", command=self.register_for_courses)
        registerButton.pack(side=TOP)

        updatePIButton = Button(buttonFrame, text="Update Personal Information", command=self.update_PI)
        updatePIButton.pack(side=TOP)

        findTutorsButton = Button(buttonFrame, text="Find Tutors", command=self.find_tutors)
        findTutorsButton.pack(side=TOP)

        tutorLBButton = Button(buttonFrame, text="Tutor Logbook", command=self.tutor_logbook)
        tutorLBButton.pack(side=TOP)

        gradePatternButton = Button(buttonFrame, text="View Grading Pattern", command=self.grading_pattern)
        gradePatternButton.pack(side=TOP)

    def register_for_courses(self):
        self.root.destroy()
        self.Driver.register_courses()

    def update_PI(self):
        self.root.destroy()
        self.Driver.launch_homepage_next(0,"student")

    def find_tutors(self):
        self.root.destroy()
        self.Driver.find_tutors()

    def tutor_logbook(self):
        self.db = pymysql.connect(host = "academic-mysql.cc.gatech.edu" , passwd = "a1Rlxylj" , user ="cs4400_Group36", db='cs4400_Group36')
        c = self.db.cursor()
        SQL = "SELECT count( *) FROM tutorsFor WHERE tutorUsername = %s"
        c.execute(SQL, self.username)
        counts = c.fetchall()[0][0]
        c.close()
        self.db.close()
        if (counts == 0):
            showwarning("ERROR", "You are not a tutor!")
            return
        else:
            self.root.destroy()
            self.Driver.tutor_logbook()


    def grading_pattern(self):
        self.root.destroy()
        self.Driver.grading_pattern()

    # This method is just a place holder to print out the username and password
    # values gathered from the textfields. This will not be used in the actual
    # application
    def print_this(self):
        print("hello world")

# This is the main method of the Login file to be used for debuggin purposes.
# This method is used to create an instance of the Login class.
if __name__=='__main__':
    app = StudentServices()
