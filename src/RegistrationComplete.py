
from tkinter import *
import pymysql

class registrationComplete:
    def __init__ (self):
        self.root = Tk()
        self.root.title('Registration Complete')

        self.makeWindow()
        self.root.mainloop()
        
    def makeWindow(self):
          
        self.label1 = Label(self.root, text = "You have registered for the following courses:")
        self.label1.grid(row = 0, column = 0, sticky = W, columnspan = 2)

        self.label2 = Label(self.root, text = "Course Code")
        self.label2.grid(row = 1, column = 0)
        self.label3 = Label(self.root, text = "Title")
        self.label3.grid(row = 1, column = 1)
        self.label4 = Label(self.root, text = "Section")
        self.label4.grid(row = 1, column = 2)
        self.label5 = Label(self.root, text = "Mode of Grading")
        self.label5.grid(row = 1, column = 3)

        self.label6 = Label(self.root, text = "CS 4400")
        self.label6.grid(row = 2, column = 0)
        self.label7 = Label(self.root, text = "Introduction to DB")
        self.label7.grid(row = 2, column = 1)
        self.label8 = Label(self.root, text = "A")
        self.label8.grid(row = 2, column = 2)
        self.label9 = Label(self.root, text = "Registered")
        self.label9.grid(row = 2, column = 3)       

        self.button1 = Button(self.root, text = "Go To Homepage", width = 20)
        self.button1.grid(row = 4, column = 3)
 

    def print_statement(self):
        print(self.var1.get())
        print("Hello World")

if __name__=='__main__':
    app = registrationComplete()

