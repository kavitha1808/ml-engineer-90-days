"""
Single Responsibility Principle example
Each function does only one task
"""

def add(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    return a - b


def multiply(a: int, b: int) -> int:
    return a * b


def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Division by zero not allowed")
    return a / b


def main():
    print("Addition:", add(10, 5))
    print("Subtraction:", subtract(10, 5))
    print("Multiplication:", multiply(10, 5))
    print("Division:", divide(10, 5))


if __name__ == "__main__":
    main()
