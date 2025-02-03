# def outer_func():
#     name = "Pythonista"

#     def inner_func():
#         print(f"Hello, {name}!")

#     return inner_func


def outer_func():
    name = "Pythonista"
    return lambda: print(f"Hello, {name}!")


inner_func = outer_func()
inner_func()
