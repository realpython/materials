from io import StringIO

words = ["Hello,", "World!", "I", "am", "a", "Pythonista!"]

sentence = StringIO()
sentence.write(words[0])
for word in words[1:]:
    sentence.write(" " + word)

sentence.getvalue()
result = sentence.getvalue()

print(result)
