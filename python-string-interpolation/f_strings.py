import math

name = "Pythonista"
day = "Friday"  # Of course 😃
print(f"Hello, {name}! Today is {day}.")

x = 5
y = 10
print(f"The sum of {x} and {y} is {x + y}.")


radius = 16
print(f"The area of your circle is {math.pi * radius ** 2}")

name = "Pythonista"
site = "real python"
print(f"Hello, {name.upper()}! Welcome to {site.title()}!")
print(f"{[2**n for n in range(3, 9)]}")

print(f"The number is {42}")
print(f"Pi {3.14}")

value = "Suspicious value"
print(f"{value = }")
print(f"{2 + 3 = }")

numbers = {"one": 1, "two": 2, "three": 3}
print(f"{numbers['one']}-{numbers['two']}-{numbers['three']}")
