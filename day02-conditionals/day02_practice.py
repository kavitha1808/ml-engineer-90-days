"""
Day 2 – Conditional Statements & Logical Operators
All Practice Questions Solutions

Concepts:
- if, elif, else
- comparison operators
- logical operators (and, or, not)
- control flow
"""

# ---------- Level 1 (Basic) ----------

# Positive, Negative or Zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Voting eligibility
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# Larger of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Larger:", a)
elif b > a:
    print("Larger:", b)
else:
    print("Both are equal")


# ---------- Level 2 (Logic) ----------

# Divisible by 3 and 5
num = int(input("Enter number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by 3 and 5")
else:
    print("Not divisible by both")

# Leap year check
year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

# Grade calculation
marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# ---------- Level 3 (Thinking) ----------

# Number between 10 and 50
num = int(input("Enter number: "))
if 10 <= num <= 50:
    print("Between 10 and 50")
else:
    print("Outside range")

# Username & password validation
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")

# Discount calculation
price = float(input("Enter price: "))
if price >= 5000:
    discount = 20
elif price >= 3000:
    discount = 10
else:
    discount = 0
print("Discount:", discount, "%")


# ---------- Warm-up ----------

# Even or odd
num = int(input("Enter number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Multiple of 10
num = int(input("Enter number: "))
if num % 10 == 0:
    print("Multiple of 10")
else:
    print("Not a multiple of 10")

# Largest of three numbers
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)

# Senior citizen check
age = int(input("Enter age: "))
if age >= 60:
    print("Senior citizen")
else:
    print("Not a senior citizen")

# Temperature classification
temp = float(input("Enter temperature: "))
if temp < 0:
    print("Freezing")
elif temp <= 30:
    print("Normal")
else:
    print("Hot")


# ---------- Logic Building ----------

# Vowel or consonant
ch = input("Enter character: ").lower()
if ch in "aeiou":
    print("Vowel")
else:
    print("Consonant")

# Two-digit number
num = int(input("Enter number: "))
if 10 <= abs(num) <= 99:
    print("Two-digit number")
else:
    print("Not a two-digit number")

# 21st century check
year = int(input("Enter year: "))
if 2001 <= year <= 2100:
    print("21st century")
else:
    print("Not 21st century")

# Pass / Fail / Distinction
score = int(input("Enter score: "))
if score >= 75:
    print("Distinction")
elif score >= 40:
    print("Pass")
else:
    print("Fail")

# Divisible by 4 or 6 but not both
num = int(input("Enter number: "))
if (num % 4 == 0) ^ (num % 6 == 0):
    print("Divisible by 4 or 6 but not both")
else:
    print("Condition not satisfied")


# ---------- Engineer Thinking ----------

# Password validation
password = input("Enter password: ")
has_digit = False
for ch in password:
    if ch.isdigit():
        has_digit = True
        break

if len(password) >= 8 and has_digit:
    print("Valid password")
else:
    print("Invalid password")

# Triangle validity (sides)
a = float(input("Enter side1: "))
b = float(input("Enter side2: "))
c = float(input("Enter side3: "))
if a + b > c and a + c > b and b + c > a:
    print("Valid triangle")
else:
    print("Invalid triangle")

# Electricity bill
units = int(input("Enter units: "))
if units <= 100:
    bill = 0
elif units <= 300:
    bill = (units - 100) * 5
else:
    bill = (200 * 5) + (units - 300) * 8
print("Bill: ₹", bill)

# Loan eligibility
age = int(input("Enter age: "))
salary = int(input("Enter salary: "))
loan = input("Existing loan (yes/no): ").lower()
if age >= 21 and salary >= 25000 and loan == "no":
    print("Loan approved")
else:
    print("Loan not approved")

# Traffic signal
signal = input("Enter signal: ").lower()
if signal == "red":
    print("Stop")
elif signal == "yellow":
    print("Ready")
elif signal == "green":
    print("Go")
else:
    print("Invalid signal")


# ---------- Interview Style ----------

# Triangle validity (angles)
x = int(input("Angle 1: "))
y = int(input("Angle 2: "))
z = int(input("Angle 3: "))
if x > 0 and y > 0 and z > 0 and (x + y + z == 180):
    print("Valid triangle")
else:
    print("Invalid triangle")

# Outside range 20–80
num = int(input("Enter number: "))
if num < 20 or num > 80:
    print("Outside range")
else:
    print("Inside range")

# Bonus calculation
exp = int(input("Years of experience: "))
if exp >= 5:
    print("Bonus: 20%")
elif exp >= 3:
    print("Bonus: 10%")
else:
    print("No bonus")

# Character type
ch = input("Enter character: ")
if ch.isupper():
    print("Uppercase")
elif ch.islower():
    print("Lowercase")
elif ch.isdigit():
    print("Digit")
else:
    print("Special character")

# Weekday or weekend
day = int(input("Enter day number (1–7): "))
if day == 6 or day == 7:
    print("Weekend")
elif 1 <= day <= 5:
    print("Weekday")
else:
    print("Invalid day")
