def parse_input(input_string):
    """Return `input_string` as an integer between 1 and 6.

    Check if `input_string` is an integer number between 1 and 6.
    If so, return an integer with the same value. Otherwise, tell
    the user to enter a valid number and quit the program.
    """
    is_valid = input_string.isdigit() and 1 <= int(input_string) <= 6
    if is_valid:
        return int(input_string)
    else:
        print("Please enter an integer between 1 and 6.")
        raise SystemExit(1)


# ~~~ CLIENT CODE ~~~
# 1. Get and validate user's input
num_dice_input = input("How many dice do you want to roll? [1-6] ")
num_dice = parse_input(num_dice_input)
