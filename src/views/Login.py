#!/usr/bin/python3.2
'''
Created on Nov 12, 2012

@author: spencer
'''
from tkinter import *
from tkinter.messagebox import showwarning
from tkinter.messagebox import showinfo
import pymysql

# This is a class called Login. We will be able to use this class to create
# several instances of this view. Therefore we could have several users
# accessing our application at once (prob not necessary for this project)
# but it will help with code flow as well
class Login:

    # This is the constructor of the login view. Here I create the Tk object,
    # username and password variables (specific to each instance of Login). I also
    # construct the view and run it through the computer's clock cycles (makeWindow
    # and mainloop)
    def __init__(self, driver):
        self.Driver = driver

        self.root = Tk()
        self.root.title('GTPort')

        self.username = StringVar()
        self.password = StringVar()

        self.makeWindow()
        self.root.mainloop() #needs to be moved out of constructor

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

        passwordEntry = Entry(passwordFrame, textvariable = self.password)
        passwordEntry.pack(side=LEFT, padx=10)

        buttonFrame = Frame(self.root)
        buttonFrame.pack(fill=X)

        loginButton = Button(buttonFrame, text="Login", command=self.login)
        loginButton.pack(side=RIGHT)

        createAccountButton = Button(buttonFrame, text="Create Account")
        createAccountButton.pack(side=RIGHT)

    def login(self):
        if self.username.get() == "" or self.password.get() == "":
            #print("please enter a valid username and password")
            showwarning("WARNING", "Please enter a valid username and password")
        else:
            self.db = pymysql.connect(host = "academic-mysql.cc.gatech.edu" , passwd = "a1Rlxylj" , user ="cs4400_Group36", db='cs4400_Group36')
            c = self.db.cursor()
            SQL = "SELECT count( *) FROM user WHERE username = %s AND password = %s"
            c.execute(SQL, (self.username.get(), self.password.get()))
            counts = c.fetchall()
            self.handleLogin(counts[0][0])
            c.close()
            self.db.close()

    def handleLogin(self,i):
        if i:
            self.root.destroy()
            self.db2 = pymysql.connect(host = "academic-mysql.cc.gatech.edu" , passwd = "a1Rlxylj" , user ="cs4400_Group36", db='cs4400_Group36')

            c = self.db.cursor()
            SQL = "SELECT count( *) FROM student WHERE username = %s"
            c.execute(SQL, (self.username.get()))
            counts = c.fetchall()
            student_count = counts[0][0]

            SQL = "SELECT count( *) FROM instructor WHERE username = %s"
            c.execute(SQL, (self.username.get()))
            counts = c.fetchall()
            instructor_count = counts[0][0]

            SQL = "SELECT count( *) FROM adminUser WHERE username = %s"
            c.execute(SQL, (self.username.get()))
            counts = c.fetchall()
            admin_count = counts[0][0]

            c.close()
            self.db2.close()

            #Launches homepage in driver
            self.Driver.launch_homepage([student_count, instructor_count,
                admin_count], self)

        else:
            showinfo("", "Login unsuccessful")

    def getUsername(self):
        return self.username.get()

# This is the main method of the Login file to be used for debuggin purposes.
# This method is used to create an instance of the Login class.
if __name__=='__main__':
    app = Login()
