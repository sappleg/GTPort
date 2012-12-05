# Figure 14 Find Tutors

from tkinter import *
import pymysql
from tkinter.messagebox import showwarning

class FindTutors:
    def __init__(self, driver, un):
        self.Driver = driver
        self.un = un
        
        self.root = Tk()
        self.root.title('Find Tutors')

        self.course = StringVar()
        self.course.set("")

        self.keyword = StringVar()
        self.course.set("")

        self.makeWindow()
        self.root.mainloop()

    def makeWindow(self):
        
        FindTutors = Label(self.root, text = 'FIND TUTORS')
        FindTutors.grid(row=0, column=0)

        self.label1 = Label(self.root, text = 'Course Code:')
        self.label1.grid(row=0, column=0, sticky=W)
        
        self.entry1 = Entry(self.root, textvariable = self.course)
        self.entry1.grid(row=0, column=1, sticky=W)
        
        self.label2 = Label(self.root, text='OR Keyword')
        self.label2.grid(row=0, column=2, sticky=W)

        self.entry2 = Entry(self.root, textvariable = self.keyword)
        self.entry2.grid(row=0, column=3, sticky=W)

        self.B1 = Button(self.root, text='Search', command = self.search)
        self.B1.grid(row=0, column=4)

        self.label3 = Label(self.root, text='Course Code')
        self.label3.grid(row=1, column=0)

        self.Label4 = Label(self.root, text='Course Name')
        self.Label4.grid(row=1, column=1, columnspan=2)

        self.label5 = Label(self.root, text='Tutor Name')
        self.label5.grid(row=1, column=3)

        self.label6 = Label(self.root, text='Tutor Email Address')
        self.label6.grid(row=1, column=4)

        self.frame = Frame(self.root)
        self.frame.grid(row = 2, columnspan = 5)
        
        self.homebutton = Button(self.root, text = 'Go to Homepage', command = self.returnHome)
        self.homebutton.grid(row = 3, columnspan = 5, sticky = E)

    def search(self):
        searchItem = None
        tutorList = []
        if len(self.course.get()) > 0 and len(self.keyword.get()) > 0:
            showwarning("ERROR","Please only enter one search criteria.")
            return
        elif len(self.course.get()) > 0 and len(self.keyword.get()) == 0:
            searchItem = self.course.get()
            db = pymysql.connect(host = "academic-mysql.cc.gatech.edu" , passwd = "a1Rlxylj" , user ="cs4400_Group36",
                             db='cs4400_Group36')
            c = db.cursor()
            query = "SELECT C.courseCode, C.courseTitle, S.name, S.email FROM courseSection C, tutorsFor T, student S WHERE C.courseTitle = T.courseTitle AND T.tutorUsername = S.username AND C.courseCode LIKE '%" + searchItem + "%' GROUP BY T.courseTitle"
            c.execute(query)
            items = c.fetchall()
            for i in items:
                tutorList += [[i[0],i[1],i[2],i[3]]]
            c.close()
            db.commit()
            db.close()
        elif len(self.course.get()) == 0 and len(self.keyword.get()) > 0:
            searchItem = self.keyword.get()
            db = pymysql.connect(host = "academic-mysql.cc.gatech.edu" , passwd = "a1Rlxylj" , user ="cs4400_Group36",
                             db='cs4400_Group36')
            c = db.cursor()
            query = "SELECT C.courseCode, C.courseTitle, S.name, S.email FROM courseSection C, student S, tutorsFor T WHERE S.username = T.tutorUsername AND T.courseTitle = C.courseTitle AND T.courseTitle LIKE '%" + searchItem + "%' GROUP BY T.courseTitle"
            c.execute(query)
            items = c.fetchall()
            for i in items:
                tutorList += [[i[0],i[1],i[2],i[3]]]
            c.close()
            db.commit()
            db.close()
        else:
            showwarning("ERROR","Please enter a valid search.")
            return

        if len(tutorList) > 0:
            self.frame.grid_remove()
            for t in range(len(tutorList)):
                if t > 0 and tutorList[t][0] == tutorList[t-1][0]:
                    Lcode = Label(self.frame, text="")
                else:
                    Lcode = Label(self.frame, text=tutorList[t][0])
                Lcode.grid(row=t,column=0,sticky=W)
                if t > 0 and tutorList[t][1] == tutorList[t-1][1]:
                    Ltitle = Label(self.frame, text="")
                else:
                    Ltitle = Label(self.frame, text=tutorList[t][1])
                Ltitle.grid(row=t,column=1)
                Lhold = Label(self.frame,text="",width=10)
                Lhold.grid(row=t,column=2)
                Lname = Label(self.frame, text=tutorList[t][2])
                Lname.grid(row=t,column=3)
                Lemail = Label(self.frame, text=tutorList[t][3])
                Lemail.grid(row=t,column=4,sticky=E)
            self.frame.grid(row = 2, columnspan = 5)
        else:
            showwarning("ERROR","Sorry, no tutors to display.\nPlease alter your search criteria\nand try again.")
            return

    def returnHome(self):
        self.root.destroy()
        self.Driver.launch_homepage([1,0,0],self.un)

if __name__=='__main__':
    app = FindTutors()       
