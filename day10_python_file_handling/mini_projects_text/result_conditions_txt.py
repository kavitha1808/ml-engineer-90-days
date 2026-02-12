file = open("student_record.txt", "r")
lines = file.readlines()
file.close()

print("---- STUDENT RESULTS ----")

for line in lines:
    data = line.strip().split(",")

    name = data[0]
    marks = int(data[2])

    if marks >= 75:
        grade = "Distinction"
    elif marks >= 40:
        grade = "Pass"
    else:
        grade = "Fail"

    print(name, ":", marks, "-", grade)
