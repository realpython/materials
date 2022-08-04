raw_file_content = """Hi there and welcome.
This is a special hidden file with a SECRET secret.
I don't want to tell you The Secret,
but I do want to secretly tell you that I have one.
"""

# Use the membership operator for pythonic membership checks
print("secret" in raw_file_content)

# You can do the inverse with `not in`
print("secret" not in raw_file_content)

# Using `in` is a readable way to check if a string contains a substring
if "secret" in raw_file_content:
   print("Found!")
