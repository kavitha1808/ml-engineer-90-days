import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Name", "Marks"])
    writer.writerow([1, "Anu", 88])
    writer.writerow([2, "Rahul", 92])
