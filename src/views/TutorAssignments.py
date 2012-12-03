
from tkinter import *
import pymysql
from tkinter.messagebox import showwarning
from tkinter.messagebox import showinfo

class TutorAssignments:
    def __init__ (self, driver, un):
        self.Driver = driver
        self.un = un
        
        self.root = Tk()
        self.root.title('Tutor Assignments')

        self.approveName = StringVar()
        self.approveName.set("--")
        self.finalList = []
        self.workingList = []

        self.makeWindow()
        self.populate()
        self.root.mainloop()
        

    def makeWindow(self):
#Labels at the top        
        label1 = Label(self.root, text = "Students:")
        label1.grid(row = 4, column = 0, sticky = E)

#Drop down menus
        self.sName = ["--"]
        self.listbox = OptionMenu(self.root,self.approveName, *self.sName)
        self.listbox.grid(row = 4, column = 1)

#end buttons
        button1 = Button(self.root, text = ">>", width = 3, command = self.approval)
        button1.grid(row = 4, column = 2, sticky = W)
        button2 = Button(self.root, text = "Done", width = 10, command = self.finish)
        button2.grid(row = 8, column = 3, sticky = E)

#Listbox
        self.approveList = Listbox(self.root)
        self.approveList.grid(row = 4, column = 3)
        

    def populate(self):
        db = pymysql.connect(host = "academic-mysql.cc.gatech.edu" , passwd = "a1Rlxylj" , user ="cs4400_Group36",
                             db='cs4400_Group36')
        c = db.cursor()
        query = "SELECT ST.name, ST.username, S.courseTitle FROM student ST, teaches T, courseSection S, appliesForTutor A WHERE T.sectionCRN = S.sectionCRN AND S.courseTitle = A.courseTitle AND A.studentUsername = ST.username AND T.instructorUsername = %s"
        c.execute(query, self.un)
        items = c.fetchall()
        self.sName = ["--"]
        self.listbox.grid_forget()
        for i in items:
            self.sName += [i[0]]
            self.workingList += [i]
        self.listbox = OptionMenu(self.root,self.approveName, *self.sName)
        self.listbox.grid(row = 4, column = 1)
        c.close()
        db.commit()
        db.close()

    def approval(self):
        if self.approveName.get() != "--":
            self.finalList += [self.approveName.get()]
            self.approveList.insert(END, self.approveName.get())
            self.listbox.grid_forget()
            self.sName.remove(self.approveName.get())
            self.approveName.set("--")
            self.listbox = OptionMenu(self.root,self.approveName, *self.sName)
            self.listbox.grid(row = 4, column = 1)
        else:
            showwarning("ERROR","Please select a tutor's name.")

    def print_statement(self):
        print(self.var1.get())
        print("Hello World")

    def finish(self):
        db = pymysql.connect(host = "academic-mysql.cc.gatech.edu" , passwd = "a1Rlxylj" , user ="cs4400_Group36",
                             db='cs4400_Group36')
        c = db.cursor()
        queryD = "DELETE FROM appliesForTutor WHERE studentUsername = %s"
        queryI = "INSERT INTO tutorsFor (tutorUsername,courseTitle) VALUES (%s, %s)"
        for name in self.finalList:
            for profile in self.workingList:
                if name == profile[0]:
                    matchUser = profile[1]
                    matchCourse = profile[2]
                    self.workingList.remove(profile)
            c.execute(queryD, matchUser)
            c.execute(queryI, (matchUser, matchCourse))
        c.close()
        db.commit()
        db.close()
        showinfo("Success","Tutors successfully approved")
        self.root.destroy()
        self.Driver.launch_homepage([0,1,0],self.un)

if __name__=='__main__':
    app = TutorAssignments()

