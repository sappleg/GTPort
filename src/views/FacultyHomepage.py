#!/usr/bin/python3.2
'''
Created on Nov 12, 2012

@author: spencer
'''
from tkinter import *

class FacultyHomepage:

    def __init__(self, driver):
        self.Driver = driver

        self.root = Tk()
        self.root.title('Home Page')

        self.selection = IntVar()
        self.selection.set(0)

        self.makeWindow()
        self.root.mainloop()

    # This method is used to construct the actual view. Names of variables
    # should be intuitive. Three frames are used to control the layout of the
    # view using Tk's 'pack' method.
    def makeWindow(self):

        radioFrame = Frame(self.root)
        radioFrame.pack(padx=15)

        personalInfoButton = Radiobutton(self.root, text="Personal Information",
                variable=self.selection, value=0)
        personalInfoButton.pack(anchor=W)

        facultyServicesButton = Radiobutton(self.root, text="Faculty Services",
                variable=self.selection, value=1)
        facultyServicesButton.pack(anchor=W)

        buttonFrame = Frame(self.root)
        buttonFrame.pack(fill=X)

        nextButton = Button(buttonFrame, text="Next", command=self.next_step)
        nextButton.pack(side=RIGHT)

    def next_step(self):
        self.root.destroy()
        self.Driver.launch_homepage_next(self.selection.get(),"instructor")

if __name__=="__main__":
    app = FacultyHomepage()
