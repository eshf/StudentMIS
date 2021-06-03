import csv 
from collections import Counter
 
 

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
                if(len(s)!=9):
                        return "Length is not 9"
                elif (s[8]=="B" and r==0):
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
                
     
#def checkData(): 
    #print("{0:<14} {1:<14} {2:<14} {3:<30}".format("First Name", "Last Name", "Student ID", "Comments")) 
    #filePath = "data.csv" 
    #with open(filePath) as csvfile: 
        #reader = csv.DictReader(csvfile) 
        #for row in reader: 
            #f = row['first_name'] 
            #l = row['last_name'] 
            #s = row['student_id'] 
            #rule= row['Rule to test'] 
            #print("{0:<14} {1:<14} {2:<14} {3:<30}".format(f, l, s, rule)) 
 
#def checkData():
    #print("{0:<14} {1:<14} {2:<14} {3:<30}".format("First Name", "Last Name", "Student ID", "Comments")) 
    #filePath = "data.csv" 
    #with open(filePath) as csvfile: 
        #reader = csv.DictReader(csvfile) 
        #for row in reader: 
            #f = row['first_name'] 
            #l = row['last_name'] 
            #s_id = row['student_id'] 
            #rule= row['Rule to test']
            #if(len(s)!=9): 
                #return "Length of Student ID is not 9" 
            #else:
                #isValidStudentIDLetter(s)

#def checkData():
        #print("{0:<14} {1:<14} {2:<14} {3:<30}".format("First Name", "Last Name", "Student ID", "Comments")) 
        #filePath = "data.csv" 
        #with open(filePath) as csvfile: 
                #reader = csv.DictReader(csvfile)
                #for row in reader: 
                        #f = row['first_name'] 
                        #l = row['last_name'] 
                        #s_id = row['student_id']
                        #rule= row['Rule to test'] 
                        #print("{0:<14} {1:<14} {2:<14} {3:<30}".format(f, l, s_id, rule))
                        #break
                
def checkValid():
        s=input("Please enter your Student ID:")
        check=False
        checkok= isValidStudentIDFormat(check, s)
        checkLetter=isValidStudentIDLetter(s)
        if(checkok==True):
                print("Valid Student ID")
        elif(checkLetter==True):
                print ("Valid Student ID")
        else:
                print("Invalid Student ID")

                        

checkValid()