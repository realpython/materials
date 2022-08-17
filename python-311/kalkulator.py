import operator

import parse

OPERATIONS = {
    "pluss": operator.add,  # Addition
    "minus": operator.sub,  # Subtraction
    "ganger": operator.mul,  # Multiplication
    "delt på": operator.truediv,  # Division
}
EXPRESSION = parse.compile("{operand1:g} {operation} {operand2:g}")


def calculate(text):
    if (ops := EXPRESSION.parse(text)) and ops["operation"] in OPERATIONS:
        operation = OPERATIONS[ops["operation"]]
        return operator.call(operation, ops["operand1"], ops["operand2"])


if __name__ == "__main__":
    for calculation in [
        "20 pluss 22",
        "2022 minus 1991",
        "45 ganger 45",
        "11 delt på 3",
    ]:
        print(f"{calculation} = {calculate(calculation)}")
