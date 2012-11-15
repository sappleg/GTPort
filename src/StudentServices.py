#!/usr/bin/python3.2
'''
Created on Nov 12, 2012

@author: spencer
'''
from tkinter import *

# This is a class called Login. We will be able to use this class to create
# several instances of this view. Therefore we could have several users
# accessing our application at once (prob not necessary for this project)
# but it will help with code flow as well
class StudentServices:

    # This is the constructor of the login view. Here I create the Tk object,
    # username and password variables (specific to each instance of Login). I also
    # construct the view and run it through the computer's clock cycles (makeWindow
    # and mainloop)
    def __init__(self):
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

        registerButton = Button(buttonFrame, text="Register for Courses", command=self.print_this)
        registerButton.pack(side=BOTTOM)

        updatePIButton = Button(buttonFrame, text="Update Personal Information", command=self.print_this)
        updatePIButton.pack(side=BOTTOM)

        findTutorsButton = Button(buttonFrame, text="Find Tutors", command=self.print_this)
        findTutorsButton.pack(side=BOTTOM)

        tutorLBButton = Button(buttonFrame, text="Tutor Logbook", command=self.print_this)
        tutorLBButton.pack(side=BOTTOM)

        gradePatternButton = Button(buttonFrame, text="View Grading Pattern", command=self.print_this)
        gradePatternButton.pack(side=BOTTOM)

    # This method is just a place holder to print out the username and password
    # values gathered from the textfields. This will not be used in the actual
    # application
    def print_this(self):
        print("hello world")

# This is the main method of the Login file to be used for debuggin purposes.
# This method is used to create an instance of the Login class.
if __name__=='__main__':
    app = StudentServices()
