# fmt: off

numbers = range(3, 13)
cubes = [
    (number - 3) ** 3 for number in numbers
    if number % 2 == 1
]
# fmt: on

print(cubes)
