import numpy as np

# Problem 1: Create & Inspect Array
arr = np.arange(1, 11)
print("Array:", arr)
print("Shape:", arr.shape)
print("Dimensions:", arr.ndim)
print("Data Type:", arr.dtype)

# Problem 2: Even Number Extraction
arr2 = np.array([12, 5, 8, 19, 30, 42, 7])
even_numbers = arr2[arr2 % 2 == 0]
print("\nEven Numbers:", even_numbers)

# Problem 3: Array Arithmetic
a = np.array([2, 4, 6])
b = np.array([1, 3, 5])

print("\nAddition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

# Problem 4: Statistics
marks = np.array([78, 85, 62, 90, 55])
print("\nMean:", np.mean(marks))
print("Max:", np.max(marks))
print("Min:", np.min(marks))
print("Standard Deviation:", np.std(marks))
