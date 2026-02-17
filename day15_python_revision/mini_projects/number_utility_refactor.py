"""
Refactored Number Utility Program
Engineering-style clean code
"""

def is_even(number: int) -> bool:
    return number % 2 == 0


def is_positive(number: int) -> bool:
    return number > 0


def main():
    number = int(input("Enter a number: "))

    print("Even:", is_even(number))
    print("Positive:", is_positive(number))


if __name__ == "__main__":
    main()
