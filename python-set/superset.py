required_ingredients = {"cheese", "eggs", "milk"}
available_ingredients = {"cheese", "eggs", "milk", "sugar", "salt"}

print(available_ingredients >= required_ingredients)
print(available_ingredients.issubset(required_ingredients))

a = {1, 2, 3, 4, 5}
print(a.issuperset(a))
print(a >= a)
