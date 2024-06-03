functions = [
    "def add(a, b): return a + b",
    "def subtract(a, b): return a - b",
    "def multiply(a, b): return a * b",
    "def divide(a, b): return a / b",
]


for function in functions:
    exec(function)


add(1, 2)
subtract(3, 2)
multiply(2, 3)
divide(6, 3)
