monthly_incomes = (
    ("January", 5000),
    ("February", 5500),
    ("March", 6000),
    ("April", 5800),
    ("May", 6200),
    ("June", 7000),
    ("July", 7500),
    ("August", 7300),
    ("September", 6800),
    ("October", 6500),
    ("November", 6000),
    ("December", 5500),
)

total_income = 0
for income in monthly_incomes:
    total_income += income[1]
