"""
operand.py - implements an operand class for use by the evaluator

AUTHOR: Jon Fincher
"""

class Operand:
    """
    Common operator class used by the evaluator.
    """

    op_string = ""      # String to hold the operand literal
    op_value = 0        # Integer value of the operand

    def __init__(self, operand_string):
        """ Create a new operator object. """
        self.op_string = operand_string
        self.op_value = int(operand_string)
