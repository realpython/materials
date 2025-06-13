def create_lazy_name():
    global number  # Create a global name lazily
    number = 42
    return number


create_lazy_name()
print(number)
