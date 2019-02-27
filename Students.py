import sqlite3
class Students:
    def __init__(self, student_ID,first_name, last_name, gpa, major, advisor):
        self.student_ID = student_ID
        self.first_name = first_name
        self.last_name = last_name
        self.gpa = gpa
        self.major = major

        self.advisor = advisor

    def getfirst_Name(self):
        return self.first_name

    def getlast_Name(self):
        return self.last_name

    def getGPA(self):
        return self.gpa

    def getMajor(self):
        return self.major

    def getAdvisor(self):
        return self.advisor

    def getStudentTuple(self):
        return(self.getfirst_Name(), self.getlast_Name(), self.getGPA(), self.getMajor(), self.getAdvisor())

    def getConn(self):
        conn = sqlite3.connect("StudentDB.db")
        return conn

    def getCursor(self):
        conn = self.getConn()
        cursor = conn.cursor()
        return cursor