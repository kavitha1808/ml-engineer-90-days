import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    print("---- STUDENT RESULTS ----")

    for row in reader:
        name = row[0]
        marks = int(row[1])

        if marks >= 75:
            grade = "Distinction"
        elif marks >= 40:
            grade = "Pass"
        else:
            grade = "Fail"

        print(name, ":", marks, "-", grade)
