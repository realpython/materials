fruits = {"apple": 0.40, "orange": 0.35, "banana": 0.25}

for fruit, price in fruits.items():
    fruits[fruit] = round(price * 0.9, 2)
