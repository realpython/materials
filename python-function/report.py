def report(**kwargs):
    print("Report:")
    for key, value in kwargs.items():
        print(f" - {key.capitalize()}: {value}")


report(
    name="Keyboard",
    price=19.99,
    quantity=5,
    category="PC Components",
)
