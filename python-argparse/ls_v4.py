import argparse
import datetime
from pathlib import Path

parser = argparse.ArgumentParser(
    prog="ls",
    description="List the content of a directory",
    epilog="Thanks for using %(prog)s! :)",
)

parser.add_argument("path")

parser.add_argument("-l", "--long", action="store_true")

args = parser.parse_args()

target_dir = Path(args.path)

if not target_dir.exists():
    print("The target directory doesn't exist")
    raise SystemExit(1)


def build_output(entry, long=False):
    if long:
        size = entry.stat().st_size
        date = datetime.date.fromtimestamp(entry.stat().st_mtime).strftime(
            "%b %d %m:%S"
        )
        return f"{size:>6d} {date} {entry.name}"
    return entry.name


for entry in target_dir.iterdir():
    print(build_output(entry, long=args.long))
