class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price, quantity=1):
        if name in self.items:
            self.items[name]["quantity"] += quantity
        else:
            self.items[name] = {
                "price": price,
                "quantity": quantity
            }
        print(f"Added {name} to cart")

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
            print(f"Removed {name}")
        else:
            print("Item not found")

    def calculate_total(self):
        total = 0
        for item in self.items.values():
            total += item["price"] * item["quantity"]
        return total

    def display_cart(self):
        print("\n--- Shopping Cart ---")
        for name, details in self.items.items():
            print(f"{name} - ₹{details['price']} x {details['quantity']}")
        print("Total Amount: ₹", self.calculate_total())


# Driver code
cart = ShoppingCart()
cart.add_item("Laptop", 55000)
cart.add_item("Mouse", 500, 2)
cart.add_item("Keyboard", 1200)
cart.display_cart()
