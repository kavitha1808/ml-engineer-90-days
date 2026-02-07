# Day 5: Tuples, Sets, List vs Tuple vs Set
# Practice Questions + Solutions
# No functions used

print("DAY 5 PRACTICE\n")

# -------------------------------
# TUPLES
# -------------------------------

print("TUPLES")

# Q1: Create tuple and print first & last element
nums = (10, 20, 30, 40, 50)
print(nums[0])
print(nums[-1])

# Q2: Check if element exists
t = (5, 8, 12, 20)
print(12 in t)

# Q3: Count occurrences
t2 = (1, 2, 2, 3, 2, 4)
print(t2.count(2))

# Q4: Swap using tuple
a = 5
b = 10
a, b = b, a
print(a, b)

print("\n-------------------------------")

# -------------------------------
# SETS
# -------------------------------

print("SETS")

# Q5: Remove duplicates from list
nums_list = [1, 2, 2, 3, 4, 4, 5]
unique_nums = list(set(nums_list))
print(unique_nums)

# Q6: Add and remove elements
s = {10, 20, 30}
s.add(40)
s.remove(20)
print(s)

# Q7: Membership check
check_set = {5, 10, 15}
print(10 in check_set)

# Q8: Common elements between lists
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
common = set(a) & set(b)
print(common)

print("\n-------------------------------")

# -------------------------------
# LIST vs TUPLE vs SET
# -------------------------------

print("LIST vs TUPLE vs SET")

data = [1, 2, 2, 3]
print(data)
print(tuple(data))
print(set(data))

print("\n-------------------------------")

