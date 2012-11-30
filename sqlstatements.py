import pymysql

class SQLstatements:
    
    def __init__(self):
        self.db = pymysql.connect(host = "academic-mysql.cc.gatech.edu" , passwd = "a1Rlxylj" , user ="cs4400_Group36",
                             db='cs4400_Group36')
        self.task10()
        self.task7()

        self.db.close()

    def task1(self):
        c = self.db.cursor()
        SQL = """IF (SELECT count( *) FROM adminUser WHERE username = %s AND password = %s) = 1
                THENGO TO ADMIN HOMEPAGEELSE IF 	(SELECT count( *) FROM student WHERE username = %s AND password = %s) = 1
                THEN	GO TO STUDENT HOMEPAGEELSE IF 	(SELECT count( *) FROM instructor WHERE username = %s AND password = %s) = 1
                THEN	GO TO INSTRUCTOR HOMEPAGEELSE	PRINT “Invalid Username/Password”"""
        c.execute(SQL)
        print("SQL Query is:")
        for item in c:
            print(item)
        c.close()

    def task2(self):
        c = self.db.cursor()
        SQL = """IF Password = Confirm Password THENIF Type of User = ‘Student’
                THENIF (SELECT count( *) FROM student WHERE username = %s) = 0
                THENINSERT INTO studentVALUES (Username, Password)
                ELSEPRINT “Student user already exists”ELSE IF Type of User = %s
                THENIF (SELECT count( *) FROM instructor WHERE username = %s) = 0 THEN
                INSERT INTO instructorVALUES (Username, Password)ELSE
                PRINT “Instructor user already exists”	ELSEPRINT “Please select a ‘Type of User’”ELSE
                PRINT “Invalid Password”"""
        c.execute(SQL)
        print("SQL Query is:")
        for item in c:
            print(item)
        c.close()

    def task3a(self): #WORKS
        c = self.db.cursor()
        SQL = "SELECT * FROM student WHERE username = %s"
        c.execute(SQL)
        print("SQL Query is:")
        for item in c:
            print(item)
        c.close()

    def task3b(self):
        c = self.db.cursor()
        SQL = """UPDATE student SET (name, dob, gender, address, permAddress, contactNum, email, major, degree, studentID)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) WHERE username = %s"""
        c.execute(SQL)
        print("SQL Query is:")
        for item in c:
            print(item)
        c.close()

    def task4a(self):#WORKS
        c = self.db.cursor()
        SQL = "SELECT * FROM instructor WHERE username = %s"
        c.execute(SQL)
        print("SQL Query is:")
        for item in c:
            print(item)
        c.close()

    def task4b(self):
        c = self.db.cursor()
        SQL = """UPDATE instructor SET (name, dob, gender, address, permAddress, contactNum, email, position, instructorID)
        VALUES ('Danielle', '1992-06-22', 'F', '10425 Oxford Mill Circle', '729 Brittain Drive', '7703298359', 'dheady3@gmail.com', 'Professor', '31') WHERE username = 'kirky'"""
        c.execute(SQL, ('danielle', ))
        print("SQL Query is:")
        for item in c:
            print(item)
        c.close()

    def task5a(self): #WORKS
        c = self.db.cursor()
        SQL = "SELECT * FROM eduHistory WHERE studentUsername = %s"
        c.execute(SQL)
        print("SQL Query is:")
        for item in c:
            print(item)
        c.close()

    def task5b(self):
        c = self.db.cursor()
        SQL = """SELECT COUNT(*) FROM eduHistory WHERE studentUsername = %s AND nameOfSchool = %s AND yearOfGrad = %s IF counr_edu = 1
        THEN UPDATE eduHistory SET (nameOfSchool, yearOfGrad, degree, major, gpa) VALUES (%s, %s, %s, %s, %s) WHERE studentUsername = %s
        AND nameOfSchool = %s AND yearOfGrad = %s ELSE INSERT INTO eduHistory SET (studentUsername, nameOfSchool, yearOfGrad, degree, major, gpa)
        VALUES (%s, %s, %s, %s, %s, %s)"""
        c.execute(SQL)
        print("SQL Query is:")
        for item in c:
            print(item)
        c.close()

    def task6(self): #WORKS
        c = self.db.cursor()
        SQL = """SELECT courseCode
                FROM coursesOffered
                WHERE deptID = ( 
                SELECT deptID
                FROM department
                WHERE name =  'Aerospace Engineering' ) """
        c.execute(SQL)
        print("SQL Query is:")
        for item in c:
            print(item)
        c.close()

        
    def task7(self):#WORKS
        c = self.db.cursor()
        SQL = "SELECT sectionCRN FROM courseSection WHERE courseCode = %s"
        c.execute(SQL)
        print("SQL Query is:")
        for item in c:
            print(item)
        c.close()

    def task8(self):#WORKS
        c = self.db.cursor()
        SQL = "INSERT INTO teaches(instructorUsername, sectionCRN) VALUES (%s, %s)"
        c.execute(SQL)
        print("SQL Query is:")
        for item in c:
            print(item)
        c.close()

    def task9(self):#WORKS
        c = self.db.cursor()
        count_int = """SELECT count( *) FROM researchInterests WHERE instructorUsername= %s
                    AND research= %s"""
        c.execute(count_int)
        print("SQL Query is:")
        for item in c:
            if item = 0:
                SQL = "INSERT INTO researchInterest(instructorUsername, research)VALUES (‘&Username’, ‘&Interest’)"
                c.execute(SQL)
        c.close()
        
    def task10(self): #WORKS
        c = self.db.cursor()
        SQL = "SELECT name FROM department"
        c.execute(SQL)
        print("SQL Query is:")
        for item in c:
            print(item)
        c.close()
        #db.commit() - This is for making changes to the database. 
 #       self.db.close()

     def task11(self):
        c = self.db.cursor()
        SQL = """SELECT (S.sectionCRN, O.courseTitle, O.courseCode, SE.letter, I.name, SE.classday, SF.classtime, SF.location)
                FROM courseOffered O, couseSection S, teaches T, instructor I, section SE WHERE O.courseTitle = S.courseTitel,
                AND O.courseCode = S.courseCode AND S.sectionCRN = T.sectionCRN AND T.instructorUsername = I.username
                AND S.sectionCRN = SF.crn AND O.deptID = (SELECT deptID FROM department WHERE name = %s)"""
        c.execute(SQL)
        print("SQL Query is:")
        for item in c:
            print(item)
        c.close()

    def task12(self):#WORKS
        c = self.db.cursor()
        SQL = "INSERT INTO registers (studentUsername, sectionCRN, grade, gradeMode) VALUES (%s, %s, NULL, %s)"
        c.execute(SQL)
        print("SQL Query is:")
        for item in c:
            print(item)
        c.close()


    #db = connectMySQL("academic-mysql.cc.gatech.edu","cs4400_Group36","a1Rlxylj")

app = SQLstatements()
