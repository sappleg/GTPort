#!/usr/bin/python3.2
'''
Created on Nov 12, 2012

@author: porter
'''
from tkinter import *
from tkinter.messagebox import showwarning
from tkinter.messagebox import showinfo
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
    def __init__(self, driver, un):
        self.Driver = driver
        self.root = Tk()
        self.root.title('Personal Information')
        self.un = un

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

        self.makeWindow()
        self.populate()
        self.root.mainloop()

    def populate(self):
        self.db = pymysql.connect(host = "academic-mysql.cc.gatech.edu" , passwd = "a1Rlxylj" , user ="cs4400_Group36",
                             db='cs4400_Group36')
        c = self.db.cursor()
        SQL = "SELECT * FROM instructor WHERE username = %s"
        c.execute(SQL, self.un)
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
        query = "SELECT D.name FROM department D, instrDept I WHERE I.instructorUsername = %s AND D.deptID = I.deptID"
        c.execute(query, self.un)
        items = c.fetchall()
        if items:
            self.department.set(items[0][0])
            query = "SELECT S.letter, C.courseCode FROM section S, courseSection C, teaches T WHERE T.instructorUsername = %s AND C.sectionCRN = T.sectionCRN AND C.sectionCRN = S.crn"
            c.execute(query, self.un)
            items2 = c.fetchall()
            if items2:
                self.course.set(items2[0][1])
                self.section.set(items2[0][0])
                if self.department.get() != "--":
                    query = "SELECT C.courseCode FROM coursesOffered C, department D WHERE C.deptID = D.deptID AND D.name = %s"
                    c.execute(query, self.department.get())
                    items = c.fetchall()
                    self.courseList = ["--"]
                    for i in items:
                        self.courseList += [i[0]]
                    self.courseOptionMenu.pack_forget()
                    self.courseOptionMenu = OptionMenu(self.courseFrame, self.course, *self.courseList, command=self.getSections)
                    self.courseOptionMenu.pack(side=LEFT)
                else:
                    showwarning("ERROR", "Please select a valid department.")

                if self.course.get() != "--":
                    query = "SELECT S.letter FROM section S, courseSection C WHERE S.crn = C.sectionCRN AND C.courseCode = %s"
                    c.execute(query, self.course.get())
                    items = c.fetchall()
                    self.sectionList = ["--"]
                    for i in items:
                        self.sectionList += [i[0]]
                    self.sectionOptionMenu.pack_forget()
                    self.sectionOptionMenu = OptionMenu(self.sectionFrame, self.section, *self.sectionList)
                    self.sectionOptionMenu.pack(side=LEFT)
                else:
                    showwarning("ERROR", "Please select a valid course.")

            else:
                self.course.set("--")
                self.section.set("--")
                self.getCourses(self.department.get())
                #self.getSections(self.c)
        else:
            self.department.set("--")
        query = "SELECT research FROM researchInterests WHERE instructorUsername = %s"
        c.execute(query, self.un)
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

        self.depts = ["--", "Aerospace Engineering","Biology", "Biomedical Engineering", "Computer Science","Electrical & Computer Engineering"]
        self.deptOptionMenu = OptionMenu(deptFrame, self.department, *self.depts, command=self.getCourses)
        self.deptOptionMenu.pack(side=LEFT)
        
        posFrame = Frame(self.root)
        posFrame.pack(padx=10)
        
        posLabel = Label(posFrame, text="Position")
        posLabel.pack(side=LEFT)
        
        posOptionMenu = OptionMenu(posFrame, self.position, "--", "Professor", "Associate Professor",
                                   "Assistant Professor")
        posOptionMenu.pack(side=LEFT)
        
        self.courseFrame = Frame(self.root)
        self.courseFrame.pack(padx=10)
        
        courseLabel = Label(self.courseFrame, text="Course")
        courseLabel.pack(side=LEFT)

        self.courseList = ["--"]
        self.courseOptionMenu = OptionMenu(self.courseFrame, self.course, *self.courseList, command=self.getSections)
        self.courseOptionMenu.pack(side=LEFT)
        
        self.sectionFrame = Frame(self.root)
        self.sectionFrame.pack(padx=10)
        
        sectionLabel = Label(self.sectionFrame, text="Section")
        sectionLabel.pack(side=LEFT)

        self.sectionList = ["--"]
        self.sectionOptionMenu = OptionMenu(self.sectionFrame, self.section, *self.sectionList)
        self.sectionOptionMenu.pack(side=LEFT)
        
        RIFrame = Frame(self.root)
        RIFrame.pack(padx=10)
        
        RILabel = Label(RIFrame, text="Research Interests")
        RILabel.pack(side=LEFT)
        
        RIEntry = Entry(RIFrame, width = 100, textvariable = self.researchInterests)
        RIEntry.pack(side=LEFT)    

        buttonFrame = Frame(self.root)
        buttonFrame.pack(fill=X)

        submitButton = Button(buttonFrame, text="Submit", command=self.submitInfo)
        submitButton.pack(side=RIGHT)

    def getCourses(self, dept):
        if self.department.get() != "--":
            self.db2 = pymysql.connect(host = "academic-mysql.cc.gatech.edu" , passwd = "a1Rlxylj" , user ="cs4400_Group36",
                             db='cs4400_Group36')
            c = self.db2.cursor()
            query = "SELECT C.courseCode FROM coursesOffered C, department D WHERE C.deptID = D.deptID AND D.name = %s"
            c.execute(query, dept)
            items = c.fetchall()
            self.courseList = ["--"]
            for i in items:
                self.courseList += [i[0]]
            self.courseOptionMenu.pack_forget()
            self.courseOptionMenu = OptionMenu(self.courseFrame, self.course, *self.courseList, command=self.getSections)
            self.courseOptionMenu.pack(side=LEFT)
            self.course.set("--")
            self.section.set("--")
            c.close()
            self.db2.close()
        else:
            showwarning("ERROR", "Please select a valid department.")

    def getSections(self, course):
        if self.course.get() != "--":
            db3 = pymysql.connect(host = "academic-mysql.cc.gatech.edu" , passwd = "a1Rlxylj", user = "cs4400_Group36", db='cs4400_Group36')
            c = db3.cursor()
            query = "SELECT S.letter FROM section S, courseSection C WHERE S.crn = C.sectionCRN AND C.courseCode = %s"
            c.execute(query, course)
            items = c.fetchall()
            self.sectionList = ["--"]
            for i in items:
                self.sectionList += [i[0]]
            self.sectionOptionMenu.pack_forget()
            self.sectionOptionMenu = OptionMenu(self.sectionFrame, self.section, *self.sectionList)
            self.sectionOptionMenu.pack(side=LEFT)
            self.section.set("--")
            c.close()
            db3.close()
            
        else:
            showwarning("ERROR", "Please select a valid course.")

    def submitInfo(self):
        db4 = pymysql.connect(host = "academic-mysql.cc.gatech.edu" , passwd = "a1Rlxylj", user = "cs4400_Group36", db='cs4400_Group36')
        c = db4.cursor()
        try:
            if self.position.get() != "--" and self.department.get() != "--" and self.course.get() != "--" and self.section.get() != "--":
                query = "UPDATE instructor SET position=%s, address=%s, name=%s, email=%s, dob=%s, permAddress=%s, gender=%s, contactNum=%s WHERE username=%s"
                c.execute(query, (self.position.get(), self.address.get(), self.name.get(), self.email.get(), self.dob.get(), self.permAddress.get(), self.gender.get(), self.contactNumber.get(), self.un))
                query = "SELECT deptID FROM department WHERE name = %s"
                c.execute(query, self.department.get())
                items = c.fetchall()
                actDept = items[0][0]

                query = """SELECT count( *) FROM instrDept WHERE
                instructorUsername=%s"""
                c.execute(query, self.un)
                count = c.fetchall()[0][0]
                if count == 0:
                    query = """INSERT INTO instrDept VALUES(%s,%s)"""
                    c.execute(query, (self.un,actDept))
                else:
                    query = "UPDATE instrDept SET deptID = %s WHERE instructorUsername = %s"
                    c.execute(query, (actDept, self.un))

                query = """SELECT count( *) FROM teaches WHERE
                instructorUsername=%s"""
                c.execute(query, (self.un))
                count = c.fetchall()[0][0]
                query = """SELECT S.crn FROM section S, courseSection C WHERE S.crn
                = C.sectionCRN AND C.courseCode = %s AND S.letter = %s"""
                c.execute(query, (self.course.get(), self.section.get()))
                crn = c.fetchall()[0][0]
                if count == 0:
                    query = """ INSERT INTO teaches VALUES(%s,%s)"""
                    c.execute(query,(self.un, crn))
                else:
                    query = """UPDATE teaches SET sectionCRN=%s WHERE
                    instructorUsername=%s"""
                    c.execute(query, (crn, self.un))

                query = """DELETE FROM researchInterests WHERE
                instructorUsername=%s"""
                c.execute(query, self.un)
                ints = self.researchInterests.get().split(",")
                for i in range(len(ints)):
                    ints[i] = ints[i].strip()
                    query = """SELECT count( *) FROM researchInterests WHERE
                    instructorUsername=%s AND research=%s"""
                    c.execute(query, (self.un, ints[i]))
                    counts = c.fetchall()[0][0]
                    if counts == 0:
                        query = """INSERT INTO researchInterests
                        VALUES(%s,%s)"""
                        c.execute(query, (self.un, ints[i]))

            else:
                if self.position.get() == "--":
                    showwarning("ERROR","Please select a position.")
                elif self.department.get() == "--":
                    showwarning("ERROR","Please select a department.")
                elif self.course.get() == "--" or self.section.get() == "--":
                    showwarning("ERROR","Please select a course/section.")
                else:
                    showwarning("ERROR","Invalid, please try again.")
                c.close()
                db4.commit()
                db4.close()
                return

            c.close()
            db4.commit()
            db4.close()
            showinfo("Success", "You successfully updated your information")
            self.root.destroy()
            self.Driver.launch_homepage([0,1,0],self.un)
        except:
            showwarning("ERROR","Course already taught by\na different professor.\nPlease select a different course/section.")
            return
        c.close()
        db4.commit()
        db4.close()

# This is the main method of the Login file to be used for debuggin purposes.
# This method is used to create an instance of the Login class.
if __name__=='__main__':
    app = FacultyPI()
