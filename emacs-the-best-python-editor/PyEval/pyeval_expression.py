"""
Expression - defines an infix expression

Uses Operator to break the infix expression down, and
outputs an RPN string using the shunting yard approach.
Algorithm outlined at https://en.wikipedia.org/wiki/Shunting-yard_algorithm
"""

from pyeval_operator import Operator


class Expression:
    """
    Defines and parses an infix expression string, returning
    an RPN expression string, or raising an exception if the input string
    is invalid.
    """

    # The _operator_stack variable uses standard Python lists to implement
    # a simple stack. As operators are parsed from the string,
    # they are appended to the stack. As the input string is processed, the
    # grows as needed. In the end, it should be empty.

    _operator_stack = []  # Holds the current stack of operators

    # Store the string, and where we are in our parsing run.
    _expr_string = ""
    _output_string = ""
    _current_position = 0

    # Have we evaluated this expressions yet?
    _evaluated = False

    def __init__(self, expression_string):
        """
        Create a new expression. Does no error checking yet, just sets
        up a new expression and gets us ready to parse.
        """

        # Add '$' as an end of line marker
        self._expr_string = expression_string.strip() + "$"

        # Start parsing at the first character
        self._current_position = 0

        # No output string yet
        self._output_string = ""

        # Clear the stack
        self._operator_stack.clear()

        # Reset the evaluated flag
        self._evaluated = False

    def result(self):
        """
        Returns the result of the evaluation.
        If the expression is not yet evaluated, we try to parse the expression.
          If this is unsuccessful, we raise a ValueError exception.
        Else we return the output string.
        """
        if not self._evaluated:
            self.parse()
            if not self._evaluated:
                raise ValueError
        return self._output_string

    def parse(self):
        """ Parses the current infix expression, and return the RPN version."""

        # If we've already evaluated, just return the result
        if self._evaluated:
            return self._output_string

        # Let's start evaluating
        # Right now, every expression starts with an operand
        # This is not universally true for functions and parentheses, but we're
        # not supporting them yet
        # TODO: Add support for functions and parentheses
        expecting_operand = True

        # Get the current character to inspect
        current_char = self._expr_string[self._current_position]

        # Loop until we're past the end of the string
        while (
            self._current_position < len(self._expr_string)
            and current_char != "$"
        ):

            # Skip any leading whitespace characters
            while current_char.isspace():
                self._current_position += 1
                current_char = self._expr_string[self._current_position]

            # Store whatever is next in the current_token string
            current_token = ""

            # If we are looking for an operand
            if expecting_operand:
                # First, we need to check for a leading '-' or '+' sign
                if current_char == "-" or current_char == "+":
                    current_token += current_char
                    self._current_position += 1
                    current_char = self._expr_string[self._current_position]

                # Now we loop for as long as we have numbers
                while current_char in "0123456789":
                    current_token += current_char
                    self._current_position += 1
                    current_char = self._expr_string[self._current_position]

                # We should have a number now - add it to the output string,
                # space delimited
                self._output_string += current_token + " "

                # And after every operand, we need to look for an operator
                expecting_operand = False

            else:
                # Here, we just need a single operator, so
                # Get that operator, validate it, then
                # Create a new operator object
                if current_char not in "+-*/%^":
                    raise SyntaxError

                current_operator = Operator(current_char)

                # Now comes the shunting yard part
                # - If the operator stack is empty, push the current operator
                # - Else
                #   - While the top of stack operator is higher precedence
                #     - Pop it and output it.
                #   - Push the current operator

                if not self._operator_stack:
                    self._operator_stack.append(current_operator)

                else:
                    top_operator = self._operator_stack[-1]
                    while (
                        self._operator_stack
                        and top_operator.precedence
                        > current_operator.precedence
                    ):
                        self._output_string += top_operator.op_string + " "
                        self._operator_stack.pop()
                        if self._operator_stack:
                            top_operator = self._operator_stack[-1]

                    self._operator_stack.append(current_operator)

                # Get the next character
                self._current_position += 1
                current_char = self._expr_string[self._current_position]

                # Skip any trailing whitespace characters
                while current_char.isspace():
                    self._current_position += 1
                    current_char = self._expr_string[self._current_position]

                # After every operator, look for an operand
                expecting_operand = True

        # At this point, we're done with the string, so we just need to pop
        # the remaining operators off the stack

        while self._operator_stack:
            top_operator = self._operator_stack.pop()
            self._output_string += top_operator.op_string + " "

        self._evaluated = True
        return self._output_string
