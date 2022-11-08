import argparse
import sys
from pathlib import Path

parser = argparse.ArgumentParser()

parser.add_argument("path")

args = parser.parse_args()

target_dir = Path(args.path)

if not target_dir.exists():
    print("The target directory doesn't exist")
    sys.exit()

if __name__ == "__main__":
    for entry in target_dir.iterdir():
        print(entry.name)
