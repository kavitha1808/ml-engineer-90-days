file = open("student_record.txt", "a")

name = input("Enter student name: ")
roll = input("Enter roll number: ")
marks = input("Enter marks: ")

file.write(name + "," + roll + "," + marks + "\n")
file.close()

print("Record saved!")

file = open("student_record.txt", "r")
print("\n--- STUDENT RECORDS ---")
print(file.read())
file.close()
