words = ["apple", "kiwi", "banana", "fig"]

long_words = []
for word in words:
    if len(word) > 3:
        long_words.append(word.upper())

print(long_words)
print(long_words == [word.upper() for word in words if len(word) > 3])
