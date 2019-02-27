import sqlite3
from Students import Students
from portalFunctions import portalFunctions

def ShowPortal():
              print("This is the Student Portal, Pick your poison. \n",
              "Press 1 to create a Student Record.\n",
              "Press 2 to display all students.\n"
              " Press 3 to delete a Student Record.\n",
              "Press 4 to edit a student's Major.\n",
              "Press 5 to edit a student's Advisor.\n",
              "Press 6 to search by attribute.\n")

conn = sqlite3.connect("StudentDB.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Student(StudentId INTEGER PRIMARY KEY AUTOINCREMENT,FirstName varchar(25),"
  "LastName varchar(25),GPA NUMERIC,Major varchar(20),FacultyAdvisor varchar(25));")

conn.commit()

menu = portalFunctions()
loop = True
ShowPortal()
while(loop):
    try:
        choose = int(input("Choose an option 1-5."))
        if(choose >= 0 and choose < 6):
            if (choose == 1):
                menu.DisplayAll()
            elif (choose == 2):
                menu.CreateStudent()
            elif (choose == 3):
                menu.UpdateStudent()
            elif (choose == 4):
                menu.DeleteStudent()
            elif (choose == 5):
                menu.SearchStudent()
        else:
            print("Try again... Press 1-5.")
            continue
    except ValueError:
        print("Invalid input.")
        continue

    print()
    cont = input("Press 'X' to exit. Press anything else to continue: ")
    if(cont.lower() == 'x'):
        loop = False
    else:
        print()
        ShowPortal()




