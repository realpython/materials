unique_words = set()
text = """
Beautiful is better than ugly
Explicit is better than implicit
Simple is better than complex
Complex is better than complicated
""".lower()

for word in text.split():
    unique_words.add(word)

print(unique_words)

print(set(text.split()))

unique_words = {word for word in text.split()}

print(unique_words)
