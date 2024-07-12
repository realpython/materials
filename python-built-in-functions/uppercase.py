def is_uppercase(text):
    for char in text:
        if not (65 <= ord(char) <= 90):
            return False
    return True


print(is_uppercase("HELLO"))  # True
print(is_uppercase("Hello"))  # False
