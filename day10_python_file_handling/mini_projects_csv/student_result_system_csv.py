import csv

with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)

    name = input("Enter student name: ")
    marks = input("Enter marks: ")

    writer.writerow([name, marks])

print("Student data saved!")

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    print("\n---- STUDENT RESULTS ----")

    for row in reader:
        name = row[0]
        marks = int(row[1])

        if marks >= 75:
            result = "Distinction"
        elif marks >= 40:
            result = "Pass"
        else:
            result = "Fail"

        print(name, ":", marks, "-", result)
