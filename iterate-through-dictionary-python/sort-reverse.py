incomes = {"apple": 5600.00, "orange": 3500.00, "banana": 5000.00}

for fruit in sorted(incomes, reverse=True):
    print(fruit, "->", incomes[fruit])
