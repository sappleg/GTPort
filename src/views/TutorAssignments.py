
from tkinter import *
import pymysql

class TutorAssignments:
    def __init__ (self):
        self.root = Tk()
        self.root.title('Tutor Assignments')

        self.var1 = StringVar()
        self.var1.set("Danielle is Pretty")

        self.makeWindow()
        self.root.mainloop()
        

    def makeWindow(self):
#Labels at the top        
        label1 = Label(self.root, text = "Students:")
        label1.grid(row = 4, column = 0, sticky = E)

#Drop down menus
        self.sName = ["--", "Danielle Heady", "Jonathan Porter", "Spencer Applegate", "Noland Smith"]
        self.listbox = OptionMenu(self.root,self.var1, *self.sName)
        self.listbox.grid(row = 4, column = 1)

#end buttons
        button1 = Button(self.root, text = ">>", width = 3)
        button1.grid(row = 4, column = 2, sticky = W)
        button2 = Button(self.root, text = "Done", width = 10, command = self.print_statement)
        button2.grid(row = 8, column = 3, sticky = E)

#Listbox
        listbox = Listbox(self.root).grid(row = 4, column = 3)
        

    def print_statement(self):
        print(self.var1.get())
        print("Hello World")

if __name__=='__main__':
    app = TutorAssignments()

