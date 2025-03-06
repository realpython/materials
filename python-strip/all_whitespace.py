spacy_text = "    Hello   ,      World !    "
print(spacy_text.strip())

# Normalize whitespace
words = spacy_text.split()
print(" ".join(words))

# Remove all whitespace
print(spacy_text.replace(" ", ""))
