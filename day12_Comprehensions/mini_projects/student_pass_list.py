students = {
    "Arun": 78,
    "Bala": 45,
    "Chitra": 89,
    "Divya": 50
}

passed = [name for name, mark in students.items() if mark >= 50]

print("Passed Students:", passed)
