# looping.py
# Demonstrates looping through lists

nums = [10, 20, 30, 40]

print("Using for loop:")
for n in nums:
    print(n)

print("\nUsing range + index:")
for i in range(len(nums)):
    print(f"Index {i} -> {nums[i]}")

print("\nUsing enumerate (best practice):")
for index, value in enumerate(nums):
    print(index, value)
