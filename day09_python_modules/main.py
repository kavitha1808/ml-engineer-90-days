from utils.math_utils import add, subtract, multiply, divide
from utils.string_utils import reverse_string, word_count

def main():
    # Math utilities
    print("Math Operations")
    print("Add:", add(10, 5))
    print("Subtract:", subtract(10, 5))
    print("Multiply:", multiply(4, 3))
    print("Divide:", divide(10, 2))

    print("\nString Operations")
    text = "Python modules are powerful"
    print("Original:", text)
    print("Reversed:", reverse_string(text))
    print("Word Count:", word_count(text))


if __name__ == "__main__":
    main()
