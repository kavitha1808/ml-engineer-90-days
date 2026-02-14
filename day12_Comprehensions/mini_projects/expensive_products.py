products = {
    "Pen": 20,
    "Bag": 900,
    "Bottle": 250,
    "Headphones": 1500
}

expensive = {item: price for item, price in products.items() if price > 500}
print(expensive)
