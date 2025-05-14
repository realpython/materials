bases = ["plain", "chocolate", "blueberry"]
toppings = ["honey", "whipped cream", "alien syrup"]
pancake_stacks = []
for base in bases:
    for topping in toppings:
        pancake_stacks.append(f"{base.capitalize()} pancake with {topping}")

print(pancake_stacks)
