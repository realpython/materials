# number_input_examples.py

# This file accompanies the Real Python article
# "How To Read User Input As Integers". It contains
# examples of functions that filter user input for
# valid integers and floats.


def get_integer(prompt: str, error_message: str = None) -> int:
    # Prompts the user for an integer value. If the input is invalid,
    # prints error_message (if specified) and then repeats the prompt.
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            if error_message:
                print(error_message)


def get_float(prompt: str, error_message: str = None) -> float:
    # Prompts the user for a float value. If the input is invalid,
    # prints error_message (if specified) and then repeats the prompt.
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            if error_message:
                print(error_message)


def get_integer_with_default(
    prompt: str, default_value: int, error_message: str = None
) -> int:
    # Prompts the user for an integer. If the input is an empty string,
    # returns default_value. Otherwise, if the input is not a valid integer,
    # prints error_message (if specified) and then repeats the prompt.
    while True:
        input_string = input(prompt)
        if input_string == "":
            return default_value
        try:
            result = int(input_string)
            return result
        except ValueError:
            if error_message:
                print(error_message)


# Run this file as a main module
# (ie python number_input_examples.py)
# to perform simple interactive testing of the functions.

if __name__ == "__main__":
    print(get_integer("Testing get_integer(): "))
    print(
        get_integer(
            "Testing get_integer() with an error message: ", "Invalid integer!"
        )
    )
    print(
        get_float(
            "Testing get_float() with an error message: ", "Invalid float!"
        )
    )
    print(
        get_integer_with_default(
            "Testing get_integer_with_default(): ",
            99,
            "That's not a valid integer!",
        )
    )
