students = {}

def add_student():
    try:
        name = input("Enter student name: ")
        marks_count = int(input("How many subjects? "))

        if marks_count <= 0:
            raise ValueError

        marks = []
        for i in range(marks_count):
            mark = int(input(f"Enter mark {i+1}: "))
            if mark < 0 or mark > 100:
                raise ValueError
            marks.append(mark)

        students[name] = marks
        print("Student added successfully")

    except ValueError:
        print("Invalid marks or count entered")
    except Exception as e:
        print("Unexpected error:", e)


def view_student():
    try:
        name = input("Enter student name: ")
        print("Marks:", students[name])
    except KeyError:
        print("Student not found")


def calculate_average():
    try:
        name = input("Enter student name: ")
        marks = students[name]
        avg = sum(marks) / len(marks)
        print("Average marks:", avg)
    except KeyError:
        print("Student not found")
    except ZeroDivisionError:
        print("No marks available")


def save_to_file():
    try:
        file = open("students.txt", "w")
        for name, marks in students.items():
            file.write(name + ":" + str(marks) + "\n")
        print("Data saved to file")
    except Exception:
        print("Error while saving file")
    finally:
        try:
            file.close()
        except:
            pass


def load_from_file():
    try:
        file = open("students.txt", "r")
        for line in file:
            name, marks = line.strip().split(":")
            students[name] = eval(marks)
        print("Data loaded successfully")
    except FileNotFoundError:
        print("File not found")
    except Exception:
        print("File corrupted or invalid")
    finally:
        try:
            file.close()
        except:
            pass


def list_marks_by_index():
    try:
        name = input("Enter student name: ")
        index = int(input("Enter mark index: "))
        print("Mark:", students[name][index])
    except IndexError:
        print("Invalid index")
    except KeyError:
        print("Student not found")
    except ValueError:
        print("Invalid input")


# MAIN MENU
while True:
    try:
        print("\n--- Student Management System ---")
        print("1. Add student")
        print("2. View student marks")
        print("3. Calculate average")
        print("4. Save to file")
        print("5. Load from file")
        print("6. Access mark by index")
        print("7. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            add_student()
        elif choice == 2:
            view_student()
        elif choice == 3:
            calculate_average()
        elif choice == 4:
            save_to_file()
        elif choice == 5:
            load_from_file()
        elif choice == 6:
            list_marks_by_index()
        elif choice == 7:
            print("Exiting program")
            break
        else:
            print("Invalid choice")

    except ValueError:
        print("Please enter numeric choice")
    finally:
        print("Menu cycle completed")
