from datetime import date
from enum import Enum

menu ="""---------------------------------------------------------------
Welcome to TUM's student management system!
What do you want to do?
g - General operations
f - Faculty operations
s - Student operations

q - Quit Program"""

general_operations = """---------------------------------------------------------------
General operations
What do you want to do?

nf - create faculty
ss - search student and show faculty
df - display faculties
dff - display all faculties of a field

b - back
q - Quit Program
"""

faculty_operations = """---------------------------------------------------------------
Faculty operations
What do you want to do?

ns - create student
gs - graduate student
ds - display enrolled students
dg - display graduated students
bf - check if student belongs to faculty

b - back
q - Quit Program
"""

student_operation = """---------------------------------------------------------------
Student operations
What do you want to do?

There is nothing to do here at the moment.

b - back
q - Quit Program
"""

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Creaza un Student
class Student:
    def __init__(self) -> None:
        self.facultyAbbreviation,self.firstName,self.lastName,self.email,self.dateOfBirth =input().split("/")
        
    def studC(self):
        print("Succes!\nFaculty Abbreviation:", self.facultyAbbreviation,
               "\nName:", self.firstName, self.lastName,
               "\nEmail: ",self.email,
               "\nDate of Birth: ",self.dateOfBirth)
        
        with open("Enrolled.txt","a") as f:
            f.write(f"{self.facultyAbbreviation},")
            f.write(f"{self.firstName},")
            f.write(f"{self.lastName},")
            f.write(f"{self.email},")
            f.write(f"{self.dateOfBirth}\n")
        
def createStudent():
    print("Creaza un Student.\nExemplu:<faculty abbreviation>/<first name>/<last name>/<email>/<dateOfBirth")
    stud = Student()
    stud.studC()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Graduate a student

student_data = []
gstudent_data = []
with open("Enrolled.txt","r") as f:
    data = f.readlines()
    for line in data:
        noN = line.replace("\n","")
        splited = noN.split(",")
        student_data.append(splited)

def grad_stud(): 
    x = input()
    found = False
    for elem in student_data:
        if elem[3] == x:
           found = True
           print(f"Congratulations, {elem[1]} has graduated")
           with open("Graduated.txt","a") as f:               
               for item in elem:
                   f.write(item + ",")
               f.write("\n")
               student_data.remove(elem)
           with open("Enrolled.txt","w") as file:
                       file.write("")#am sters tot din file    
           for a in student_data:
                   a = a[0:5]               
                   for b in a:
                       with open("Enrolled.txt","a") as file:
                           file.write(b)#am adaugat ce  avem nevoie
                           file.write(",")
                   with open("Enrolled.txt","a") as file:
                       file.write("\n")
                                      
    if found == False:
        print("Student not found")
        
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#display student
def dis_stud():
    x = input()
    for i in student_data:
        if x == i[0]:
            print(i[1:5])
        else:
            print("Nu exista asa facultate")
            terminal_menu()

def dis_gstud():
    x = input()
    for i in gstudent_data:
        if x == i[0]:
            print(i[1:5])
        else:
            print("Nu exista asa facultate")
            terminal_menu() 
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#check if a student belongs to a faculty

def check():
    x,y = input().split("/")
    found_student = False
    found_faculty = False
    for i in student_data:
        if x == i[0] and found_faculty == False:
            found_faculty = True
        if y == i[3] and found_student == False:
            found_student = True
        if found_faculty and found_student:
            print(f"Studentul {i[1]} {i[2]} face parte dan facultatea {x}")
    
    if not found_faculty:
        print("Ati introdus <faculty abbreviation> incorect")
    if not found_student:
        print("Studentul nu face parte din aceasta facultate") 

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Create Faculty
StudyField = ["MECHANICAL_ENGINEERING","SOFTWARE_ENGINEERING","FOOD_TECHNOLOGY","URBANISM_ARHITECTURE","VETERINARY_MEDICINE"]
class Faculty:
    def __init__(self) -> None:
        found = False
        self.facultyName,self.facultyAbbreviation,self.field = input().split("/")
        StudyField1 = ["MECHANICAL_ENGINEERING","SOFTWARE_ENGINEERING","FOOD_TECHNOLOGY","URBANISM_ARHITECTURE","VETERINARY_MEDICINE"]
        for i in StudyField1:
            if i == self.field:
                print("---------------------------------------------------------------\nFaculty Created!\nFaculty Name:", self.facultyName,
                    "\nFaculty Abbreviation:", self.facultyAbbreviation,
                    "\nField: ",self.field)
        
                with open("Faculties.txt","a") as f:
                    f.write(self.facultyName + ",")
                    f.write(self.facultyAbbreviation + ",")
                    f.write(self.field + '\n')
                found = True
        if not found:
            print("---------------------------------------------------------------\nStudy Field Incorect")    
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Search student and show faculty
with open("Enrolled.txt","r") as f:
    data = f.readlines()
    for line in data:
        noN = line.replace("\n","")
        splited = noN.split(",")
        student_data.append(splited)
with open("Faculties.txt","r") as f:
    data = f.readlines()
    facultiesList = []
    for line in data:
        noN = line.replace("\n","")
        splited = noN.split(",")
        facultiesList.append(splited) 
    

def searchStudent():
    x = input()
    found = False
    for i in student_data:
        if x == i[3]:
            for z in facultiesList:
                if i[0].lower() == z[1].lower(): 
                    found = True
                    print(f"Studentul: {i[1]} {i[2]}, Facultatea: {z[0]}") 
            break     
    if not found: 
        print("Nu avem asa student") 
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Display all faculties of a field
def dis_ff():
    x = input("Type Field:").upper()
    ff_list = []
    for i in facultiesList:
        if x == i[2]:
            ff_list.append(i[0])
    print(ff_list)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Functia Terminal
def terminal_menu():
    with open("Enrolled.txt","r") as f:
        data = f.readlines()
        for line in data:
            noN = line.replace("\n","")
            splited = noN.split(",")
            student_data.append(splited)

    with open("Graduated.txt","r") as f:
        data = f.readlines()
        for line in data:
            noN = line.replace("\n","")
            splited = noN.split(",")
            gstudent_data.append(splited)
              
    print(menu)
    inp1 = input().lower()
    if inp1 == "g":#General Operations
        print(general_operations)
        inp2 = input().lower()
        if inp2 == "b":
            terminal_menu()
        elif inp2 == "nf":
            print("Faculty Field trebuie sa fie unul din lista de mai jos")
            for i in StudyField:
                print(i)
            print("Creaza Facultatea.\nExemplu:<faculty name>/<faculty abbreviation>/<field>")
            Faculty()
            terminal_menu()
        elif inp2 == "ss":
            print("Enter student's email:")
            searchStudent()
            terminal_menu()
        elif inp2 == "df":
            print(facultiesList)
            terminal_menu()
        elif inp2 == "dff":
            dis_ff()
            terminal_menu()
        elif inp2 == "q":
            print("Program quited")
        else:
            print("Nu exista asa comanda")
            terminal_menu()
            
    elif inp1 == "f":#Faculty Operations
        print(faculty_operations)
        inp2 = input().lower()
        if inp2 == "ns":
            createStudent()
            terminal_menu()
        elif inp2 == "gs":
            print("Enter student's email for graduation:")
            grad_stud()
            terminal_menu()
        elif inp2 == "ds":
            print("Type faculty abbreviation:")
            dis_stud()
            terminal_menu()        
        elif inp2 == "dg":
            print("Type faculty abbreviation:")
            dis_gstud()
            terminal_menu()        
        elif inp2 == "bf":
            print("Type: <faculty abbreviation>/<email> ")
            check()
            terminal_menu()
        elif inp2 == "b":
            terminal_menu()
        elif inp2 == "q":
            print("Program quited") 
        else:
            print("Nu exista asa comanda") 
            terminal_menu()

    elif inp1 == "s":#Student Operations
        print(student_operation)
        inp2 = input().lower()
        if inp2 == "b":
            terminal_menu()
        elif inp2 == "q":
            print("Program quited")
        else:
            print("Nu exista asa comanda") 
            terminal_menu()   
    elif inp1 == "q":
        print("Program quited")
        
    else:
        print("Nu exista asa comanda")
        terminal_menu()
   
terminal_menu()





