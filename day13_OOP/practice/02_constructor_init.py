class MobilePhone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_details(self):
        print("\n--- Mobile Details ---")
        print("Brand :", self.brand)
        print("Model :", self.model)
        print("Price :", self.price)


phone1 = MobilePhone("Samsung", "S23", 75000)
phone2 = MobilePhone("Apple", "iPhone 14", 90000)

phone1.display_details()
phone2.display_details()
