inventory = [
    {"product": "Apple", "price": 5.70},
    {"product": "Orange", "price": 4.50},
    {"product": "Banana", "price": 6.00},
    {"product": "Mango", "price": 8.60},
    {"product": "Pepper", "price": 4.20},
    {"product": "Carrot", "price": 3.57},
]
for item in inventory:
    product = item["product"]
    price = item["price"]
    print(f"{product:.<30}${price:.2f}")
