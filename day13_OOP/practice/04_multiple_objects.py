class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, percent):
        discount = self.price * (percent / 100)
        self.price -= discount

    def display(self):
        print(self.name, "- ₹", self.price)


products = [
    Product("Laptop", 60000),
    Product("Headphones", 3000),
    Product("Monitor", 12000)
]

for product in products:
    product.apply_discount(10)
    product.display()
