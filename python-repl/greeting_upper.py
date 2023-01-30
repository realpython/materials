def greet(name="World", upper=False):
    greeting = f"Hello, {name}!"
    if upper:
        greeting = greeting.upper()
    print(greeting)
