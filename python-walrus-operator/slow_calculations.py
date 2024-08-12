numbers = [7, 6, 1, 4, 1, 8, 0, 6]


def slow(number):
    print(f"Slowly calculating {number} - 2 = {number - 2}")
    return number - 2


print("\nList Comprehension:")
results = [slow(num) for num in numbers if slow(num) > 0]
print(results)

print("\nLoop")
results = []
for num in numbers:
    value = slow(num)
    if value > 0:
        results.append(value)
print(results)

print("\nfilter()")
results = list(filter(lambda value: value > 0, (slow(num) for num in numbers)))
print(results)

print("\nDouble List Comprehension")
results = [value for num in numbers for value in [slow(num)] if value > 0]
print(results)

print("\nList Comprehension with Walrus Operator")
results = [value for num in numbers if (value := slow(num)) > 0]
print(results)
