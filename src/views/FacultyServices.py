from tkinter import *
import pymysql
from tkinter.messagebox import showinfo

class FacultyServices:
    def __init__ (self, driver):
        self.Driver = driver

        self.root = Tk()
        self.root.title('Faculty Services')

        self.makeWindow()
        self.root.mainloop()

    def makeWindow(self):
        button1 = Button(self.root, text = "Assign Grades", width = 25, command = self.assign_grades)
        button1.grid(row = 0, column = 0)
        button1 = Button(self.root, text = "Update Personal Information", width = 25, command = self.update_PI)
        button1.grid(row = 1, column = 0)
        button1 = Button(self.root, text = "Assign Tutors", width = 25, command = self.assign_tutors)
        button1.grid(row = 2, column = 0)
        button1 = Button(self.root, text = "View Student Performance", width = 25, command = self.view_performance)
        button1.grid(row = 3, column = 0)

    def assign_grades(self):
        showinfo("ERROR","This set is not part of the required\nfunctionalities for Phase III.\nPlease make a different selection.")

    def update_PI(self):
        self.root.destroy()
        self.Driver.launch_homepage_next(0,"instructor")

    def assign_tutors(self):
        self.root.destroy()
        self.Driver.assign_tutors()

    def view_performance(self):
        self.root.destroy()
        self.Driver.view_student_performance()

if __name__=='__main__':
    app = facultyServices()

