while True:
    try:
        num = int(input("Enter a number (0 to exit): "))

        if num == 0:
            print("Exiting program")
            break

        result = 100 / num

    except ValueError:
        print("ERROR: Please enter a valid integer")

    except ZeroDivisionError:
        print("ERROR: Division by zero is not allowed")

    else:
        print("Calculation successful")
        print("Result:", result)

    print("Iteration completed\n")
