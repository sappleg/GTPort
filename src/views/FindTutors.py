# Figure 14 Find Tutors

from tkinter import *

class FindTutors:
    def __init__(self):
        self.win = Tk()
        self.win.title('Find Tutors')

        self.course = StringVar()
        self.course.set("")

        self.keyWord = StringVar()
        self.course.set("")

        self.makeWindow()
        self.win.mainloop()

    def makeWindow(self):
        
        FindTutors = Label(self.win, text = 'FIND TUTORS')
        FindTutors.grid(row=0, column=0)

        self.label1 = Label(self.win, text = 'Course Code:')
        self.label1.grid(row=0, column=0, sticky=W)
        
        self.entry1 = Entry(self.win, textvariable = self.course)
        self.entry1.grid(row=0, column=1, sticky=W)
        
        self.label2 = Label(self.win, text='OR Keyword')
        self.label2.grid(row=0, column=2, sticky=W)

        self.entry2 = Entry(self.win, textvariable = self.keyWord)
        self.entry2.grid(row=0, column=3, sticky=W)

        self.B1 = Button(self.win, text='Search')#command = self.blah
        self.B1.grid(row=0, column=4)

        self.label3 = Label(self.win, text='COURSE CODE')
        self.label3.grid(row=1, column=0)

        self.Label4 = Label(self.win, text='COURSE NAME')
        self.Label4.grid(row=1, column=1, columnspan=2)

        self.label5 = Label(self.win, text='TUTOR NAME')
        self.label5.grid(row=1, column=3)

        self.label6 = Label(self.win, text='TUTOR EMAIL ADDRESS')
        self.label6.grid(row=1, column=4)

        self.frame = Frame(self.win)
        self.frame.grid(row = 2, columnspan = 5)
        self.homebutton = Button(self.win, text = 'Go to Homepage', command = self.returnhome)
        self.homebutton.grid(row = 3, columnspan = 5, sticky = E)

    def returnhome(self):
        print('I LOVE YOU')
        

if __name__=='__main__':
    app = FindTutors()       
