# Student Enrollment & Attendance System

# List to store students
students = []

# Set to store attendance
attendance = set()

# Enrolling students (tuple = fixed data)
student1 = (101, "Kavitha", "AI & DS")
student2 = (102, "Arun", "CSE")
student3 = (103, "Meena", "ECE")

students.append(student1)
students.append(student2)
students.append(student3)

print("Students enrolled successfully")

# Mark attendance
attendance.add(101)
attendance.add(102)
attendance.add(101)   # duplicate ignored automatically

# Display all students
print("\nAll Enrolled Students:")
for s in students:
    print("ID:", s[0], "| Name:", s[1], "| Dept:", s[2])

# Display attendance
print("\nPresent Student IDs:")
print(attendance)
