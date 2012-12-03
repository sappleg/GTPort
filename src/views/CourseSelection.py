from tkinter import *
import pymysql

class CourseSelection:
    def __init__ (self, driver, un):
        self.Driver = driver
        self.username = un

        self.root = Tk()
        self.root.title('Course Selection')

        self.var3 = StringVar()
        self.var2 = StringVar()
        self.var1 = StringVar()
        self.var3.set("Audit")
        self.var2.set("Audit")
        self.var1.set("Audit")

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
        label14 = Label(self.root, text = "Computer Science")
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
        query = "SELECT D.deptID FROM student S, department D WHERE S.username=%s AND S.major = D.name"
        c.execute(query, (self.username))
        deptID = c.fetchall()[0][0]
        c.close()
        db.close()

        db2 = pymysql.connect(host = "academic-mysql.cc.gatech.edu" , passwd = "a1Rlxylj", user = "cs4400_Group36", db='cs4400_Group36')
        c = db2.cursor()
        #query = "SELECT * FROM coursesOffered WHERE deptID=%s"
        query = "SELECT S.sectionCRN, O.courseTitle, O.courseCode, SE.letter, I.name, SE.classday, SE.classtime, SE.location FROM coursesOffered O, courseSection S, teaches T, instructor I, section SE WHERE O.courseTitle = S.courseTitle AND O.courseCode = S.courseCode AND S.sectionCRN = T.sectionCRN AND T.instructorUsername = I.username AND S.sectionCRN = SE.crn AND O.deptID = %s"
        c.execute(query, (deptID))
        items = c.fetchall()
        c.close()
        db2.close()

        count = 0
        courses = []
        for i in range(len(items)):
            row = []
            row.append(Checkbutton(self.root, variable=IntVar(value=i)).grid(row = i+3, column =0))
            row.append(Label(self.root, textvariable = StringVar(value=items[i][0])).grid(row = i+3, column = 1))
            Label(self.root, text = items[i][1]).grid(row = i+3, column = 2)
            Label(self.root, text = items[i][2]).grid(row = i+3, column = 3)
            Label(self.root, text = items[i][3]).grid(row = i+3, column = 4)
            Label(self.root, text = items[i][4]).grid(row = i+3, column = 5)
            Label(self.root, text = items[i][5]).grid(row = i+3, column = 6)
            Label(self.root, text = items[i][6]).grid(row = i+3, column = 7)
            Label(self.root, text = items[i][7]).grid(row = i+3, column = 8)
            row.append(OptionMenu(self.root, StringVar(value="Audit"), "Audit", "Pass/Fail","Registered").grid(row = i+3, column = 9))
            courses.append(row)
            count += 1

        for i in courses:
            print(i)

        #row1 of data
        #label13 = Label(self.root, text = "88767")
        #label13.grid(row = 3, column = 1)
        #label15 = Label(self.root, text = "Introduction to DB")
        #label15.grid(row = 3, column = 2)
        #label16 = Label(self.root, text = "CS 4400")
        #label16.grid(row = 3, column = 3)
        #label17 = Label(self.root, text = "A")
        #label17.grid(row = 3, column = 4)
        #label18 = Label(self.root, text = "Mark, Leo")
        #label18.grid(row = 3, column = 5)
        #label19 = Label(self.root, text = "MWF")
        #label19.grid(row = 3, column = 6)
        #label20 = Label(self.root, text = "1:00 PM - 2:00 PM")
        #label20.grid(row = 3, column = 7)
        #label21 = Label(self.root, text = "KACB 2443")
        #label21.grid(row = 3, column = 8)

        #check buttons
        #checkbutt = Checkbutton(self.root).grid(row = 3, column = 0)

        #Drop down menus
        #listbox = OptionMenu(self.root, self.var1, "Audit", "Pass/Fail", "Registered")
        #listbox.grid(row = 3, column = 9)

        #end buttons
        button1 = Button(self.root, text = "Back", width = 10)
        button1.grid(row = count+6, column = 0, sticky = W)
        button2 = Button(self.root, text = "Register", width = 10, command = self.print_statement)
        button2.grid(row = count+6, column = 9, sticky = E)

    def print_statement(self):
        print(self.var1.get())
        print("Hello World")

if __name__=='__main__':
    app = courseSelection()
