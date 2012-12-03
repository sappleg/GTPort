# Figure 15 Tutor Logbook

from tkinter import *
import pymysql
import datetime

class TutorLogbook:
    def __init__(self):
        self.win = Tk()
        self.win.title('Tutor Logbook')

        self.course = StringVar()
        self.course.set("--")

        self.makeWindow()
        self.win.mainloop()

    def makeWindow(self):
        var1 = datetime.datetime.today()
        self.label = Label(self.win, text = str(var1))
        self.label.grid(row=0, column = 1, columnspan = 2, sticky = E)

        self.label1 = Label(self.win, text = 'Tutor Name:')
        self.label1.grid(row=1, column=0, sticky=W)

        self.label2 = Label(self.win, text = 'NAME')
        self.label2.grid(row=1, column=1, sticky=W)

        self.label3 = Label(self.win, text = 'Course Code:')
        self.label3.grid(row=2, column=0, sticky=W)
        
        self.depts = ["--", "CS4400"]
        self.deptOptions = OptionMenu(self.win, self.course, *self.depts)
        self.deptOptions.grid(row = 2, column = 1, sticky = W)


        self.label4 = Label(self.win, text = 'Student ID:')
        self.label4.grid(row=3, column=0, sticky=W)

        self.entry1 = Entry(self.win)
        self.entry1.grid(row=3, column = 1)
        
        self.label5 = Label(self.win, text = 'Student Name')
        self.label5.grid(row=4, column=0, sticky=W)

        self.entry2 = Entry(self.win)
        self.entry2.grid(row=4, column = 1)

        self.button1 = Button(self.win, text='Submit')#command=self.blah
        self.button1.grid(row=5, column=2)
        

if __name__=='__main__':
    app = TutorLogbook()
