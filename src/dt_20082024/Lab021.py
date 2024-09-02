# Grade Calculator
# Write a program that calculates and displays the letter grade
# for a given numerical score (e.g., A, B, C, D, or F)
# based on the following grading scale:

# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59
# logic
# input is integer (marks)
# output is string
marks=int(input("enter marks"))
if marks>=90 and marks<=100:  # simplified chaining format 90 <= marks <= 100
    print("your grade is A")
elif marks>=80 and marks<90:
    print("B")
elif marks>=70 and marks<80:
    grade="C"
    print("Your grade is", grade)
elif marks>=60 and marks<70:
    print("D")
else:
    print("F")


