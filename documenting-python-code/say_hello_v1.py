def say_hello(name):
    print(f"Hello {name}, is it me you're looking for?")


say_hello.__doc__ = "A simple function that says hello... Richie style"

if __name__ == "__main__":
    help(say_hello)
