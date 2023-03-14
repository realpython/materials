"""Utility functions for prompting users for numeric input.

This file accompanies the Real Python tutorial How To Read User Input As
Integers. It contains examples of functions that filter user input for valid
integers and floats.
"""


def get_integer(prompt: str, error_message: str = None) -> int:
    """Prompts the user for an integer value.

    If the input is invalid, prints error_message (if specified) and then
    repeats the prompt.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            if error_message:
                print(error_message)


def get_float(prompt: str, error_message: str = None) -> float:
    """Prompts the user for a float value.

    If the input is invalid, prints error_message (if specified) and then
    repeats the prompt.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            if error_message:
                print(error_message)


def get_integer_with_default(
    prompt: str, default_value: int, error_message: str = None
) -> int:
    """Prompts the user for an integer, and falls back to a default value.

    If the input is an empty string, then the function returns default_value.
    Otherwise, if the input is not a valid integer, prints error_message (if
    specified) and then repeats the prompt.
    """
    while True:
        input_string = input(prompt)
        if not input_string:
            return default_value
        try:
            return int(input_string)
        except ValueError:
            if error_message:
                print(error_message)


if __name__ == "__main__":
    # Test functions when running as a script.
    print(get_integer("Test get_integer(): "))
    print(
        get_integer(
            "Test get_integer() with an error message: ",
            error_message="Invalid integer!",
        )
    )
    print(
        get_float(
            "Test get_float() with an error message: ",
            error_message="Invalid float!",
        )
    )
    print(
        get_integer_with_default(
            "Test get_integer_with_default(): ",
            default_value=99,
            error_message="That's not a valid integer!",
        )
    )
