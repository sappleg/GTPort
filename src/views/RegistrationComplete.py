
from tkinter import *
import pymysql

class RegistrationComplete:
    def __init__ (self,driver,un):
        self.Driver = driver
        self.username = un

        self.root = Tk()
        self.root.title('Registration Complete')

        self.makeWindow()
        self.root.mainloop()
        
    def makeWindow(self):
          
        label1 = Label(self.root, text = "You have registered for the following courses:")
        label1.grid(row = 0, column = 0, sticky = W, columnspan = 2)

        label2 = Label(self.root, text = "Course Code")
        label2.grid(row = 1, column = 0)
        label3 = Label(self.root, text = "Title")
        label3.grid(row = 1, column = 1)
        label4 = Label(self.root, text = "Section")
        label4.grid(row = 1, column = 2)
        label5 = Label(self.root, text = "Mode of Grading")
        label5.grid(row = 1, column = 3)

        label6 = Label(self.root, text = "CS 4400")
        label6.grid(row = 2, column = 0)
        label7 = Label(self.root, text = "Introduction to DB")
        label7.grid(row = 2, column = 1)
        label8 = Label(self.root, text = "A")
        label8.grid(row = 2, column = 2)
        label9 = Label(self.root, text = "Registered")
        label9.grid(row = 2, column = 3)       

        button1 = Button(self.root, text = "Go To Homepage", width = 20, command=self.homepage)
        button1.grid(row = 4, column = 3)
 

    def homepage(self):
        self.root.destroy()
        self.Driver.launch_homepage([1,0,0],self.username)

if __name__=='__main__':
    app = RegistrationComplete()
