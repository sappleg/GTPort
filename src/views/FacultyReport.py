# Figure 17 Effect of tutoring on Student Performance

from tkinter import *
import pymysql
from tkinter.messagebox import showwarning

class FacultyReport:
    def __init__(self, driver, un):
        self.Driver = driver
        self.un = un

        self.root = Tk()
        self.root.title("Faculty Report")

        self.dept = StringVar()
        self.dept.set("--")

        self.makeWindow()
        self.root.mainloop()

    def makeWindow(self):
        self.label = Label(self.root, text="Department: ")
        self.label.grid(row=0, column=0)
        
        self.deptList = ["--", "Aerospace Engineering","Biology", "Biomedical Engineering", "Computer Science","Electrical & Computer Engineering"]
        self.options = OptionMenu(self.root, self.dept, *self.deptList, command=self.populate)
        self.options.grid(row=0, column=1, columnspan=5)
        
        self.label1 = Label(self.root, text = 'Course Code |')
        self.label1.grid(row=1, column=0, sticky=W)

        self.label2 = Label(self.root, text = 'Course Name |')
        self.label2.grid(row=1, column=1, sticky=EW)

        self.label3 = Label(self.root, text = 'Avg. Grade for No. of Tutoring Session')
        self.label3.grid(row=1, column=2, columnspan=3, sticky=EW)

        self.label4 = Label(self.root, text = '>3 Tutoring Sessions |')
        self.label4.grid(row=2, column=2, sticky=EW)

        self.label5 = Label(self.root, text = '1-3 Tutoring Sessions |')
        self.label5.grid(row=2, column=3, sticky=EW)

        self.label6 = Label(self.root, text = 'No Tutoring Sessions')
        self.label6.grid(row=2, column=4, sticky=EW)


        self.link1 = Button(self.root, text = 'Go To Homepage', command=self.returnHome)
        self.link1.grid(row=4, column=4, columnspan=2, sticky=E)

        self.bodyFrame = Frame(self.root)
        self.bodyFrame.grid(row=3,columnspan=5,sticky=EW)

    def populate(self, dept):
        if self.dept.get() != "--":
            db = pymysql.connect(host = "academic-mysql.cc.gatech.edu" , passwd = "a1Rlxylj" , user ="cs4400_Group36",
                             db='cs4400_Group36')
            c = db.cursor()
            query = "SELECT C.courseCode, C.courseTitle FROM coursesOffered C, department D WHERE C.deptID = D.deptID AND D.name = %s"
            c.execute(query, dept)
            items = c.fetchall()
            itemList = []
            for i in items:
                y = []
                for x in i:
                    y += [x]
                y += [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
                itemList += [y]
            for i in itemList:
                queryA = "SELECT R.grade, R.studentUsername, R.sectionCRN FROM registers R, courseSection C WHERE R.sectionCRN = C.sectionCRN AND C.courseTitle = %s AND R.grade NOT LIKE 'NULL'"
                c.execute(queryA, i[1])
                a = c.fetchall()
                for b in a:
                    queryB = "SELECT COUNT(*) FROM tutorLog WHERE studentUsername = %s AND sectionCRN = %s"
                    c.execute(queryB, (b[1],b[2]))
                    finalItems = c.fetchall()
                    for m in finalItems:
                        if m[0] > 3:
                            if b[0] == "A":
                                i[2][0] += 1
                            elif b[0] == "B":
                                i[2][1] += 1
                            elif b[0] == "C":
                                i[2][2] += 1
                            elif b[0] == "D":
                                i[2][3] += 1
                            elif b[0] == "F":
                                i[2][4] += 1
                        elif m[0] <= 3 and m[0] >= 1:
                            if b[0] == "A":
                                i[3][0] += 1
                            elif b[0] == "B":
                                i[3][1] += 1
                            elif b[0] == "C":
                                i[3][2] += 1
                            elif b[0] == "D":
                                i[3][3] += 1
                            elif b[0] == "F":
                                i[3][4] += 1
                        elif m[0] < 1:
                            if b[0] == "A":
                                i[4][0] += 1
                            elif b[0] == "B":
                                i[4][1] += 1
                            elif b[0] == "C":
                                i[4][2] += 1
                            elif b[0] == "D":
                                i[4][3] += 1
                            elif b[0] == "F":
                                i[4][4] += 1
            for x in itemList:
                if (x[2][0]+x[2][1]+x[2][2]+x[2][3]+x[2][4]) == 0:
                    gpa3 = "N/A"
                else:
                    gpa3 = ((x[2][0]*4)+(x[2][1]*3)+(x[2][2]*2)+(x[2][3]*1)+(x[2][4]*0))/(x[2][0]+x[2][1]+x[2][2]+x[2][3]+x[2][4])
                    float(gpa3)
                if (x[3][0]+x[3][1]+x[3][2]+x[3][3]+x[3][4]) == 0:
                    gpa2 = "N/A"
                else:
                    gpa2 = ((x[3][0]*4)+(x[3][1]*3)+(x[3][2]*2)+(x[3][3]*1)+(x[3][4]*0))/(x[3][0]+x[3][1]+x[3][2]+x[3][3]+x[3][4])
                    float(gpa2)
                if (x[4][0]+x[4][1]+x[4][2]+x[4][3]+x[4][4]) == 0:
                    gpa1 = "N/A"
                else:
                    gpa1 = ((x[4][0]*4)+(x[4][1]*3)+(x[4][2]*2)+(x[4][3]*1)+(x[4][4]*0))/(x[4][0]+x[4][1]+x[4][2]+x[4][3]+x[4][4])
                    float(gpa1)

                x += [[gpa3, gpa2, gpa1]]
            goodList = []
            for y in itemList:
                goodList += [[y[0],y[1],y[5][0],y[5][1],y[5][2]]]
            c.close()
            db.close()
            # Something about this grid remove/forget doesnt
            # work correctly! But the content is correct!
            self.bodyFrame.grid_remove()
            for num in range(len(goodList)):
                Lcode = Label(self.bodyFrame, text=goodList[num][0])
                Lcode.grid(row=num,column=0)
                Ltitle = Label(self.bodyFrame, text=goodList[num][1])
                Ltitle.grid(row=num, column=1)
                Lgpa3 = Label(self.bodyFrame, text=str(goodList[num][2]), width=20)
                Lgpa3.grid(row=num, column=2)
                Lgpa2 = Label(self.bodyFrame, text=str(goodList[num][3]), width=20)
                Lgpa2.grid(row=num, column=3)
                Lgpa1 = Label(self.bodyFrame, text=str(goodList[num][4]), width=20)
                Lgpa1.grid(row=num, column=4)
            self.bodyFrame.grid(row=3,columnspan=5,sticky=EW)
        else:
            showwarning("ERROR", "Please select a valid department.")

    def returnHome(self):
        self.root.destroy()
        self.Driver.launch_homepage([0,1,0],self.un)
        




if __name__=="__main__":
    app = FacultyReport()


