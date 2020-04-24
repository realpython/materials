"""
pyeval_operand.py - implements an operand class for use by the evaluator

AUTHOR: Jon Fincher
"""


class Operand:
    """
    Common operator class used by the evaluator.
    """

    def __init__(self, operand_string):
        """ Create a new operator object. """

        # String to hold the operand literal
        self.op_string = operand_string

        # Integer value of the operand
        self.op_value = int(operand_string)
