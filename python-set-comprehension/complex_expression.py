numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print({number**2 if number % 2 == 0 else number**3 for number in numbers})

result_set = set()
for number in numbers:
    if number % 2 == 0:
        value = number**2
    else:
        value = number**3
    result_set.add(value)

print(result_set)
