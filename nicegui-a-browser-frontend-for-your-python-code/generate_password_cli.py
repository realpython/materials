import argparse
import secrets
import string

MIN_LENGTH = 8
MAX_LENGTH = 64
DEFAULT_LENGTH = 16
SYMBOLS = "!@#$%^&*()-_=+"


def generate_password(
    length: int,
    digits: bool = True,
    symbols: bool = False,
) -> str:
    if not MIN_LENGTH <= length <= MAX_LENGTH:
        raise ValueError(f"length must be from {MIN_LENGTH} to {MAX_LENGTH}")

    alphabet = string.ascii_letters
    if digits:
        alphabet += string.digits
    if symbols:
        alphabet += SYMBOLS
    return "".join(secrets.choice(alphabet) for _ in range(length))


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a random password.")
    parser.add_argument(
        "-l",
        "--length",
        type=int,
        default=DEFAULT_LENGTH,
        help=(
            f"number of characters, {MIN_LENGTH} to {MAX_LENGTH} "
            f"(default: {DEFAULT_LENGTH})"
        ),
    )
    parser.add_argument(
        "--digits",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="allow digits (default: on)",
    )
    parser.add_argument(
        "--symbols",
        action=argparse.BooleanOptionalAction,
        default=False,
        help="allow symbols (default: off)",
    )
    args = parser.parse_args()

    try:
        print(generate_password(args.length, args.digits, args.symbols))
    except ValueError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
