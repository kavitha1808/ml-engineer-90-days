class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} vehicle started")


class Car(Vehicle):
    def __init__(self, brand, seats):
        super().__init__(brand)
        self.seats = seats

    def details(self):
        print(f"Brand: {self.brand}, Seats: {self.seats}")


car = Car("Toyota", 5)
car.start()
car.details()
