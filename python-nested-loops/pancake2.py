bases = ["plain", "chocolate", "blueberry"]
toppings = ["honey", "whipped cream", "alien syrup"]
pancake_stacks = [
    f"{base.capitalize()} pancake with {topping}"
    for base in bases
    for topping in toppings
]
print(pancake_stacks)
