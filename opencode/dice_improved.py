"""Simulate a six-sided dice roll.

Usage:

    $ python dice.py
    How many dice do you want to roll? [1-6] 5

~~~~~~~~~~~~~~~~~~~~~~~~~ RESULTS ~~~~~~~~~~~~~~~~~~~~~~~~~
┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
│  ●   ●  │ │  ●      │ │  ●   ●  │ │  ●   ●  │ │         │
│    ●    │ │         │ │    ●    │ │    ●    │ │    ●    │
│  ●   ●  │ │      ●  │ │  ●   ●  │ │  ●   ●  │ │         │
└─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────┘
"""

import random
from typing import List, Tuple

# Constants
MIN_DICE = 1
MAX_DICE = 6

DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "


def parse_input(input_string: str) -> int:
    """Validate input string and return as an integer.

    Check if `input_string` is an integer number between MIN_DICE and MAX_DICE.
    If so, return the integer value. Otherwise, raise a ValueError.
    """
    try:
        val = int(input_string.strip())
        if MIN_DICE <= val <= MAX_DICE:
            return val
    except ValueError:
        pass

    raise ValueError(f"Please enter a number from {MIN_DICE} to {MAX_DICE}.")


def roll_dice(num_dice: int) -> List[int]:
    """Return a list of random integers between 1 and 6 with length `num_dice`.

    Args:
        num_dice: The number of dice to roll.

    Returns:
        A list of random integers.
    """
    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1, 6)
        roll_results.append(roll)
    return roll_results


def generate_dice_faces_diagram(dice_values: List[int]) -> str:
    """Return an ASCII diagram of dice faces from `dice_values`.

    The string returned contains an ASCII representation of each die.

    Args:
        dice_values: A list of integers representing the rolled values.

    Returns:
        A formatted string with the ASCII diagram.
    """
    dice_faces = _get_dice_faces(dice_values)
    dice_faces_rows = _generate_dice_faces_rows(dice_faces)

    # Generate header with the word "RESULTS" centered
    width = len(dice_faces_rows[0])
    diagram_header = " RESULTS ".center(width, "~")

    dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows)
    return dice_faces_diagram


def _get_dice_faces(dice_values: List[int]) -> List[Tuple[str, ...]]:
    """Retrieve ASCII art representations for given dice values.

    Args:
        dice_values: A list of integers representing the rolled values.

    Returns:
        A list of tuples, where each tuple is the ASCII art for a die.
    """
    dice_faces = []
    for value in dice_values:
        dice_faces.append(DICE_ART[value])
    return dice_faces


def _generate_dice_faces_rows(dice_faces: List[Tuple[str, ...]]) -> List[str]:
    """Combine dice face tuples into horizontal rows of strings.

    Args:
        dice_faces: A list of tuples, where each tuple is the ASCII art for a
        die.

    Returns:
        A list of strings, each representing a horizontal row of the dice
        diagram.
    """
    dice_faces_rows = []
    for row_idx in range(DIE_HEIGHT):
        row_components = []
        for die in dice_faces:
            row_components.append(die[row_idx])
        row_string = DIE_FACE_SEPARATOR.join(row_components)
        dice_faces_rows.append(row_string)
    return dice_faces_rows


def main() -> None:
    """Main entry point for the Dice CLI application."""
    while True:
        num_dice_input = input(
            f"How many dice do you want to roll? [{MIN_DICE}-{MAX_DICE}] "
        )
        try:
            num_dice = parse_input(num_dice_input)
            break
        except ValueError as e:
            print(e)

    roll_results = roll_dice(num_dice)
    dice_face_diagram = generate_dice_faces_diagram(roll_results)
    print(f"\n{dice_face_diagram}")


if __name__ == "__main__":
    main()
