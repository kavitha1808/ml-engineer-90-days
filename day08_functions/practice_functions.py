"""
Day 08 – Functions Practice (Complete)

Topics covered:
- Functions basics
- Parameters vs arguments
- Default arguments
- Return vs print
- Local vs global scope
- Logic traps
- Real-world style function usage
"""

# --------------------------------------------------
# 1. Basic function
# --------------------------------------------------

def greet():
    print("Hello, welcome to Python")

greet()


# --------------------------------------------------
# 2. Parameters vs Arguments
# --------------------------------------------------

def add(a, b):   # a, b -> parameters
    return a + b

print(add(10, 20))   # 10, 20 -> arguments


# --------------------------------------------------
# 3. Default Arguments
# --------------------------------------------------

def power(base, exp=2):
    return base ** exp

print(power(3))
print(power(3, 3))


# --------------------------------------------------
# 4. Missing Argument Error (commented on purpose)
# --------------------------------------------------

# def subtract(a, b):
#     return a - b
# subtract(5)   # TypeError


# --------------------------------------------------
# 5. Return vs Print
# --------------------------------------------------

def multiply(a, b):
    print(a * b)

result = multiply(2, 3)
print(result)   # None


# --------------------------------------------------
# 6. Local Scope
# --------------------------------------------------

def local_test():
    x = 10
    print("Inside function:", x)

local_test()
# print(x)  # NameError


# --------------------------------------------------
# 7. Local vs Global
# --------------------------------------------------

x = 50

def change_local():
    x = 100
    print("Inside:", x)

change_local()
print("Outside:", x)


# --------------------------------------------------
# 8. Global Keyword
# --------------------------------------------------

count = 0

def increment():
    global count
    count += 1

increment()
increment()
print("Count:", count)


# --------------------------------------------------
# 9. Return stops execution
# --------------------------------------------------

def demo():
    print("A")
    return
    print("B")

demo()


# --------------------------------------------------
# 10. Loop with return (logic trap)
# --------------------------------------------------

def first_number():
    for i in range(5):
        return i

print(first_number())


# --------------------------------------------------
# 11. Default argument trap (mutable)
# --------------------------------------------------

def add_item(item, box=[]):
    box.append(item)
    return box

print(add_item(1))
print(add_item(2))
print(add_item(3))


# --------------------------------------------------
# 12. Correct way to handle default list
# --------------------------------------------------

def safe_add_item(item, box=None):
    if box is None:
        box = []
    box.append(item)
    return box

print(safe_add_item(1))
print(safe_add_item(2))


# --------------------------------------------------
# 13. Modify global list without global keyword
# --------------------------------------------------

nums = [1, 2, 3]

def modify_list():
    nums.append(4)

modify_list()
print(nums)


# --------------------------------------------------
# 14. Real-world style: Salary calculation
# --------------------------------------------------

def calculate_tax(income):
    if income > 50000:
        return income * 0.1
    return 0

def final_salary(income):
    return income - calculate_tax(income)

print(final_salary(60000))


# --------------------------------------------------
# 15. Mini logic check (final boss)
# --------------------------------------------------

x = 1

def outer():
    x = 2
    def inner():
        global x
        x = 3
    inner()
    print("Inside outer:", x)

outer()
print("Global x:", x)
