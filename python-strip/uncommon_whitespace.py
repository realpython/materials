text = "\u200b\u200b\u200bHello\u200b\u200b"

# Text contains a few zero width space Unicode characters
print(text)

# Default usage doesn't remove this character
print(text.strip())

# You need to remove it explicitly
print(text.strip("\u200b"))
