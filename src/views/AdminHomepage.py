#!/usr/bin/python3.2
'''
Created on Nov 12, 2012

@author: spencer
'''
from tkinter import *
from tkinter.messagebox import showinfo

class AdminHomepage:

    def __init__(self, driver):
        self.Driver = driver

        self.root = Tk()
        self.root.title('Home Page')

        self.selection = IntVar()

        self.makeWindow()
        self.root.mainloop()

    # This method is used to construct the actual view. Names of variables
    # should be intuitive. Three frames are used to control the layout of the
    # view using Tk's 'pack' method.
    def makeWindow(self):

        radioFrame = Frame(self.root)
        radioFrame.pack(padx=15)

        self.adminReportButton = Radiobutton(self.root, text="View Administrative Report",
                variable=self.selection, value=0)
        self.adminReportButton.pack(anchor=W)

        self.addCourseButton = Radiobutton(self.root, text="Add New Course",
                variable=self.selection, value=1)
        self.addCourseButton.pack(anchor=W)

        buttonFrame = Frame(self.root)
        buttonFrame.pack(fill=X)

        nextButton = Button(buttonFrame, text="Next", command=self.next_step)
        nextButton.pack(side=RIGHT)

    def next_step(self):
        if self.selection.get() == 0:
            self.root.destroy()
            self.Driver.launch_homepage_next(self.selection.get(),"admin")
        elif self.selection.get() == 1:
            showinfo("ERROR","This set is not part of the required\nfunctionalities for Phase III.\nPlease make a different selection.")
            self.selection.set(0)

if __name__=="__main__":
    app = AdminHomepage()
