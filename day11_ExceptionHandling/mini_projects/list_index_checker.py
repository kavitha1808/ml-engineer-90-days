items = ["apple", "banana", "cherry"]

try:
    index = int(input("Enter index: "))
    print("Item:", items[index])
except IndexError:
    print("Index out of range")
except ValueError:
    print("Enter a valid number")
