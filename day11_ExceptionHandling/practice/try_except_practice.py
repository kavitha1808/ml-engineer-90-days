# Demonstrates basic try-except with multiple test cases

while True:
    try:
        num = int(input("Enter a number (0 to exit): "))

        if num == 0:
            print("Exiting program")
            break

        result = 100 / num
        print("Result:", result)

    except ValueError:
        print("ERROR: Please enter a valid integer")

    except ZeroDivisionError:
        print("ERROR: Division by zero is not allowed")

    finally:
        print("Iteration completed\n")
