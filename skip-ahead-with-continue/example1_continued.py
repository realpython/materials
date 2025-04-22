total = 0

for number in range(-10, 10):
    if number < 0:
        continue
    total += number

print(total)
