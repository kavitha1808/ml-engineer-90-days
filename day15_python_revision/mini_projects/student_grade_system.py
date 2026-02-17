"""
Student Grade Management System
Clean, refactored, modular design
"""

def get_marks() -> list:
    marks = []
    count = int(input("Enter number of subjects: "))

    for i in range(count):
        while True:
            try:
                mark = int(input(f"Enter mark {i+1}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100")
            except ValueError:
                print("Invalid input")
    return marks


def calculate_average(marks: list) -> float:
    return sum(marks) / len(marks)


def assign_grade(avg: float) -> str:
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "F"


def main():
    marks = get_marks()
    average = calculate_average(marks)
    grade = assign_grade(average)

    print("\n--- Result ---")
    print("Marks:", marks)
    print("Average:", average)
    print("Grade:", grade)


if __name__ == "__main__":
    main()
