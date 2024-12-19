numbers = [1, 3, 5, 7, 9]
target = 5
for number in numbers:
    print(f"Processing {number}...")
    if number == target:
        print(f"Target found {target}!")
        break

numbers = [1, 2, 3, 4, 5, 6]
for number in numbers:
    print(f"{number = }")
    if number % 2 != 0:
        continue
    print(f"{number} is even!")
