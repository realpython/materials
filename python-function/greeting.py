# def greet(name):
#     print(f"Hello, {name}!")


def greet(name, verbose=False):
    if verbose:
        print(f"Hello, {name}! Welcome to Real Python!")
    else:
        print(f"Hello, {name}!")


greet("Pythonista", verbose=True)
greet("Pythonista")
