def decorator(function):
    def closure():
        print("Doing something before calling the function.")
        function()
        print("Doing something after calling the function.")

    return closure


@decorator
def greet():
    print("Hi, Pythonista!")
