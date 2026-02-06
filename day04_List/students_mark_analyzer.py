marks = [78, 45, 89, 32, 56, 40, 90]

total = 0
passed = []

highest = marks[0]
lowest = marks[0]

for m in marks:
    total += m

    if m >= 40:
        passed.append(m)

    if m > highest:
        highest = m
    if m < lowest:
        lowest = m

average = total / len(marks)

print("Total Marks:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
print("Passed Students Marks:", passed)
