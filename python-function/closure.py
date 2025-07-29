def function():
    value = 42

    def closure():
        print(f"The value is: {value}!")

    return closure


reveal_number = function()
reveal_number()
