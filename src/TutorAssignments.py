
from tkinter import *
import pymysql

class tutorAssignments:
    def __init__ (self, root):
        self.root = root
        
#Labels at the top        
        self.label1 = Label(root, text = "Students:")
        self.label1.grid(row = 4, column = 0, sticky = E)

#Drop down menus
        self.var1 = StringVar()
        self.var1.set("Danielle")
        self.listbox = OptionMenu(root,self.var1, "Danielle Heady", "Jonathan Porter", "Spencer Applegate", "Noland Smith")
        self.listbox.grid(row = 4, column = 1)

#end buttons
        self.button1 = Button(root, text = ">>", width = 3)
        self.button1.grid(row = 4, column = 2, sticky = W)
        self.button2 = Button(root, text = "Done", width = 10, command = self.print_statement)
        self.button2.grid(row = 8, column = 3, sticky = E)

#Listbox
        listbox = Listbox(root).grid(row = 4, column = 3)
        

    def print_statement(self):
        print(self.var1.get())
        print("Hello World")

root = Tk()
root.title("Tutor Assignments")
app = tutorAssignments(root)
root.mainloop()
