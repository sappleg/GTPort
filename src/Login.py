#!/usr/bin/python

from tkinter import *

# This is a class called Login. We will be able to use this class to create
# several instances of this view. Therefore we could have several users
# accessing our application at once (prob not necessary for this project)
# but it will help with code flow as well
class Login:

    # This is the constructor of the login view. Here I create the Tk object,
    # username and password variables (specific to each instance of Login). I also
    # construct the view and run it through the computer's clock cycles (makeWindow
    # and mainloop)
    def __init__(self):
        self.root = Tk()
        self.root.title('GTPort')

        self.username = StringVar()
        self.password = StringVar()

        self.makeWindow()
        self.root.mainloop()

    # This method is used to construct the actual view. Names of variables
    # should be intuitive. Three frames are used to control the layout of the
    # view using Tk's 'pack' method.
    def makeWindow(self):

        usernameFrame = Frame(self.root)
        usernameFrame.pack(padx=15, pady=15)

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

        createAccountButton = Button(buttonFrame, text="Create Account", command=self.print_this)
        createAccountButton.pack(side=RIGHT)

        loginButton = Button(buttonFrame, text="Login", command=self.print_this)
        loginButton.pack(side=RIGHT)

    # This method is just a place holder to print out the username and password
    # values gathered from the textfields. This will not be used in the actual
    # application
    def print_this(self):
        print(self.username.get())
        print(self.password.get())

# This is the main method of the Login file to be used for debuggin purposes.
# This method is used to create an instance of the Login class.
if __name__=='__main__':
    app = Login()
