def add_messages(func):
    def _add_messages():
        print("This is my first decorator")
        func()
        print("Bye!")

    return _add_messages


@add_messages
def greet():
    print("Hello, World!")


greet()
