from datetime import date

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

nf/<faculty name>/<faculty abbreviation>/<field> - create faculty
ss/<student email> - search student and show faculty
df - display faculties
df/<field> - display all faculties of a field

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
bf/<faculty abbreviation>/<email> - check if student belongs to faculty

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
        self.facultyAbbreviation,self.firstName,self.lastName,self.email,self.dateOfBirth = input().split("/")
        
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
with open("Enrolled.txt","r") as f:
    data = f.readlines()
    student_data = []
    for line in data:
        noN = line.replace("\n","")
        splited = noN.split(",")
        student_data.append(splited)
# print(student_data)

with open("Graduated.txt","r") as f:
    data = f.readlines()
    gstudent_data = []
    for line in data:
        noN = line.replace("\n","")
        splited = noN.split(",")
        gstudent_data.append(splited)
# print(gstudent_data)

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
            print(i[1:3])
        else:
            print("Nu exista asa facultate")
            terminal_menu()

def dis_gstud():
    x = input()
    for i in gstudent_data:
        if x == i[0]:
            print(i[1:3])
        else:
            print("Nu exista asa facultate")
            terminal_menu() 
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Functia Terminal
def terminal_menu():
    print(menu)
    inp1 = input()
    if inp1 == "g":
        print(general_operations)
        inp2 = input()
        if inp2 == "b":
            terminal_menu()
        elif inp2 == "q":
            print("Program quited")
        else:
            print("Nu exista asa comanda")
            terminal_menu()
            
    elif inp1 == "f":
        print(faculty_operations)
        inp2 = input()
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
        elif inp2 == "b":
            terminal_menu()
        elif inp2 == "q":
            print("Program quited") 
        else:
            print("Nu exista asa comanda") 
            terminal_menu()

    elif inp1 == "s":
        print(student_operation)
        inp2 = input()
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






