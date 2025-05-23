required_ingredients = {"cheese", "eggs", "milk"}
available_ingredients = {"cheese", "eggs", "milk", "sugar", "salt"}

print(required_ingredients <= available_ingredients)
print(required_ingredients.issubset(available_ingredients))

a = {1, 2, 3, 4, 5}
print(a <= a)
print(a.issubset(a))
