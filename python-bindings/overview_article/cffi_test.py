import _c_function

if __name__ == "__main__":
    # sample data for our call:
    x = 6
    y = 2.3

    c_function = _c_function.lib.c_function
    answer = c_function(x, y)
    print(f"    In Python: int: {x} float {y:.1f} return val {answer:.1f}")
