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
class StudentPI:

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
        self.tutorWilling = IntVar()
        self.tutorCourses = []
        self.tutorCoursesSelected = []
        self.currentTutorCourse = StringVar(value="CS8781")
        self.major = StringVar(value="Aerospace Engineering")
        self.degree = StringVar(value="BS")
        self.previousEduSchool = []
        self.currentPreviousEduSchool = StringVar()
        self.previousEduMajor = []
        self.currentPreviousEduMajor = StringVar()
        self.previousEduDegree = []
        self.currentPreviousEduDegree = StringVar()
        self.previousEduGradYear = []
        self.currentPreviousEduGradYear = StringVar()
        self.previousEduGPA = []
        self.currentPreviousEduGPA = StringVar()

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

        tutorWillingFrame = Frame(self.root)
        tutorWillingFrame.pack(padx=10)

        tutorWillingLabel = Label(tutorWillingFrame, text="Willing to tutor? ")
        tutorWillingLabel.pack(side=LEFT)
        
        yesRadioButton = Radiobutton(tutorWillingFrame, text="Yes", variable=self.tutorWilling,value=1)
        yesRadioButton.pack(side=LEFT)
        
        noRadioButton = Radiobutton(tutorWillingFrame, text="No", variable=self.tutorWilling,value=2)
        noRadioButton.pack(side=LEFT)

        tutorCoursesFrame = Frame(self.root)
        tutorCoursesFrame.pack(padx=15, fill=X)

        tutorCoursesLabel = Label(tutorCoursesFrame, text="If Yes, select the courses you would like to tutor for ")
        tutorCoursesLabel.pack(side=LEFT)

        tutorCoursesOptionMenu = OptionMenu(tutorCoursesFrame, self.currentTutorCourse, "CS8781")
        tutorCoursesOptionMenu.pack(side=LEFT)

        addCourseButton = Button(tutorCoursesFrame, text="+", command=self.print_this)
        addCourseButton.pack(side=LEFT)
        
        tutorCoursesText = Text(tutorCoursesFrame, height=1, width=50, background="white")
        tutorCoursesText.pack(side=LEFT)

        majorFrame = Frame(self.root)
        majorFrame.pack(padx=15)

        majorLabel = Label(majorFrame, text="Major ")
        majorLabel.pack(side=LEFT)

        majorOptionMenu = OptionMenu(majorFrame, self.major, "Aerospace Engineering",
                                            "Biology", "Biomedical Engineering", "Computer Science",
                                            "Electrical & Computer Engineering")
        majorOptionMenu.pack(side=LEFT)

        degreeLabel = Label(majorFrame, text="Degree ")
        degreeLabel.pack(side=LEFT)

        degreeOptionMenu = OptionMenu(majorFrame, self.degree, "BS", "MS", "Ph.D")
        degreeOptionMenu.pack(side=LEFT)

        previousEduLabelFrame = Frame(self.root)
        previousEduLabelFrame.pack(padx=15)
        
        previousEduLabel = Label(previousEduLabelFrame, text="Previous Education ")
        previousEduLabel.pack()

        previousEduFrame = Frame(self.root, borderwidth=1)
        previousEduFrame.pack()
        
        previousEduSchoolNameLabel = Label(previousEduFrame, text="Name of Institution Attended ")
        previousEduSchoolNameLabel.grid(row=0, column=0)

        previousEduSchoolNameEntry = Entry(previousEduFrame, textvariable = self.currentPreviousEduSchool)
        previousEduSchoolNameEntry.grid(row=0, column=1)
        
        previousEduMajorLabel = Label(previousEduFrame, text="Major ")
        previousEduMajorLabel.grid(row=1, column=0)

        previousEduMajorEntry = Entry(previousEduFrame, textvariable = self.currentPreviousEduMajor)
        previousEduMajorEntry.grid(row=1, column=1)
        
        previousEduDegreeLabel = Label(previousEduFrame, text="Degree ")
        previousEduDegreeLabel.grid(row=2, column=0)

        previousEduDegreeEntry = Entry(previousEduFrame, textvariable = self.currentPreviousEduDegree)
        previousEduDegreeEntry.grid(row=2, column=1)
        
        previousEduGradYearLabel = Label(previousEduFrame, text="Year of graduation ")
        previousEduGradYearLabel.grid(row=3, column=0)

        previousEduGradYearEntry = Entry(previousEduFrame, textvariable = self.currentPreviousEduGradYear)
        previousEduGradYearEntry.grid(row=3, column=1)
        
        previousEduGPALabel = Label(previousEduFrame, text="GPA ")
        previousEduGPALabel.grid(row=4, column=0)

        previousEduGPAEntry = Entry(previousEduFrame, textvariable = self.currentPreviousEduGPA)
        previousEduGPAEntry.grid(row=4, column=1)
        
        
        
        
        

        buttonFrame = Frame(self.root)
        buttonFrame.pack(fill=X)

        submitButton = Button(buttonFrame, text="Submit", command=self.print_this)
        submitButton.pack(side=RIGHT)

        addEduButton = Button(buttonFrame, text="Add Education", command=self.print_this)
        addEduButton.pack(side=LEFT)

    # This method is just a place holder to print out the username and password
    # values gathered from the textfields. This will not be used in the actual
    # application
    def print_this(self):
        print("Hello World")

# This is the main method of the Login file to be used for debuggin purposes.
# This method is used to create an instance of the Login class.
if __name__=='__main__':
    app = StudentPI()
