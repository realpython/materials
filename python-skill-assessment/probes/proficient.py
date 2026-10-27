def shout(func):
    def wrapper(name):
        return func(name).upper() + "!"

    return wrapper


@shout
def greet(name):
    return f"hello, {name}"


print(greet("ada"))
print(greet.__name__)
