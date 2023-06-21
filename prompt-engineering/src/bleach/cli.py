import argparse

from bleach.app import sanitize


def main() -> None:
    args = cli_prompt()
    print("Sanitizing...")
    print(sanitize(args.file))


def cli_prompt() -> argparse.Namespace:
    """Parse the arguments provided through the CLI."""
    parser = argparse.ArgumentParser(
        description="Sanitize chat support text with OpenAI's API"
    )
    parser.add_argument("--file", help="Path to file with text")

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    main()
