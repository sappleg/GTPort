# Figure 15 Tutor Logbook

from tkinter import *
import pymysql
import datetime
from tkinter.messagebox import showinfo
from tkinter.messagebox import showwarning

class TutorLogbook:
    def __init__(self, driver, un):
        self.Driver = driver
        self.un = un
        self.root = Tk()
        self.root.title('Tutor Logbook')

        self.course = StringVar()
        self.course.set("--")
        self.studentID = StringVar()
        self.studentName = StringVar()

        self.makeWindow()
        self.populate()
        self.root.mainloop()

    def makeWindow(self):
        var1 = datetime.datetime.today()
        self.label = Label(self.root, text = str(var1))
        self.label.grid(row=0, column = 1, columnspan = 2, sticky = E)

        self.label1 = Label(self.root, text = 'Tutor Name:')
        self.label1.grid(row=1, column=0, sticky=W)

        self.label2 = Label(self.root, text = 'NAME')
        self.label2.grid(row=1, column=1, sticky=W)

        self.label3 = Label(self.root, text = 'Course Code:')
        self.label3.grid(row=2, column=0, sticky=W)
        
        self.tutorCourses = ["--"]
        self.courseOptions = OptionMenu(self.root, self.course, *self.tutorCourses)
        self.courseOptions.grid(row = 2, column = 1, sticky = W)

        self.label4 = Label(self.root, text = 'Student ID:')
        self.label4.grid(row=3, column=0, sticky=W)

        self.entry1 = Entry(self.root, textvariable=self.studentID)
        self.entry1.grid(row=3, column = 1)

        self.popButton = Button(self.root, text="Auto-Populate", command=self.popName)
        self.popButton.grid(row=3, column=2)
        
        self.label5 = Label(self.root, text = 'Student Name: ')
        self.label5.grid(row=4, column=0, sticky=W)

        self.entry2 = Entry(self.root, textvariable=self.studentName)
        self.entry2.grid(row=4, column = 1)
        self.entry2.config(state="readonly")

        self.button1 = Button(self.root, text='Submit', command=self.submit)
        self.button1.grid(row=5, column=2, sticky=E)

    def populate(self):
        db = pymysql.connect(host = "academic-mysql.cc.gatech.edu" , passwd = "a1Rlxylj" , user ="cs4400_Group36",
                             db='cs4400_Group36')
        c = db.cursor()
        query = "SELECT name FROM student WHERE username = %s"
        c.execute(query, self.un)
        items = c.fetchall()
        self.label2.config(text=str(items[0][0]))
        self.courseOptions.grid_forget()
        query = "SELECT C.courseCode FROM tutorsFor T, courseSection C WHERE T.courseTitle = C.courseTitle AND T.tutorUsername = %s GROUP BY C.courseTitle"
        c.execute(query, self.un)
        items = c.fetchall()
        self.tutorCourses = ["--"]
        for i in items:
            self.tutorCourses += [i[0]]
        self.courseOptions = OptionMenu(self.root, self.course, *self.tutorCourses)
        self.courseOptions.grid(row = 2, column = 1, sticky = W)
        c.close()
        db.commit()
        db.close()

    def popName(self):
        db = pymysql.connect(host = "academic-mysql.cc.gatech.edu" , passwd = "a1Rlxylj" , user ="cs4400_Group36",
                             db='cs4400_Group36')
        c = db.cursor()
        query = "SELECT name, username FROM student WHERE studentID = %s"
        c.execute(query, self.studentID.get())
        self.items = c.fetchall()
        if len(self.items) == 0:
            showwarning("ERROR","Student does not exist.\nPlease check student ID.")
            self.studentName.set("")
        else:
            self.studentName.set(self.items[0][0])
        c.close()
        db.commit()
        db.close()

    def submit(self):
        db = pymysql.connect(host = "academic-mysql.cc.gatech.edu" , passwd = "a1Rlxylj" , user ="cs4400_Group36",
                             db='cs4400_Group36')
        c = db.cursor()
        query = "INSERT INTO tutorLog (tutorUsername, studentUsername, courseTitle) VALUES (%s, %s, (SELECT courseTitle FROM courseSection WHERE courseCode = %s GROUP BY courseTitle))"
        c.execute(query, (self.un,self.items[0][1],self.course.get()))
        c.close()
        db.commit()
        db.close()

        self.returnHome()

    def returnHome(self):
        showinfo("Success","Logbook entry successfully added.")
        self.root.destroy()
        self.Driver.launch_homepage([1,0,0],self.un)
        

if __name__=='__main__':
    app = TutorLogbook()
