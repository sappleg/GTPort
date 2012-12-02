#!/usr/bin/python3.2
'''
Created on Nov 12, 2012

@author: spencer
'''
from tkinter import *
from tkinter.messagebox import showwarning
import pymysql
import datetime

# This is a class called Login. We will be able to use this class to create
# several instances of this view. Therefore we could have several users
# accessing our application at once (prob not necessary for this project)
# but it will help with code flow as well
class FacultyPI:

    # This is the constructor of the login view. Here I create the Tk object,
    # username and password variables (specific to each instance of Login). I also
    # construct the view and run it through the computer's clock cycles (makeWindow
    # and mainloop)
    def __init__(self, un):
        self.root = Tk()
        self.root.title('Personal Information')

        self.name = StringVar()
        self.dob = StringVar()
        self.gender = StringVar(value="--")
        self.address = StringVar()
        self.permAddress = StringVar()
        self.contactNumber = StringVar()
        self.email = StringVar()
        self.researchInterests = StringVar()
        
        self.department = StringVar(value="--")
        self.position = StringVar(value="--")
        self.course = StringVar(value="--")
        self.section = StringVar(value="--")

        self.populate(un)
        self.makeWindow()
 #       self.getCourses()
        self.root.mainloop()

    def populate(self, un):
        self.db = pymysql.connect(host = "academic-mysql.cc.gatech.edu" , passwd = "a1Rlxylj" , user ="cs4400_Group36",
                             db='cs4400_Group36')
        c = self.db.cursor()
        SQL = "SELECT * FROM instructor WHERE username = %s"
        c.execute(SQL, un)
        items = c.fetchall()
        self.name.set(items[0][4])
        self.dob.set(items[0][6])
        self.address.set(items[0][3])
        self.permAddress.set(items[0][7])
        self.contactNumber.set(items[0][9])
        self.email.set(items[0][5])
        self.position.set(items[0][2])
        if items[0][8] == "M":
            self.gender.set("Male")
        elif items[0][8] == "F":
            self.gender.set("Female")
        query = "SELECT name FROM department D, instrDept I WHERE I.instructorUsername = %s AND D.deptID = I.deptID"
        c.execute(query, un)
        items = c.fetchall()
        self.department.set(items[0][0])
        query = "SELECT S.letter, C.courseCode FROM section S, courseSection C, teaches T WHERE T.instructorUsername = %s AND C.sectionCRN = T.sectionCRN AND C.sectionCRN = S.crn"
        c.execute(query, un)
        items = c.fetchall()
        self.course.set(items[0][1])
        self.section.set(items[0][0])
        query = "SELECT research FROM researchInterests WHERE instructorUsername = %s"
        c.execute(query, un)
        items = c.fetchall()
        string = ""
        for i in range(len(items)):
            string += items[i][0]
            if i != (len(items)-1):
                string += ", "
        self.researchInterests.set(string)
        c.close()
        self.db.close()
        

    # This method is used to construct the actual view. Names of variables
    # should be intuitive. Three frames are used to control the layout of the
    # view using Tk's 'pack' method.
    def makeWindow(self):

        nameFrame = Frame(self.root)
        nameFrame.pack(padx=10)

        nameLabel = Label(nameFrame, text="Name ")
        nameLabel.pack(side=LEFT)

        nameEntry = Entry(nameFrame, textvariable = self.name)
        nameEntry.pack(side=LEFT, padx=10)

        dobFrame = Frame(self.root)
        dobFrame.pack(padx=10)

        dobLabel = Label(dobFrame, text="Date of Birth ")
        dobLabel.pack(side=LEFT)

        dobEntry = Entry(dobFrame, textvariable = self.dob)
        dobEntry.pack(side=LEFT, padx=10)

        genderFrame = Frame(self.root)
        genderFrame.pack(padx=15)

        genderLabel = Label(genderFrame, text="Gender ")
        genderLabel.pack(side=LEFT)

        genderOptionMenu = OptionMenu(genderFrame, self.gender, "--", "Male", "Female")
        genderOptionMenu.pack(side=LEFT)

        addressFrame = Frame(self.root)
        addressFrame.pack(padx=10)

        addressLabel = Label(addressFrame, text="Address ")
        addressLabel.pack(side=LEFT)

        addressEntry = Entry(addressFrame, textvariable = self.address)
        addressEntry.pack(side=LEFT, padx=10)

        permAddressFrame = Frame(self.root)
        permAddressFrame.pack(padx=10)

        permAddressLabel = Label(permAddressFrame, text="Permanent Address ")
        permAddressLabel.pack(side=LEFT)

        permAddressEntry = Entry(permAddressFrame, textvariable = self.permAddress)
        permAddressEntry.pack(side=LEFT, padx=10)

        contactFrame = Frame(self.root)
        contactFrame.pack(padx=10)

        contactLabel = Label(contactFrame, text="Contact ")
        contactLabel.pack(side=LEFT)

        contactEntry = Entry(contactFrame, textvariable = self.contactNumber)
        contactEntry.pack(side=LEFT, padx=10)

        emailFrame = Frame(self.root)
        emailFrame.pack(padx=10)

        emailLabel = Label(emailFrame, text="Email Address ")
        emailLabel.pack(side=LEFT)

        emailEntry = Entry(emailFrame, textvariable = self.email)
        emailEntry.pack(side=LEFT, padx=10)
        
        deptFrame = Frame(self.root)
        deptFrame.pack(padx=10)
        
        deptLabel = Label(deptFrame, text="Department ")
        deptLabel.pack(side=LEFT)

        deptOptionMenu = OptionMenu(deptFrame, self.department, "--", "Aerospace Engineering",
                                    "Biology", "Biomedical Engineering", "Computer Science",
                                    "Electrical & Computer Engineering")
        deptOptionMenu.pack(side=LEFT)
        
        posFrame = Frame(self.root)
        posFrame.pack(padx=10)
        
        posLabel = Label(posFrame, text="Position")
        posLabel.pack(side=LEFT)
        
        posOptionMenu = OptionMenu(posFrame, self.position, "--", "Professor", "Associate Professor",
                                   "Assistant Professor")
        posOptionMenu.pack(side=LEFT)
        
        courseFrame = Frame(self.root)
        courseFrame.pack(padx=10)
        
        courseLabel = Label(courseFrame, text="Course")
        courseLabel.pack(side=LEFT)
        
        courseOptionMenu = OptionMenu(courseFrame, self.course, "--")
        courseOptionMenu.pack(side=LEFT)
        
        sectionFrame = Frame(self.root)
        sectionFrame.pack(padx=10)
        
        sectionLabel = Label(sectionFrame, text="Section")
        sectionLabel.pack(side=LEFT)
        
        sectionOptionMenu = OptionMenu(sectionFrame, self.section, "--")
        sectionOptionMenu.pack(side=LEFT)
        
        RIFrame = Frame(self.root)
        RIFrame.pack(padx=10)
        
        RILabel = Label(RIFrame, text="Research Interests")
        RILabel.pack(side=LEFT)
        
        RIEntry = Entry(RIFrame, width = 100, textvariable = self.researchInterests)
        RIEntry.pack(side=LEFT)    

        buttonFrame = Frame(self.root)
        buttonFrame.pack(fill=X)

        submitButton = Button(buttonFrame, text="Submit", command=self.print_this)
        submitButton.pack(side=RIGHT)

##    def getCourses(self):
##        if self.department.get() != "--":
##            return
##        else:
##            showwarning("ERROR", "Please select a valid department")

    # This method is just a place holder to print out the username and password
    # values gathered from the textfields. This will not be used in the actual
    # application
    def print_this(self):
        print(self.department.get())

# This is the main method of the Login file to be used for debuggin purposes.
# This method is used to create an instance of the Login class.
if __name__=='__main__':
    app = FacultyPI()
