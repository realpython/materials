numbers = [1, 3, 5, 7, 9]
target = 42

for number in numbers:
    print(f"Processing {number}...")
    if number == target:
        print(f"Target found {target}!")
        break
else:
    print(f"Target no found {target}")
