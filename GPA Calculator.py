# Title: Week 4 - Calculate this, Computer
# Author Name: Anh Vo
# Date: Oct 1, 2020
# Description: Calculate the Term Grade Point Average (GPA)

# Greet the user
print("-----------WELCOME TO GPA CALCULATOR----------")

# Ask the user the number of courses taken
courseNum = int(input("Number of course you take:---> "))
# Initialize Total units, total gradePoint of the term
totalU = 0
totalGradeP = 0

# Use for loops to ask questions
for course in range(courseNum):
#   Ask for Letter grade of each course
    letterG = input("Letter Grade of course "+ str((course+1))+ ":---> ").upper()

#   Convert letter grade to numerical equivalent
#   There is a deduction of 0.33 in grades 
    numEqui = 0.00
    gradeA = ["A+","A","A-"]
    gradeB =["B+","B","B-"]
    gradeC = ["C+","C","C-"]
    fails = ["F", "FD", "N"]
    
    if letterG in gradeA:
        numEqui+= (4.33 - 0.33*gradeA.index(letterG))
    elif letterG in gradeB:
        numEqui+=(3.33 - 0.33*gradeB.index(letterG))
    elif letterG in gradeC:
        numEqui+=(2.33 - 0.33*gradeC.index(letterG))
    elif letterG == "D":
        numEqui+=1.00
    elif letterG in fails:
        numEqui+=0.00
    else:
        print("Cannot define your letter grade")
            
#   Ask for the Unit of the course
    unit = int(input("Unit of course " + str((course+1)) +" :---> "))
    totalU += unit
               
#   Find Grade Point of each course
    gradeP = unit*numEqui
    totalGradeP+=gradeP
    
# Calculate GPA
gpa = totalGradeP/totalU
print("Term Grade Point Average:",round(gpa,2))
 
