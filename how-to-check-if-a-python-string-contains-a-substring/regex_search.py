import re

file_content = """hi there and welcome.
this is a special hidden file with a secret secret.
i don't want to tell you the secret,
but i do want to secretly tell you that i have one."""

# Find words that start with "secret"
print(re.search(r"secret\w+", file_content))

# Inspect what methods on the Match object can give you
m = re.search(r"secret\w+", file_content)
print(m.group())  # "secretly"
print(m.span())  # (128, 136)

# Find the first word followed by certain punctuation characters
print(re.search(r"secret[\.,]", file_content))

# Find all words followed by certain punctuation characters
print(re.findall(r"secret[\.,]", file_content))

# Use a capturing group to remove the punctuation character
print(re.findall(r"(secret)[\.,]", file_content))

# Iterate over all matches as Match objects
for match in re.finditer(r"(secret)[\.,]", file_content):
    print(match)

# Print only the first capturing group from the match
for match in re.finditer(r"(secret)[\.,]", file_content):
    print(match.group(1))
