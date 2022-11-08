import argparse
import datetime
import sys
from pathlib import Path

parser = argparse.ArgumentParser(
    prog="ls",
    description="List the content of a directory",
    epilog="Thanks for using %(prog)s! :)",
    argument_default=argparse.SUPPRESS,
)

general = parser.add_argument_group("general output")
general.add_argument(
    "path",
    nargs="?",
    default=".",
    help="takes the path to the target directory (default: %(default)s)",
)

detailed = parser.add_argument_group("detailed output")
detailed.add_argument(
    "-l",
    "--long",
    action="store_true",
    help="display detailed directory content",
)

args = parser.parse_args()

target_dir = Path(args.path)

if not target_dir.exists():
    print("The target directory doesn't exist")
    sys.exit()


def build_output(entry, long=False):
    if long:
        size = entry.stat().st_size
        owner = entry.owner()
        date = datetime.date.fromtimestamp(entry.stat().st_mtime).strftime(
            "%b %d %m:%S"
        )
        return f"{owner} {size:>6d} {date} {entry.name}"
    return entry.name


if __name__ == "__main__":
    for entry in target_dir.iterdir():
        try:
            long = args.long
        except AttributeError:
            long = False
        print(build_output(entry, long=long))
