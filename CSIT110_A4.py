import csv, shutil, A3
import os.path
from collections import Counter
studentlst = []



def printMenu():
    print("===============================================")
    print("Student Records Management System")
    print("===============================================")
    print("1: Insert a new student")
    print("2: Delete a student")
    print("3: Save data to file and exit")



#def insert_new_student():
    #filePath = "data.csv"
    #check=False
    #while True:
        #firstName=input("Enter first name:")
        #lastName= input("Enter last name:")
        #if firstName=="":
            #print("First Name is empty, please enter again:")
            #if lastName=="":
               #print("Last Name is empty, please enter again:")
            #else:
                #break
    #while True:
        #s=input("Please enter your Student ID:")
        #print()
        #if (A3.isValidStudentIDFormat(check, s)==True):
            #validStInput= [firstName, lastName, studentID]
            #studentlst.append(validStInput)
            #print("New Student added to the list")
            #print(validStInput)
        #else:
            #print("The format of Student ID added is incorrect. Please enter again.")





def insert_new_student():
    while (A3.isValidStudentIDFormat(check,s)==True):
            students={}
            filePath = "data.csv"
            print("Insert a new student")
            f_name = input("Enter first name: ")
            l_name = input("Enter last name: ")
            studentID=input("Enter student id: ")
            #create a user detail using dictionary
            studentlst = {"first_name":f_name, "last_name":l_name, "student_id": studentID}
            students[studentID] = studentlst
            print(students)
            break
    
        
#def checkData(studentID):
    
    #return isValidStudentIDFormat(check,s)

def delete_student():
    filePath = "data.csv"
    found = 'false'
    fieldnames = ['first_name', 'last_name', 'student_id']
    print("Delete a student")
    studentID = input("Enter student id to delete: ")      
    with open(filePath, 'r') as csvfile, open('output.csv', 'w') as outputfile:
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        writer = csv.DictWriter(outputfile, fieldnames=fieldnames)
        for row in reader:
            if not studentID == row['student_id']:
                writer.writerow({'first_name': row['first_name'], 'last_name': row['last_name'], 'student_id': row['student_id']})
            if studentID == row['student_id']:  
                found = 'true'
    shutil.move('output.csv', filePath) 
    if found == "false":
        print("Student ID not found")

def save_data():
    filePath="data.csv"
    file_exists = os.path.isfile(filePath)    
    if file_exists:
        with open('data.csv', 'a') as writer:
            for i in range(0, len(studentlst)):
                for value in studentlst[i]:
                    writer.write(value+"\t")
            writer.write("\n") 
            
def isValidStudentIDFormat (check, s):
        reason = ""
        if len(s) == 9:
            if s[0] == 'S':
                letters = "BCDEFGHIJKLM"
                if s[8] in letters:
                    r = s[1:8]
                    if (not r.isdigit()):
                        reason = "Must contain 7 numbers"
                        return check, reason
                    check = True
                    reason = "Valid student ID"
                    return check, reason
                else:
                    reason = "Invalid last letter"
            else:
                reason  = "Must start with a letter 'S'"
        else:
            reason = "Length is not 9"
        return check, reason
check= False
#while (check == False):
        #s_id= input ("Enter student ID: ")
        #check, reason = isValidStudentIDFormat (check, s_id)
        #print (reason)
    
    # The function returns a True if the format is right,
    # else it returns the invalid reason
    
def isValidStudentIDLetter(s):
        while(isValidStudentIDFormat):
            r = (int(s[1])*2 + int(s[2])*7 + int(s[3])*6 + int(s[4])*5 + int(s[5])*4 + int(s[6])*3 + int(s[7])*2) % 11
            if (s[8]=="B" and r==0):
                return "Valid student ID"
            elif (s[8]=="C" and r==1):
                return "Valid student ID"
            elif(s[8]=="D" and r==2):
                return "Valid student ID"
            elif (s[8]=="E" and r==3):
                return "Valid student ID"
            elif(s[8]=="F" and r==4):
                return "Valid student ID"
            elif(s[8]=="G" and r==5):
                return "Valid student ID"
            elif(s[8]=="H" and r==6):
                return "Valid student ID"
            elif(s[8]=="H" and r==7):
                return "Valid student ID"
            elif(s[8]=="I" and r==8):
                return "Valid student ID"
            elif(s[8]=="J" and r==9):
                return "Valid student ID"
            elif(s[8]=="K" and r==10):
                return "Valid student ID"
            else:
                return "Invalid last letter" 

while True:
    printMenu()
    choice=int(input("Please enter your menu selection [0-2]:"))
    if (choice==1):
        insert_new_student()
    elif(choice==2):
        delete_student()
    elif(choice==3):
        save_data()
        print("===============================================")
        print("Data file saved")
        print("Thank you for using Student Records Management System")
        print("===============================================")
        break
    else:
        print("===============================================")
        print("Invalid choice, please enter again")
        print("===============================================")