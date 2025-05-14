numbers = [1, 3, 5, 9]

target = 7
for number in numbers:
    if number == target:
        print("Found!")
        break
else:
    print("Not found.")

target = 3
for number in numbers:
    if number == target:
        print("Found!")
        break
else:
    print("Not found.")
