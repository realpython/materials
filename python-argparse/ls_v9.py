import argparse
import datetime
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
    help="take the path to the target directory (default: %(default)s)",
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
    parser.exit(1, message="The target directory doesn't exist")


def build_output(entry, long=False):
    if long:
        size = entry.stat().st_size
        date = datetime.date.fromtimestamp(entry.stat().st_mtime).strftime(
            "%b %d %m:%S"
        )
        return f"{size:>6d} {date} {entry.name}"
    return entry.name


for entry in target_dir.iterdir():
    try:
        long = args.long
    except AttributeError:
        long = False
    print(build_output(entry, long=long))
