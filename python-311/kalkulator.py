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
