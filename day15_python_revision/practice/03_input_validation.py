"""
Validating user input properly
Engineering mindset example
"""

def get_valid_mark() -> int:
    while True:
        try:
            mark = int(input("Enter mark (0–100): "))
            if 0 <= mark <= 100:
                return mark
            else:
                print("Mark must be between 0 and 100")
        except ValueError:
            print("Invalid input. Enter a number.")


def main():
    mark = get_valid_mark()
    print("Valid mark entered:", mark)


if __name__ == "__main__":
    main()
