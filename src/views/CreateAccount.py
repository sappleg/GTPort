#!/usr/bin/python3.2
'''
Created on Nov 12, 2012

@author: spencer
'''
from tkinter import *

class CreateAccount:

    def __init__(self):
        self.root = Tk()
        self.root.title('Create Account')

        self.username = StringVar()
        self.password = StringVar()
        self.confirmPassword = StringVar()
        self.userType = StringVar()
        self.userType.set("Student")

        self.makeWindow()
        self.root.mainloop()

    # This method is used to construct the actual view. Names of variables
    # should be intuitive. Three frames are used to control the layout of the
    # view using Tk's 'pack' method.
    def makeWindow(self):

        usernameFrame = Frame(self.root)
        usernameFrame.pack(padx=15)

        usernameLabel = Label(usernameFrame, text="Username: ")
        usernameLabel.pack(side=LEFT)

        usernameEntry = Entry(usernameFrame, textvariable = self.username)
        usernameEntry.pack(side=LEFT, padx=10)

        passwordFrame = Frame(self.root)
        passwordFrame.pack(padx=15)

        passwordLabel = Label(passwordFrame, text="Password: ")
        passwordLabel.pack(side=LEFT)

        passwordEntry = Entry(passwordFrame, textvariable = self.password, show='*')
        passwordEntry.pack(side=LEFT, padx=10)

        confirmPasswordFrame = Frame(self.root)
        confirmPasswordFrame.pack(padx=15)

        confirmPasswordLabel = Label(confirmPasswordFrame, text="Confirm Password: ")
        confirmPasswordLabel.pack(side=LEFT)

        confirmPasswordEntry = Entry(confirmPasswordFrame, textvariable = self.confirmPassword, show='*')
        confirmPasswordEntry.pack(side=LEFT, padx=10)

        userTypeFrame = Frame(self.root)
        userTypeFrame.pack(padx=15)

        userTypeLabel = Label(userTypeFrame, text="Confirm Password: ")
        userTypeLabel.pack(side=LEFT)

        userTypeOptionMenu = OptionMenu(userTypeFrame, self.userType, "Student", "Instructor")
        userTypeOptionMenu.pack(side=LEFT)

        buttonFrame = Frame(self.root)
        buttonFrame.pack(fill=X)

        registerButton = Button(buttonFrame, text="Register", command=self.print_this)
        registerButton.pack(side=RIGHT)

        cancelButton = Button(buttonFrame, text="Cancel", command=usernameFrame.quit)
        cancelButton.pack(side=RIGHT)

    # This method is just a place holder to print out the username and password
    # values gathered from the textfields. This will not be used in the actual
    # application
    def print_this(self):
        print(self.username.get())
        print(self.password.get())
        print(self.confirmPassword.get())
        print(self.userType.get())

if __name__=="__main__":
    app = CreateAccount()
