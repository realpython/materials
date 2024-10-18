def function():
    value = 42
    return value


# Global scope
global_variable = "global"


def outer_func():
    # Nonlocal scope
    nonlocal_variable = "nonlocal"

    def inner_func():
        # Local scope
        local_variable = "local"
        print(f"Hi from the '{local_variable}' scope!")
        print(f"Hi from the '{nonlocal_variable}' scope!")
        print(f"Hi from the '{global_variable}' scope!")

    inner_func()


outer_func()
