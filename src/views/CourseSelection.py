
from tkinter import *
import pymysql

class courseSelection:
    def __init__ (self):
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
        label3 = Label(self.root, text = "Secion")
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

#row1 of data
        label13 = Label(self.root, text = "88767")
        label13.grid(row = 3, column = 1)
        label15 = Label(self.root, text = "Introduction to DB")
        label15.grid(row = 3, column = 2)
        label16 = Label(self.root, text = "CS 4400")
        label16.grid(row = 3, column = 3)
        label17 = Label(self.root, text = "A")
        label17.grid(row = 3, column = 4)
        label18 = Label(self.root, text = "Mark, Leo")
        label18.grid(row = 3, column = 5)
        label19 = Label(self.root, text = "MWF")
        label19.grid(row = 3, column = 6)
        label20 = Label(self.root, text = "1:00 PM - 2:00 PM")
        label20.grid(row = 3, column = 7)
        label21 = Label(self.root, text = "KACB 2443")
        label21.grid(row = 3, column = 8)
        
#check buttons
        checkbutt = Checkbutton(self.root).grid(row = 3, column = 0)
        checkbutt2 = Checkbutton(self.root).grid(row = 4, column = 0)
        checkbutt3 = Checkbutton(self.root).grid(row = 5, column = 0)

#Drop down menus
        listbox = OptionMenu(self.root, self.var1, "Audit", "Pass/Fail", "Registered")
        listbox.grid(row = 3, column = 9)


        listbox2 = OptionMenu(self.root, self.var2, "Audit", "Pass/Fail", "Registered")
        listbox2.grid(row = 4, column = 9)


        listbox3 = OptionMenu(self.root, self.var3, "Audit", "Pass/Fail", "Registered")
        listbox3.grid(row = 5, column = 9)

#end buttons
        button1 = Button(self.root, text = "Back", width = 10)
        button1.grid(row = 6, column = 0, sticky = W)
        button2 = Button(self.root, text = "Register", width = 10, command = self.print_statement)
        button2.grid(row = 6, column = 9, sticky = E)

    def print_statement(self):
        print(self.var1.get())
        print("Hello World")

if __name__=='__main__':
    app = courseSelection()
