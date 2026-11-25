"""Count the most common words in a text file."""

import sys
from collections import Counter


def top_words(text, n=3):
    words = text.split()
    return Counter(words).most_common(n)


if __name__ == "__main__":
    with open(sys.argv[1], encoding="utf-8") as file:
        for word, count in top_words(file.read()):
            print(f"{word}: {count}")
