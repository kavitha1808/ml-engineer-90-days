try:
    marks = int(input("Enter marks: "))

    if marks < 0 or marks > 100:
        raise ValueError

    if marks >= 50:
        print("Pass")
    else:
        print("Fail")

except ValueError:
    print("Invalid marks! Enter between 0 and 100")
