x = 20


def f():
    x = 40
    print(x)


f()
print(x)


fruits = ["apple", "banana", "cherry", "mango"]


def f():
    fruits[1] = "peach"


f()
print(fruits)


fruits = ["apple", "banana", "cherry", "mango"]


def f():
    fruits = ["grapes", "orange"]  # noqa


f()
print(fruits)
