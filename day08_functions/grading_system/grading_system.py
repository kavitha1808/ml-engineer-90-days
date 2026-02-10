students = {}

def calculate_total(marks):
    return sum(marks)

def calculate_average(total, count):
    return total / count

def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "Fail"

def print_report(name, marks):
    total = calculate_total(marks)
    avg = calculate_average(total, len(marks))
    grade = calculate_grade(avg)

    print("\nStudent:", name)
    print("Marks:", marks)
    print("Total:", total)
    print("Average:", avg)
    print("Grade:", grade)

def add_student(name, marks):
    students[name] = marks

def generate_reports():
    for name in students:
        print_report(name, students[name])
        print("-" * 25)

add_student("Kavitha", [85, 90, 88])
add_student("Arun", [60, 70, 65])
generate_reports()
