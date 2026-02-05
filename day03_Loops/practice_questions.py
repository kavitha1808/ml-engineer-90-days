# Q1: Print numbers from 0 to 9
for i in range(10):
    print(i)


# Q2: Print numbers from 10 to 1
for i in range(10, 0, -1):
    print(i)


# Q3: Print even numbers between 1 and 50
for i in range(2, 51, 2):
    print(i)


# Q4: Output of range(1, 10, 3)
for i in range(1, 10, 3):
    print(i)
# Output: 1 4 7


# Q5: Print 2 4 6 8 10
for i in range(2, 11, 2):
    print(i)


# Q6: Print 1 to 5 using while
i = 1
while i <= 5:
    print(i)
    i += 1


# Q7: Infinite loop example (commented to avoid freeze)
# i = 1
# while i <= 5:
#     print(i)


# Q8: Print 5 to 1 using while
i = 5
while i >= 1:
    print(i)
    i -= 1


# Q9: Print numbers until >100 (start 10, step 10)
i = 10
while i <= 100:
    print(i)
    i += 10


# Q10: Stop loop when number becomes 6
for i in range(1, 11):
    if i == 6:
        break
    print(i)


# Q11: break output
for i in range(5):
    if i == 3:
        break
    print(i)
# Output: 0 1 2


# Q12: Search for 7 in list
nums = [1, 4, 6, 7, 9]
for n in nums:
    if n == 7:
        print("Found")
        break


# Q13: Skip number 5
for i in range(1, 11):
    if i == 5:
        continue
    print(i)


# Q14: Odd numbers output
for i in range(1, 6):
    if i % 2 == 0:
        continue
    print(i)
# Output: 1 3 5


# Q15: Skip even numbers
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)


# Q16: Empty loop using pass
for i in range(5):
    pass


# Q17: pass explanation example
for i in range(3):
    pass


# Q18: continue skips print("Hello")
for i in range(3):
    print(i)
    continue
    print("Hello")


# Q19: break inside while
i = 0
while i < 3:
    print(i)
    i += 1
    break
# Output: 0


# Q20: Infinite loop using pass (commented)
# while True:
#     pass


# Q21: break vs continue vs pass demo
for i in range(5):
    if i == 1:
        continue
    if i == 3:
        break
    pass
    print(i)


# Q22: Stop at first even number
for i in range(1, 11):
    if i % 2 == 0:
        break
    print(i)


# Q23: Skip numbers divisible by 3
for i in range(1, 16):
    if i % 3 == 0:
        continue
    print(i)
