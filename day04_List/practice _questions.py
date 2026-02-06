# Day 04 – Practice Questions (Lists)
# All solutions in a single file

# --------------------------------------------------
# 1. Sum of all elements in a list
# --------------------------------------------------
nums = [10, 20, 30, 40]

total = 0
for n in nums:
    total += n

print("1. Sum of elements:", total)


# --------------------------------------------------
# 2. Find maximum and minimum (without max/min)
# --------------------------------------------------
nums = [45, 12, 89, 34, 7]

maximum = nums[0]
minimum = nums[0]

for n in nums:
    if n > maximum:
        maximum = n
    if n < minimum:
        minimum = n

print("2. Maximum:", maximum)
print("   Minimum:", minimum)


# --------------------------------------------------
# 3. Reverse a list (without using reverse())
# --------------------------------------------------
nums = [1, 2, 3, 4, 5]
reversed_list = []

for i in range(len(nums) - 1, -1, -1):
    reversed_list.append(nums[i])

print("3. Reversed list:", reversed_list)


# --------------------------------------------------
# 4. Count even numbers in a list
# --------------------------------------------------
nums = [1, 2, 3, 4, 6, 9]
even_count = 0

for n in nums:
    if n % 2 == 0:
        even_count += 1

print("4. Even numbers count:", even_count)


# --------------------------------------------------
# 5. Remove duplicates from a list
# --------------------------------------------------
nums = [1, 2, 2, 3, 4, 4, 5]
unique = []

for n in nums:
    if n not in unique:
        unique.append(n)

print("5. List without duplicates:", unique)


# --------------------------------------------------
# 6. Find second largest element
# --------------------------------------------------
nums = [10, 45, 23, 89, 67]

largest = second_largest = float('-inf')

for n in nums:
    if n > largest:
        second_largest = largest
        largest = n
    elif n > second_largest and n != largest:
        second_largest = n

print("6. Second largest element:", second_largest)


# --------------------------------------------------
# 7. Check if a list is sorted
# --------------------------------------------------
nums = [10, 20, 30, 40]
is_sorted = True

for i in range(len(nums) - 1):
    if nums[i] > nums[i + 1]:
        is_sorted = False
        break

print("7. Is the list sorted?", is_sorted)


# --------------------------------------------------
# 8. Rotate list by k positions (right rotation)
# --------------------------------------------------
nums = [1, 2, 3, 4, 5]
k = 2

k = k % len(nums)
rotated_list = nums[-k:] + nums[:-k]

print("8. Rotated list by", k, "positions:", rotated_list)
