import _c_function

if __name__ == "__main__":
    # sample data for our call:
    x, y = 6, 2.3

    answer = _c_function.c_function(x, y)
    print(f"    In Python: int: {x} float {y:.1f} return val {answer:.1f}")
