def greet(name, verbose=False):
    if verbose:
        print(f"Hello, {name}! It's great to see you!")
    else:
        print(f"Hello, {name}!")


greet("Pythonista")
greet("Pythonista", verbose=True)
