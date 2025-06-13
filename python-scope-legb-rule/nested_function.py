def outer_func():
    variable = 100

    def inner_func():
        print(f"Printing variable from inner_func(): {variable}")

    inner_func()
    print(f"Printing variable from outer_func(): {variable}")


outer_func()
