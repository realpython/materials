file_content_title = """Hi There And Welcome.
This Is A Special Hidden File With A Secret Secret.
I Don't Want To Tell You The Secret,
But I Do Want To Secretly Tell You That I Have One."""

# Strings are case-sensitive
print("secret" in file_content_title)  # False

# Convert the input string to lowercase to generalize matching
file_content = file_content_title.lower()

print(file_content)

print("secret" in file_content)  # True
