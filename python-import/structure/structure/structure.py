# structure/structure.py

# Standard library imports
import pathlib
import sys

# Local imports
from structure import files


def main():
    # Read path from command line
    try:
        root = pathlib.Path(sys.argv[1]).resolve()
    except IndexError:
        print("Need one argument: the root of the original file tree")
        raise SystemExit()

    # Re-create the file structure
    new_root = files.unique_path(pathlib.Path.cwd(), "{:03d}")
    for path in root.rglob("*"):
        if path.is_file() and new_root not in path.parents:
            rel_path = path.relative_to(root)
            files.add_empty_file(new_root / rel_path)


if __name__ == "__main__":
    main()
