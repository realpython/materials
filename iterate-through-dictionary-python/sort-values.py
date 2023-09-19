incomes = {"apple": 5600.00, "orange": 3500.00, "banana": 5000.00}

for key, value in sorted(incomes.items(), key=lambda item: item[1]):
    print(key, "->", value)
