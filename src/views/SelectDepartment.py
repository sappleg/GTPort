from tkinter import *
import pymysql

class SelectDepartment:
    def __init__ (self, driver):
        self.Driver = driver
        self.root = Tk()
        self.root.title('Select Department')

        self.dept = StringVar(value="Computer Science")

        self.makeWindow()
        self.root.mainloop()

    def makeWindow(self):

        label1 = Label(self.root, text = "Term:        Fall 2012")
        label1.grid(row = 0, column = 1, sticky = W)
        label2 = Label(self.root, text = "Department")
        label2.grid(row = 1, column = 1, sticky = W)


        listbox = OptionMenu(self.root,self.dept, "Aerospace Engineering", "Biology", "Biomedical Engineering", "Computer Science", "Electrical & Computer Engineering")
        listbox.grid(row = 1, column = 1, sticky = E)

        button1 = Button(self.root, text = "Back", width = 10)
        button1.grid(row = 2, column = 0)
        button2 = Button(self.root, text = "Next", width = 10, command = self.course_selection)
        button2.grid(row = 2, column = 2)

    def course_selection(self):
        self.root.destroy()
        self.Driver.course_selection(self.dept)

if __name__=='__main__':
    app = SelectDepartment()
