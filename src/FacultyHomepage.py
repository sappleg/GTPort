#!/usr/bin/python3.2
'''
Created on Nov 12, 2012

@author: spencer
'''
from tkinter import *

class FacultyHomepage:

    def __init__(self):
        self.root = Tk()
        self.root.title('Home Page')

        self.personalInfo = IntVar()
        self.facultyServices = IntVar()

        self.makeWindow()
        self.root.mainloop()

    # This method is used to construct the actual view. Names of variables
    # should be intuitive. Three frames are used to control the layout of the
    # view using Tk's 'pack' method.
    def makeWindow(self):

        radioFrame = Frame(self.root)
        radioFrame.pack(padx=15)
        
        self.personalInfoButton = Radiobutton(self.root, text="Personal Information", variable=self.personalInfo, value=1, command=self.PIRadio)
        self.personalInfoButton.pack(anchor=W)
        
        self.facultyServicesButton = Radiobutton(self.root, text="Faculty Services", variable=self.facultyServices, value=2, command=self.FSRadio)
        self.facultyServicesButton.pack(anchor=W)

        buttonFrame = Frame(self.root)
        buttonFrame.pack(fill=X)

        nextButton = Button(buttonFrame, text="Next", command=self.print_this)
        nextButton.pack(side=RIGHT)

        logoutButton = Button(buttonFrame, text="Logout", command=self.print_this())
        logoutButton.pack(side=RIGHT)
    
    def PIRadio(self):
        self.facultyServicesButton.deselect()
        self.facultyServices.set(0);
        
    def FSRadio(self):
        self.personalInfoButton.deselect()
        self.personalInfo.set(0);

    # This method is just a place holder to print out the username and password
    # values gathered from the textfields. This will not be used in the actual
    # application
    def print_this(self):
        print("Hello World")

if __name__=="__main__":
    app = FacultyHomepage()
