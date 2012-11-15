
from tkinter import *
import pymysql

class selectDepartment:
    def __init__ (self):
        self.root = Tk()
        self.root.title('Select Department')

        self.makeWindow()
        self.root.mainloop()


    def makeWindow(self):
        
        self.label1 = Label(self.root, text = "Term:        Fall 2012")
        self.label1.grid(row = 0, column = 1, sticky = W)
        self.label2 = Label(self.root, text = "Department")
        self.label2.grid(row = 1, column = 1, sticky = W)

        self.var1 = StringVar()
        self.var1.set("Computer Science")
        self.listbox = OptionMenu(self.root,self.var1, "Aerospace Engineering", "Biology", "Biomedical Engineering", "Computer Science", "Electrical and Computer Engineering")
        self.listbox.grid(row = 1, column = 1, sticky = E)

        self.button1 = Button(self.root, text = "Back", width = 10)
        self.button1.grid(row = 2, column = 0)
        self.button2 = Button(self.root, text = "Next", width = 10, command = self.print_statement)
        self.button2.grid(row = 2, column = 2)

    def print_statement(self):
        print(self.var1.get())
        print("Hello World")

if __name__=='__main__':
    app = selectDepartment()


