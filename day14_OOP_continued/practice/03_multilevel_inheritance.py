class Person:
    def __init__(self, name):
        self.name = name


class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id


class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Department: {self.department}")


mgr = Manager("Anita", 101, "IT")
mgr.show_details()
