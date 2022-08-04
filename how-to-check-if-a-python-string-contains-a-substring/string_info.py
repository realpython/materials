file_content = """hi there and welcome.
this is a special hidden file with a secret secret.
i don't want to tell you the secret,
but i do want to secretly tell you that i have one.
"""

# Use .index() to get the starting index of the first match
print(file_content.index("secret"))

# Pass a custom start index to .index() to search from a different point
print(file_content.index("secret", 60))

# Count the number of matches in the text
print(file_content.count("secret"))

# Use a for loop to inspect all matches
for word in file_content.split():
    if "secret" in word:
        print(word)

# Use a list comprehension and a conditional check for a one-liner
print([word for word in file_content.split() if "secret" in word])
