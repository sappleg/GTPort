# Figure 17 Effect of tutoring on Student Performance

from tkinter import *

class FindTutors:
    def __init__(self, win):

        self.win = win
        self.frame = Frame(win)
        self.frame.grid()

        self.makeWindow()

    def makeWindow(self):
        self.label1 = Label(self.win, text = 'Course Code')
        self.label1.grid(row=0, column=0, sticky=W)

        self.label2 = Label(self.win, text = 'Course Name')
        self.label2.grid(row=0, column=1, sticky=W)

        self.label3 = Label(self.win, text = 'No. of Meetings with Tutors')
        self.label3.grid(row=0, column=2, sticky=W)

        self.link1 = Label(self.win, text = 'Average Grade of Students')
        self.link1.grid(row=0, column=3, sticky=W)




root = Tk()
root.title('Effect of Tutoring on Student Performance')
app = FindTutors(root)
root.mainloop()
