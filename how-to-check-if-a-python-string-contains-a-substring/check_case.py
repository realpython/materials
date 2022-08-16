title_cased_file_content = """Hi There And Welcome.
This Is A Special Hidden File With A Secret Secret.
I Don't Want To Tell You The Secret,
But I Do Want To Secretly Tell You That I Have One."""

# Strings are case-sensitive
print("secret" in title_cased_file_content)  # False

# Convert the input string to lowercase to generalize matching
file_content = title_cased_file_content.lower()

print(file_content)

print("secret" in file_content)  # True
