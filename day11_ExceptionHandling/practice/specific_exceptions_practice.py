# Handling different exceptions separately

data = [10, 20, 30]
student = {"name": "Alice", "marks": 85}

try:
    index = int(input("Enter index (0-2): "))
    print("List value:", data[index])

    key = input("Enter dictionary key: ")
    print("Dictionary value:", student[key])

except IndexError:
    print("ERROR: List index out of range")

except KeyError:
    print("ERROR: Key does not exist in dictionary")

except ValueError:
    print("ERROR: Invalid numeric input")

print("Program ended safely")
