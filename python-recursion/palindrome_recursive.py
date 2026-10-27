def is_palindrome(word):
    """Return True if word is a palindrome, False if not."""
    if len(word) <= 1:
        return True
    else:
        return word[0] == word[-1] and is_palindrome(word[1:-1])


if __name__ == "__main__":
    for word in ["", "a", "foo", "racecar", "troglodyte", "civic"]:
        print(f"{word!r}: {is_palindrome(word)}")
