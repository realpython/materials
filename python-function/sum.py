def sum_numbers(*numbers, precision=2):
    return round(sum(numbers), precision)


print(sum_numbers(1.3467, 2.5243, precision=3))
print(sum_numbers(1.3467, 2.5243, 3))
