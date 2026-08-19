from argparse import ArgumentParser
from collections import Counter
from pathlib import Path

parser = ArgumentParser(description="Show the most common words in a text file.")
parser.add_argument("file", type=Path)
parser.add_argument("-n", "--top", type=int, default=5)
args = parser.parse_args()


words = args.file.read_text(encoding="utf-8").lower().split()
for word, count in Counter(words).most_common(args.top):
    print(f"{word}: {count}")
