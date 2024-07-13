def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


def say_whee():
    print("Whee!")


say_whee = decorator(say_whee)


@decorator
def say_whee2():
    print("Whee!")


if __name__ == "__main__":
    say_whee()
    say_whee2()
