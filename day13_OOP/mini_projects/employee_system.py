class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def give_increment(self, percentage):
        increment = self.salary * (percentage / 100)
        self.salary += increment
        print(f"Incremented salary by {percentage}%")

    def annual_salary(self):
        return self.salary * 12

    def display_employee(self):
        print("\n--- Employee Details ---")
        print("ID:", self.emp_id)
        print("Name:", self.name)
        print("Monthly Salary:", self.salary)
        print("Annual Salary:", self.annual_salary())


# Driver code
emp1 = Employee(101, "Kavitha", 45000)
emp1.give_increment(10)
emp1.display_employee()
