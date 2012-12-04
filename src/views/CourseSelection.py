from tkinter import *
from tkinter.messagebox import showwarning
import pymysql

class CourseSelection:
    def __init__ (self, driver, un, dept):
        self.Driver = driver
        self.username = un

        self.root = Tk()
        self.root.title('Course Selection')

        self.department = StringVar(value=dept.get())

        self.makeWindow()
        self.root.mainloop()

    def makeWindow(self):
        #Labels at the top
        label1 = Label(self.root, text = "Term:")
        label1.grid(row = 0, column = 0, sticky = W)
        label22 = Label(self.root, text = "Fall 2012")
        label22.grid(row = 0, column = 1, sticky = W)
        label2 = Label(self.root, text = "Department:")
        label2.grid(row = 1, column = 0, sticky = W)
        label14 = Label(self.root, textvariable=self.department)
        label14.grid(row = 1, column = 1, sticky = W)

        #Title row
        label3 = Label(self.root, text = "Section")
        label3.grid(row = 2, column = 0)
        label4 = Label(self.root, text = "CRN")
        label4.grid(row = 2, column = 1)
        label5 = Label(self.root, text = "Title")
        label5.grid(row = 2, column = 2)
        label6 = Label(self.root, text = "Course Code")
        label6.grid(row = 2, column = 3)
        label7 = Label(self.root, text = "Section")
        label7.grid(row = 2, column = 4)
        label8 = Label(self.root, text = "Instructor")
        label8.grid(row = 2, column = 5)
        label9 = Label(self.root, text = "Days")
        label9.grid(row = 2, column = 6)
        label10 = Label(self.root, text = "Time")
        label10.grid(row = 2, column = 7)
        label11 = Label(self.root, text = "Location")
        label11.grid(row = 2, column = 8)
        label12 = Label(self.root, text = "Mode of Grading")
        label12.grid(row = 2, column = 9)

        #populate
        self.populate()

    def populate(self):
        db = pymysql.connect(host = "academic-mysql.cc.gatech.edu" , passwd = "a1Rlxylj", user = "cs4400_Group36", db='cs4400_Group36')
        c = db.cursor()
        query = "SELECT D.deptID FROM student S, department D WHERE S.username=%s AND D.name=%s"
        c.execute(query, (self.username,self.department.get()))
        deptID = c.fetchall()[0][0]
        c.close()
        db.close()

        db2 = pymysql.connect(host = "academic-mysql.cc.gatech.edu" , passwd = "a1Rlxylj", user = "cs4400_Group36", db='cs4400_Group36')
        c = db2.cursor()
        query = "SELECT S.sectionCRN, O.courseTitle, O.courseCode, SE.letter, I.name, SE.classday, SE.classtime, SE.location FROM coursesOffered O, courseSection S, teaches T, instructor I, section SE WHERE O.courseTitle = S.courseTitle AND O.courseCode = S.courseCode AND S.sectionCRN = T.sectionCRN AND T.instructorUsername = I.username AND S.sectionCRN = SE.crn AND O.deptID = %s"
        c.execute(query, (deptID))
        items = c.fetchall()
        c.close()
        db2.close()

        count = 0
        self.courses = []
        for i in range(len(items)):
            row = []

            tmp1 = IntVar(value=0)
            row.append(tmp1)
            Checkbutton(self.root, variable=tmp1).grid(row = i+3, column =0)

            tmp2 = StringVar(value=items[i][0])
            row.append(tmp2)
            Label(self.root, textvariable = tmp2).grid(row = i+3, column = 1)

            Label(self.root, text = items[i][1]).grid(row = i+3, column = 2)
            Label(self.root, text = items[i][2]).grid(row = i+3, column = 3)
            Label(self.root, text = items[i][3]).grid(row = i+3, column = 4)
            Label(self.root, text = items[i][4]).grid(row = i+3, column = 5)
            Label(self.root, text = items[i][5]).grid(row = i+3, column = 6)
            Label(self.root, text = items[i][6]).grid(row = i+3, column = 7)
            Label(self.root, text = items[i][7]).grid(row = i+3, column = 8)

            tmp3 = StringVar(value="Audit")
            row.append(tmp3)
            OptionMenu(self.root, tmp3, "Audit", "Pass/Fail","Registered").grid(row = i+3, column = 9)

            self.courses.append(row)
            count += 1

        #end buttons
        button1 = Button(self.root, text = "Back", width = 10, command=self.back)
        button1.grid(row = count+6, column = 0, sticky = W)
        button2 = Button(self.root, text = "Register", width = 10, command=self.register)
        button2.grid(row = count+6, column = 9, sticky = E)

    def back(self):
        self.root.destroy()
        self.Driver.launch_homepage_next(1,"student")

    def register(self):
        register = []
        for i in range(len(self.courses)):
            row = []
            if self.courses[i][0].get() == 1:
                row.append(self.courses[i][1].get())
                grade_mode = self.courses[i][2].get()
                if (grade_mode == "Registered"):
                    row.append("R")
                elif (grade_mode == "Pass/Fail"):
                    row.append("P")
                elif (grade_mode == "Audit"):
                    row.append("A")
            register.append(row)

        count = 0
        db3 = pymysql.connect(host = "academic-mysql.cc.gatech.edu" , passwd = "a1Rlxylj", user = "cs4400_Group36", db='cs4400_Group36')
        c = db3.cursor()
        for i in range(len(register)):
            if register[i]:
                query = "SELECT count( *) FROM registers WHERE studentUsername=%s AND sectionCRN=%s"
                c.execute(query, (self.username,register[i][0]))
                counts = c.fetchall()[0][0]
                if counts == 1:
                    showwarning("ERROR","You've already registered for course "+register[i][0])
                    return
                else:
                    query = "INSERT INTO registers(studentUsername, sectionCRN, gradeMode) VALUES(%s,%s,%s)"
                    c.execute(query, (self.username, register[i][0], register[i][1]))
            else:
                count += 1
        if count == len(register):
            return

        c.close()
        db3.close()

        self.root.destroy()
        self.Driver.registration_complete(self.username)

if __name__=='__main__':
    app = courseSelection()
