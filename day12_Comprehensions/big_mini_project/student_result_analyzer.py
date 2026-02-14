# Student Result Analyzer with Grades and Exception Handling

def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 50:
        return "C"
    else:
        return "F"


students = {}

try:
    # Step 1: Read input file
    with open("input_marks.txt", "r") as file:
        lines = file.readlines()

    if not lines:
        raise ValueError("Input file is empty")

    # Step 2: Validate and process file data
    for line in lines:
        try:
            name, mark = line.strip().split(",")

            mark = int(mark)

            if mark < 0 or mark > 100:
                raise ValueError("Marks out of valid range")

            students[name] = mark

        except ValueError:
            print(f"Skipping invalid record: {line.strip()}")

except FileNotFoundError:
    print("Error: input_marks.txt file not found.")
    exit()

except ValueError as e:
    print("Error:", e)
    exit()

# Step 3: Create grade mapping
student_grades = {name: get_grade(mark) for name, mark in students.items()}

# Step 4: Separate passed and failed students
passed_students = {name: mark for name, mark in students.items() if mark >= 50}
failed_students = {name: mark for name, mark in students.items() if mark < 50}

# Step 5: Statistics
total_students = len(students)
average_marks = sum(students.values()) / total_students if total_students > 0 else 0

# Step 6: Write output file
with open("result_report.txt", "w") as report:
    report.write("📘 STUDENT RESULT REPORT (SAFE MODE)\n")
    report.write("---------------------------------\n\n")

    report.write(f"Total Valid Students: {total_students}\n")
    report.write(f"Average Marks: {average_marks:.2f}\n\n")

    report.write("📊 Student Grades:\n")
    for name, mark in students.items():
        report.write(f"{name} - {mark} → Grade {student_grades[name]}\n")

    report.write("\n✅ Passed Students:\n")
    for name, mark in passed_students.items():
        report.write(f"{name} - {mark}\n")

    report.write("\n❌ Failed Students:\n")
    for name, mark in failed_students.items():
        report.write(f"{name} - {mark}\n")

print("✔ Result analysis completed safely. Check result_report.txt")
