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

marks = []

for i in range(5):
    score = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(score)

average = sum(marks) / 5

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "Fail"

print("Average Marks:", average)
print("Grade:", grade)
