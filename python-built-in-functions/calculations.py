functions = [
    "def add(a, b): return a + b",
    "def subtract(a, b): return a - b",
    "def multiply(a, b): return a * b",
    "def divide(a, b): return a / b",
]


for function in functions:
    exec(function)


# Uncomment the following lines
# print(add(1, 2))
# print(subtract(3, 2))
# print(multiply(2, 3))
# print(divide(6, 3))
