
from tkinter import *
import pymysql

class TutorAssignments:
    def __init__ (self, driver, un):
        self.Driver = driver
        self.un = un
        
        self.root = Tk()
        self.root.title('Tutor Assignments')

        self.var1 = StringVar()
        self.var1.set("--")

        self.makeWindow()
        self.populate()
        self.root.mainloop()
        

    def makeWindow(self):
#Labels at the top        
        label1 = Label(self.root, text = "Students:")
        label1.grid(row = 4, column = 0, sticky = E)

#Drop down menus
        self.sName = ["--"]
        self.listbox = OptionMenu(self.root,self.var1, *self.sName)
        self.listbox.grid(row = 4, column = 1)

#end buttons
        button1 = Button(self.root, text = ">>", width = 3, command = self.print_statement)
        button1.grid(row = 4, column = 2, sticky = W)
        button2 = Button(self.root, text = "Done", width = 10, command = self.returnHome)
        button2.grid(row = 8, column = 3, sticky = E)

#Listbox
        listbox = Listbox(self.root).grid(row = 4, column = 3)
        

    def populate(self):
        db = pymysql.connect(host = "academic-mysql.cc.gatech.edu" , passwd = "a1Rlxylj" , user ="cs4400_Group36",
                             db='cs4400_Group36')
        c = db.cursor()
        query = "SELECT ST.name FROM student ST, teaches T, courseSection S, appliesForTutor A WHERE T.sectionCRN = S.sectionCRN AND S.courseTitle = A.courseTitle AND A.studentUsername = ST.username AND T.instructorUsername = %s"
        c.execute(query, self.un)
        items = c.fetchall()
        for i in items:
            print(i)
        c.close()
        db.commit()
        db.close()

    def print_statement(self):
        print(self.var1.get())
        print("Hello World")

if __name__=='__main__':
    app = TutorAssignments()

