# def function(x, y, z):
#     print(f"{x = }")
#     print(f"{y = }")
#     print(f"{z = }")


# numbers = [1, 2, 3]

# function(*numbers)


# def function(one, two, three):
#     print(f"{one = }")
#     print(f"{two = }")
#     print(f"{three = }")


# numbers = {"one": 1, "two": 2, "three": 3}
# function(**numbers)


def function(**kwargs):
    for key, value in kwargs.items():
        print(key, "->", value)


numbers = {"one": 1, "two": 2, "three": 3}
letters = {"a": "A", "b": "B", "c": "C"}

function(**numbers, **letters)
