fruits = {"apple": 1.0, "banana": 0.5, "cherry": 2.0, "mango": 2.3}
with_discount = ["apple", "cherry"]
print(
    {
        fruit: price * 0.9 if fruit in with_discount else price
        for fruit, price in fruits.items()
    }
)
