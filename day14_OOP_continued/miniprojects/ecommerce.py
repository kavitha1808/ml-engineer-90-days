class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.__stock = stock

    def reduce_stock(self, qty):
        if qty <= self.__stock:
            self.__stock -= qty
            return True
        return False


class Order:
    def __init__(self):
        self.items = {}

    def add_product(self, product, qty):
        if product.reduce_stock(qty):
            self.items[product.name] = qty


p = Product("Laptop", 50000, 5)
o = Order()
o.add_product(p, 2)
print(o.items)
