incomes = {"apple": 5600.00, "orange": 3500.00, "banana": 5000.00}

{fruit: incomes[fruit] for fruit in sorted(incomes)}

{
    fruit: income
    for fruit, income in sorted(incomes.items(), key=lambda item: item[1])
}
