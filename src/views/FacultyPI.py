#!/usr/bin/python3.2
'''
Created on Nov 12, 2012

@author: spencer
'''
from tkinter import *

# This is a class called Login. We will be able to use this class to create
# several instances of this view. Therefore we could have several users
# accessing our application at once (prob not necessary for this project)
# but it will help with code flow as well
class FacultyPI:

    # This is the constructor of the login view. Here I create the Tk object,
    # username and password variables (specific to each instance of Login). I also
    # construct the view and run it through the computer's clock cycles (makeWindow
    # and mainloop)
    def __init__(self):
        self.root = Tk()
        self.root.title('Personal Information')

        self.name = StringVar()
        self.dob = StringVar()
        self.gender = StringVar(value="Male")
        self.address = StringVar()
        self.permAddress = StringVar()
        self.contactNumber = StringVar()
        self.email = StringVar()
        
        self.department = StringVar(value="Computer Science")
        self.position = StringVar(value="Professor")
        self.course = StringVar(value="CS 7689")
        self.section = StringVar(value="A")
        self.researchInterests = []
        self.currentResearchInterest = StringVar(value="DatabaseModeling")

        self.makeWindow()
        self.root.mainloop()

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

        genderOptionMenu = OptionMenu(genderFrame, self.gender, "Male", "Female")
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

        deptOptionMenu = OptionMenu(deptFrame, self.department, "AeroSpace Engineering",
                                    "Biology", "Biomedical Engineering", "Computer Science",
                                    "Electrical & Computer Engineering")
        deptOptionMenu.pack(side=LEFT)
        
        posFrame = Frame(self.root)
        posFrame.pack(padx=10)
        
        posLabel = Label(posFrame, text="Position")
        posLabel.pack(side=LEFT)
        
        posOptionMenu = OptionMenu(posFrame, self.position, "Professor", "Associate Professor",
                                   "Assistant Professor")
        posOptionMenu.pack(side=LEFT)
        
        courseFrame = Frame(self.root)
        courseFrame.pack(padx=10)
        
        courseLabel = Label(courseFrame, text="Course")
        courseLabel.pack(side=LEFT)
        
        courseOptionMenu = OptionMenu(courseFrame, self.course, "CS 7689", "CS 4400")
        courseOptionMenu.pack(side=LEFT)
        
        sectionFrame = Frame(self.root)
        sectionFrame.pack(padx=10)
        
        sectionLabel = Label(sectionFrame, text="Section")
        sectionLabel.pack(side=LEFT)
        
        sectionOptionMenu = OptionMenu(sectionFrame, self.section, "A", "B", "C", "D", "E", "F")
        sectionOptionMenu.pack(side=LEFT)
        
        RIFrame = Frame(self.root)
        RIFrame.pack(padx=10)
        
        RILabel = Label(RIFrame, text="Research Interests")
        RILabel.pack(side=LEFT)
        
        RIEntry = Entry(RIFrame, textvariable = self.researchInterests)
        RIEntry.pack(side=LEFT)    

        buttonFrame = Frame(self.root)
        buttonFrame.pack(fill=X)

        submitButton = Button(buttonFrame, text="Submit", command=self.print_this)
        submitButton.pack(side=RIGHT)

    # This method is just a place holder to print out the username and password
    # values gathered from the textfields. This will not be used in the actual
    # application
    def print_this(self):
        print("Hello World")

# This is the main method of the Login file to be used for debuggin purposes.
# This method is used to create an instance of the Login class.
if __name__=='__main__':
    app = FacultyPI()
