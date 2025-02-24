for number in range(1, 11):
    for product in range(number, number * 11, number):
        print(f"{product:>4d}", end="")
    print()
