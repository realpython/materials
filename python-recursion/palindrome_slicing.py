def is_palindrome(word):
    """Return True if word is a palindrome, False if not."""
    return word == word[::-1]


if __name__ == "__main__":
    for word in ["foo", "racecar", "troglodyte", "civic"]:
        print(f"{word!r}: {is_palindrome(word)}")
