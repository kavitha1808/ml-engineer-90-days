# list_methods.py
# Demonstrates common list methods

nums = [10, 20, 30]

# Add elements
nums.append(40)
nums.insert(1, 15)
nums.extend([50, 60])

print("After adding elements:", nums)

# Remove elements
nums.remove(15)     # removes value
nums.pop()          # removes last element
nums.pop(0)         # removes first element

print("After removing elements:", nums)

# Other methods
nums.sort()
print("Sorted list:", nums)

nums.reverse()
print("Reversed list:", nums)

print("Count of 20:", nums.count(20))
print("Index of 30:", nums.index(30))
print("Length of list:", len(nums))
