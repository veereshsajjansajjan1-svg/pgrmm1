# Student Grade Evaluation Program

# Accept marks from the user
marks = int(input("Enter your marks: "))

# Determine grade
if marks >= 90:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
elif marks >= 60:
    grade = 'D'
else:
    grade = 'Fail'

# Display grade
print("Grade:", grade)
