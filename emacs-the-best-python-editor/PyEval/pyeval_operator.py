"""
pyeval_operator.py - implements an operator class for use by the evaluator

AUTHOR: Jon Fincher
"""

# Dictionary lookup for precedence
# Currently four levels of precedence
PRECEDENCE = {
    "+": 2,  # Addition
    "-": 2,  # Subtraction
    "*": 3,  # Multiplication
    "/": 3,  # Division
    "%": 3,  # Modulo
    "^": 4,  # Power
}

# Dictionary lookup for number of operands to use
OPERAND_COUNT = {
    "+": 2,  # Addition
    "-": 2,  # Subtraction
    "*": 2,  # Multiplication
    "/": 2,  # Division
    "%": 2,  # Modulo
    "^": 2,  # Power
}


class Operator:
    """
    Common operator class used by the evaluator.
    """

    def __init__(self, operator_string):
        """ Create a new operator object. """

        # String to hold the operator
        self._op_string = operator_string

        # Integer to hold the precedence
        self._op_prec = PRECEDENCE[operator_string]

        # Integer to hold the number of operands to use
        self._op_cnt = OPERAND_COUNT[operator_string]

    @property
    def op_string(self):
        return self._op_string

    @op_string.setter
    def op_string(self, new_op_string):
        self._op_string = new_op_string
        self._op_prec = PRECEDENCE[self._op_string]
        self._op_cnt = OPERAND_COUNT[self._op_string]

    @property
    def count(self):
        return self._op_cnt

    @property
    def precedence(self):
        return self._op_prec
