#!/usr/bin/env python3

"""MathREPL, a math expression evaluator using Python's eval() and math."""

import math

__version__ = "1.0"
__author__ = "Leodanis Pozo Ramos"

ALLOWED_NAMES = {
    k: v for k, v in math.__dict__.items() if not k.startswith("__")
}

PS1 = "mr>>"

WELCOME = f"""
MathREPL {__version__}, your Python math expressions evaluator!
Enter a valid math expression after the prompt "{PS1}".
Type "help" for more information.
Type "quit" or "exit" to exit.
"""

USAGE = f"""
Usage:
Build math expressions using numeric values and operators.
Use any of the following functions and constants:

{', '.join(ALLOWED_NAMES.keys())}
"""


def evaluate(expression):
    """Evaluate a math expression."""
    # Compile the expression eventually raising a SyntaxError
    # when the user enters an invalid expression
    code = compile(expression, "<string>", "eval")

    # Validate allowed names
    for name in code.co_names:
        if name not in ALLOWED_NAMES:
            raise NameError(f"The use of '{name}' is not allowed")

    # Evaluate the expression eventually raising a ValueError
    # when the user uses a math function with a wrong input value
    # e.g. math.sqrt(-10)
    return eval(code, {"__builtins__": {}}, ALLOWED_NAMES)


def main():
    """Main loop: Read and evaluate user's input."""
    print(WELCOME)
    while True:
        # Read user's input
        try:
            expression = input(f"{PS1} ")
        except (KeyboardInterrupt, EOFError):
            raise SystemExit()

        # Handle special commands
        if expression.lower() == "help":
            print(USAGE)
            continue
        if expression.lower() in {"quit", "exit"}:
            raise SystemExit()

        # Evaluate the expression and handle errors
        try:
            result = evaluate(expression)
        except SyntaxError:
            # If the user enters an invalid expression
            print("Invalid input expression syntax")
            continue
        except (NameError, ValueError) as err:
            # If the user tries to use a name that isn't allowed
            # or an invalid value to a given math function
            print(err)
            continue

        # Print the result if no error occurs
        print(f"The result is: {result}")


if __name__ == "__main__":
    main()
