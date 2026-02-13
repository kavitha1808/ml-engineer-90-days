while True:
    try:
        num = int(input("Enter a number (0 to exit): "))

        if num == 0:
            print("Exiting program")
            break

        result = 100 / num
        print("Result:", result)

    except ValueError:
        print("ERROR: Invalid input")

    except ZeroDivisionError:
        print("ERROR: Division by zero")

    finally:
        print("Execution cycle completed\n")
