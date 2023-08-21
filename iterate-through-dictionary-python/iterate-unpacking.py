fruits = {"apple": 0.40, "orange": 0.35}
vegetables = {"pepper": 0.20, "onion": 0.55}

for product, price in {**fruits, **vegetables}.items():
    print(product, "->", price)
