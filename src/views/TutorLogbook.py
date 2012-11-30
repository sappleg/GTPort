# Figure 15 Tutor Logbook

from tkinter import *

class FindTutors:
    def __init__(self, win):

        self.win = win
        self.frame = Frame(win)
        self.frame.grid()

        self.makeWindow()

    def makeWindow(self):
        self.label1 = Label(self.win, text = 'Tutor Name:')
        self.label1.grid(row=0, column=0, sticky=W)

        self.label2 = Label(self.win, text = 'NAME')
        self.label2.grid(row=0, column=1, sticky=W)

        self.label3 = Label(self.win, text = 'Course Code:')
        self.label3.grid(row=1, column=0, sticky=W)




        self.label4 = Label(self.win, text = 'Student ID:')
        self.label4.grid(row=2, column=0, sticky=W)

        self.entry1 = Entry(self.win)
        self.entry1.grid(row=2, column = 1)
        
        self.label5 = Label(self.win, text = 'Student Name')
        self.label5.grid(row=3, column=0, sticky=W)

        self.entry2 = Entry(self.win)
        self.entry2.grid(row=3, column = 1)

        self.button1 = Button(self.win, text='Submit')#command=self.blah
        self.button1.grid(row=4, column=2)
        



root = Tk()
root.title('Tutor Logbook')
app = FindTutors(root)
root.mainloop()
