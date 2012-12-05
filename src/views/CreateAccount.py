#!/usr/bin/python3.2
'''
Created on Nov 12, 2012

@author: spencer
'''
from tkinter import *
import pymysql
from tkinter.messagebox import showwarning
from tkinter.messagebox import showinfo

class CreateAccount:

    def __init__(self, driver):
        self.Driver = driver
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

        userTypeLabel = Label(userTypeFrame, text="Account Type: ")
        userTypeLabel.pack(side=LEFT)

        userTypeOptionMenu = OptionMenu(userTypeFrame, self.userType, "--", "Student", "Instructor")
        userTypeOptionMenu.pack(side=LEFT)

        buttonFrame = Frame(self.root)
        buttonFrame.pack(fill=X)

        registerButton = Button(buttonFrame, text="Register", command=self.register)
        registerButton.pack(side=RIGHT)

        cancelButton = Button(buttonFrame, text="Cancel", command=self.cancel)
        cancelButton.pack(side=RIGHT)

    # This method is just a place holder to print out the username and password
    # values gathered from the textfields. This will not be used in the actual
    # application
    def register(self):
        if self.password.get() != self.confirmPassword.get():
            showwarning("ERROR","Your passwords do not match.\nPlease retype and try again.")
        elif self.userType.get() == "--":
            showwarning("ERROR","Please select an account type.")
        else:
            go = 0
            db = pymysql.connect(host = "academic-mysql.cc.gatech.edu" , passwd = "a1Rlxylj" , user ="cs4400_Group36", db='cs4400_Group36')
            c = db.cursor()
            query = "SELECT COUNT(*) FROM user WHERE username = %s"
            c.execute(query, self.username.get())
            items = c.fetchall()
            if items[0][0] > 0:
                showwarning("ERROR","That username is already taken!\nPlease select a different username\nand try again.")
            else:
                query1 = "INSERT INTO user (username, password) VALUES (%s, %s)"
                query2 = ""
                if self.userType.get() == "Instructor":
                    query2 = "INSERT INTO instructor (username) VALUES (%s)"
                    counts = [0,1,0]
                elif self.userType.get() == "Student":
                    query2 = "INSERT INTO student (username) VALUES (%s)"
                    counts = [1,0,0]
                c.execute(query1, (self.username.get(), self.password.get()))
                if query2 != "":
                    c.execute(query2, self.username.get())
                go = 1
            c.close()
            db.commit()
            db.close()
            if go == 1:
                showinfo("Success","Registration successful.")
                self.root.destroy()
                self.Driver.launch_homepage(counts, self.username.get())


    def cancel(self):
        self.root.destroy()
        self.Driver.return_login()

if __name__=="__main__":
    app = CreateAccount()
