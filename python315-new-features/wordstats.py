from collections import Counter

def most_common_words(text, n=3):
    words = [word.strip(".,").lower() for word in text.split()]
    return Counter(words).most_common(n)

sample = "The quick brown fox jumps over the lazy dog. " * 100_000
print(most_common_words(sample))
