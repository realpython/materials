def calculate(x, y, *, operator):
    if operator == "+":
        return x + y
    elif operator == "-":
        return x - y
    elif operator == "*":
        return x * y
    elif operator == "/":
        return x / y
    else:
        raise ValueError("invalid operator")


calculate(3, 4, operator="+")
calculate(3, 4, operator="-")
calculate(3, 4, operator="*")
calculate(3, 4, operator="/")
