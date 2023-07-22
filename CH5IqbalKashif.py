'''
# Name: KASHIF IQBAL
# Program: Chapter 5 - loops
# Description: Test Grade Calculator Program using the if statements 

'''

# CONSTNAT
TITLE = "\nWelcome to Test Grade Calulator Program!\n"
LINE =  "-" * len(TITLE)
NUM_TESTS = 3
A_GRADE = 90
B_GRADE = 80
C_GRADE = 70
D_GRADE = 60
print(TITLE+LINE)


# input integer test score collect from user
scoreList = []
score1 = int(input("Enter test score between 0 and 100: "))
if score1 <=100 and score1 >= 0:
    scoreList.append(score1)
else:
    print("Error! enter test score between 0-100: ")

score2 = int(input("Enter test score between 0 and 100: "))
if score2 <=100 and score2 >= 0:
    scoreList.append(score2)
else:
    print("Error! enter test score between 0-100: ")

score3 = int(input("Enter test score between 0 and 100: "))
if score3 <=100 and score3 >= 0:
    scoreList.append(score3)
else:
    print("Error! enter test score between 0-100: ")




# Find a lowest Value using a if statement 
loScore = score1
if score2 < loScore:
    loScore = score2
if score3 < loScore:
    loScore = score3


totalScore = score1+score2+score3

# Find avgScore by addign 3 scores and subtracting loScore and dividigng by (NUM_TEST)
avgScore = totalScore/NUM_TESTS


# Find a letterGrade of avgScore to using if/elsif/else logic 
if avgScore >= A_GRADE:
    letterGrade = 'A'
elif avgScore >= B_GRADE and avgScore <= A_GRADE:
    letterGrade = 'B'
elif avgScore >= C_GRADE and avgScore <= B_GRADE:
    letterGrade = 'C'
elif avgScore >= D_GRADE and avgScore <= C_GRADE:
    letterGrade = 'D'
else:
    letterGrade = "Very Lowet Avg"

#Display loScore, avgScore, and letterGrade.
print(LINE)
print("Lowest test score dropped =", loScore)
print("Average test score = ", "{:.2f}".format(avgScore))
print("Letter Grade = ", letterGrade)
print(LINE)