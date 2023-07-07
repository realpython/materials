import argparse

from bleach.app import sanitize


def main() -> None:
    args = cli_prompt()
    if args.test:
        print("Sanitizing...")
        print(sanitize(args.file))
    else:
        cleaned_filename = f"{args.file.split('.')[-2]}_sanitized.txt"
        with open(cleaned_filename, "w") as sanitized_file:
            sanitized_file.write(sanitize(args.file))

def cli_prompt() -> argparse.Namespace:
    """Parse the arguments provided through the CLI."""
    parser = argparse.ArgumentParser(
        description="Sanitize chat support text with OpenAI's API"
    )
    parser.add_argument("--file", help="Path to file with text")
    parser.add_argument("--test", action='store_true', help="Show output in console")

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    main()
