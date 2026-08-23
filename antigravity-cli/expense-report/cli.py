"""Command-line entry point for the expense reporter."""

import sys

from transactions import report


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "transactions.csv"
    print(report(path))


if __name__ == "__main__":
    main()
