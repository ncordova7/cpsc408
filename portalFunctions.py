import sqlite3
from Students import Students


class portalFunctions:
    conn = sqlite3.connect('StudentDB.db')
    cursor = conn.cursor()

    def DisplayAll(self):
        portalFunctions.cursor.execute("SELECT * FROM Student")
        result = portalFunctions.cursor.fetchall()
        for x in result:
            print(x)
        portalFunctions.conn.commit()
    def CreateStudent(self):
     while True:
        try:
            firstName = str(input("Enter Student's First Name: \n"))
            lastName = str(input("Enter Student's Last Name: \n"))
            gpa = float(input("Enter Student's GPA: \n"))
            major = str(input("Enter Student's Major: \n"))
            advisor = str(input("Enter Student's Advisor: \n"))

            students = Students(firstName, lastName, gpa, major, advisor)
            portalFunctions.cursor.execute("INSERT INTO Student('FirstName', 'LastName', 'GPA', 'Major', 'Advisor')"
              "VALUES(?, ?, ?, ?, ?)", students.GetStudentTuple())
            portalFunctions.conn.commit()
            break
        except ValueError:
            print("Invalid value type, try again.")

    def UpdateStudent(self):
        while True:
            try:
                student = int(input("Enter Student's ID: "))
                choice = int(input("Press 0 to change student's major.\n",
                                   "Press 1 if you want to change advisor.\n",
                                   "Press2 to change major and advisor: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value for both the student ID and choice.")

        if choice == 0:
            major = input("Enter new major: ")
            portalFunctions.cursor.execute("UPDATE Student SET Major = ? WHERE StudentID == ?", (major, student))
        elif choice == 1:
            advisor = input("Enter updated advisor: ")
            portalFunctions.cursor.execute("UPDATE Student SET FacultyAdvisor = ? WHERE StudentID == ?", (advisor, student))
        elif choice == 2:
            major = input("Enter updated major: ")
            advisor = input("Enter updated advisor: ")
            portalFunctions.cursor.execute("UPDATE Student SET Major = ? WHERE StudentID == ?", (major, student))
            portalFunctions.cursor.execute("UPDATE Student SET FacultyAdvisor = ? WHERE StudentID == ?", (advisor, student))
        else:
            print(choice)
        portalFunctions.conn.commit()

    def DeleteStudent(self):
        while True:
            try:
                stu = input("Enter student ID that you want to delete: ")
                break
            except ValueError:
                print("Enter numeric value")
        portalFunctions.cursor.execute("DELETE FROM Student WHERE StudentID = {0}".format(stu))
        portalFunctions.conn.commit()

    def SearchStudent(self):
        print("Press 1 for yes or 0 for no.")
        while True:
            try:
                major = int(input("Search by major..."))
                gpa = int(input("Search by GPA..."))
                advisor = int(input("Serach by Advisor... "))
                break
            except ValueError:
                print("Invalid input, choose another option.")

        if major == 1:
            majorSearch = input("Enter the major: ")
            portalFunctions.cursor.execute("SELECT * FROM Student WHERE Major == '{0}'".format(majorSearch))
            result = portalFunctions.cursor.fetchall()
            if result != []:
                for x in result:
                    print(x)
        while True:
            try:
                if gpa == 1:
                    checkGpa = input("Enter the GPA: ")
                    portalFunctions.cursor.execute("SELECT * FROM Student WHERE GPA == '{0}'".format(checkGpa))
                    result = portalFunctions.cursor.fetchall()
                    if result != []:
                        for x in result:
                            print(x)
                    break
            except ValueError:
                print("Invalid GPA, try again.")
        if advisor == 1:
            checkAdvisor = input("Enter Student's Advisor: ")
            portalFunctions.cursor.execute("SELECT * FROM Students WHERE Advisor == '{0}'".format(checkAdvisor))
            result = portalFunctions.cursor.fetchall()
            if result != []:
                for x in result:
                    print(x)

    def Print(result):
        for x in result:

            print(x)