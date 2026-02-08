# Mini Project 1: Student Report Card

student_marks = {
    "Maths": 85,
    "Science": 72,
    "English": 90,
    "Social": 80
}

total = 0

for mark in student_marks.values():
    total += mark

average = total / len(student_marks)

print("Total Marks:", total)
print("Average:", average)

if average >= 85:
    print("Grade: A")
elif average >= 60:
    print("Grade: B")
else:
    print("Grade: C")
