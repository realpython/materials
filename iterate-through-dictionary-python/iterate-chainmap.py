from collections import ChainMap

fruits = {"apple": 0.40, "orange": 0.35}
vegetables = {"pepper": 0.20, "onion": 0.55}
inventory = ChainMap(fruits, vegetables)

for product, price in inventory.items():
    print(product, "->", price)
