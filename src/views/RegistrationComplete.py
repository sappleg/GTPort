
from tkinter import *
import pymysql

class RegistrationComplete:
    def __init__ (self,driver,un,courses):
        self.Driver = driver
        self.username = un
        self.courses = courses

        self.root = Tk()
        self.root.title('Registration Complete')

        self.makeWindow()
        self.root.mainloop()

    def makeWindow(self):
        label1 = Label(self.root, text = "You have registered for the following courses:")
        label1.grid(row = 0, column = 0, sticky = W, columnspan = 2)

        self.populate()

    def homepage(self):
        self.root.destroy()
        self.Driver.launch_homepage([1,0,0],self.username)

    def populate(self):
        label2 = Label(self.root, text = "Course Code")
        label2.grid(row = 1, column = 0)
        label3 = Label(self.root, text = "Title")
        label3.grid(row = 1, column = 1)
        label4 = Label(self.root, text = "Section")
        label4.grid(row = 1, column = 2)
        label5 = Label(self.root, text = "Mode of Grading")
        label5.grid(row = 1, column = 3)

        db = pymysql.connect(host = "academic-mysql.cc.gatech.edu" , passwd = "a1Rlxylj", user = "cs4400_Group36", db='cs4400_Group36')
        c = db.cursor()
        count = 2
        for course in self.courses:
            if course:
                query = """SELECT courseTitle, courseCode FROM courseSection WHERE
                sectionCRN=%s"""
                c.execute(query, (course[0]))
                items = c.fetchall()
                course_title = items[0][0]
                course_code = items[0][1]
                query = """SELECT letter FROM section WHERE crn=%s"""
                c.execute(query, (course[0]))
                letter = c.fetchall()[0][0]
                grade_mode = ""
                if course[1] == "A":
                    grade_mode = "Audit"
                elif course[1] == "R":
                    grade_mode = "Registered"
                elif course[1] == "P":
                    grade_mode = "Pass/Fail"

                Label(self.root, text = course_code).grid(row=count,column=0)
                Label(self.root, text = course_title).grid(row=count,column=1)
                Label(self.root, text = letter).grid(row=count,column=2)
                Label(self.root, text = grade_mode).grid(row=count,column=3)

                count += 1

        button1 = Button(self.root, text = "Go To Homepage", width = 20, command=self.homepage)
        button1.grid(row = count, column = 3)

        c.close()
        db.close()

if __name__=='__main__':
    app = RegistrationComplete()
