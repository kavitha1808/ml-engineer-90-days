def calculate_tax(income):
    if income > 50000:
        return income * 0.1
    return 0

def calculate_salary(income):
    tax = calculate_tax(income)
    return income - tax

def print_summary(income):
    tax = calculate_tax(income)
    salary = calculate_salary(income)

    print("Income:", income)
    print("Tax:", tax)
    print("Final Salary:", salary)

print_summary(60000)
