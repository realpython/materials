fruits = {
    "apple": 1.00,
    "banana": 0.50,
    "cherry": 2.00,
}
print({fruit: round(price * 0.95, 2) for fruit, price in fruits.items()})
