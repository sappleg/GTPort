# Figure 16 Tutor Logbook

from tkinter import *
import pymysql

class AdminReport:
    def __init__(self):
 #       self.Driver = driver

        self.root = Tk()
        self.root.title("Administrative Report")

        self.dept = StringVar()
        self.dept.set("--")

        self.makeWindow()
        self.root.mainloop()

    def makeWindow(self):
        self.deptList = ["--", "Aerospace Engineering","Biology", "Biomedical Engineering", "Computer Science","Electrical & Computer Engineering"]
        self.options = OptionMenu(self.root, self.dept, *self.deptList, command=self.populate)
        self.options.grid(row=0, columnspan=3)
        
        self.label1 = Label(self.root, text = 'Course Code')
        self.label1.grid(row=1, column=0, sticky=W)

        self.label2 = Label(self.root, text = 'Course Name')
        self.label2.grid(row=1, column=1, sticky=W)

        self.label3 = Label(self.root, text = 'Average Grade')
        self.label3.grid(row=1, column=2, sticky=W)

        self.link1 = Button(self.root, text = 'Go To Homepage')
        self.link1.grid(row=3, column=1, columnspan=2, sticky=E)

        self.bodyFrame = Frame(self.root)
        self.bodyFrame.grid(row=2,columnspan=3,sticky=EW)

    def populate(self, dept):
        if self.dept.get() != "--":
            db = pymysql.connect(host = "academic-mysql.cc.gatech.edu" , passwd = "a1Rlxylj" , user ="cs4400_Group36",
                             db='cs4400_Group36')
            c = db.cursor()
            query = "SELECT C.courseCode, C.courseTitle FROM coursesOffered C, department D WHERE C.deptID = D.deptID AND D.name = %s"
            c.execute(query, dept)
            items = c.fetchall()
            itemList = []
            for i in items:
                itemList += [i]
            for course in itemList:
                query = "SELECT courseCode, courseTitle FROM courseSection WHERE courseTitle = %s"
                c.execute(query, course[1])
                items = c.fetchall()
                for i in items:
                    itemList += [i]
            for i in itemList:
                print(i)
            c.close()
            db.close()
        else:
            showwarning("ERROR", "Please select a valid department.")
        




if __name__=="__main__":
    app = AdminReport()
