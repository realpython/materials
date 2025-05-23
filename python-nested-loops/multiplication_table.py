for multiplicant in range(1, 11):
    for multiplier in range(1, 4):
        expression = f"{multiplicant:>2d} × {multiplier}"
        product = multiplicant * multiplier
        print(f"{expression} = {product:>2d}", end="\t")
    print()
