 
import sys
from collections import Counter

def count_word_frequency(file_path):
    """Counts the frequency of each word in a given text file."""
    try:
        with open(file_path, 'r') as f:
            words = f.read().lower().split()
            word_count = Counter(words)
            sorted_word_count = word_count.most_common()

            print("\nWord Frequency Count (Descending):\n")
            for word, count in sorted_word_count:
                print(f"{word}: {count}")
    except FileNotFoundError:
        print("File not found. Please check the file path.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python word_counter.py <file_path>")
    else:
        file_path = sys.argv[1]
        count_word_frequency(file_path)
