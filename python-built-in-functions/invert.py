def invert_case(text):
    result = ""
    shift = ord("a") - ord("A")

    for char in text:
        code_point = ord(char)
        if char.islower():
            result += chr(code_point - shift)
        elif char.isupper():
            result += chr(code_point + shift)
        else:
            result += char

    return result


# Example usage
example_string = "Hello, World!"
print("Original:", example_string)
print("Inverted Case:", invert_case(example_string))
