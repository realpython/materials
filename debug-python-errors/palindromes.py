def find_palindromes(text):
    # Split sentence into words
    words = text.split()

    # Remove punctuation and convert to lowercase
    normalized_words = ["".join(filter(str.isalnum, word)).lower() for word in words]

    # Check for palindromes
    return [word for word in normalized_words if word == word[::-1]]


if __name__ == "__main__":
    print(find_palindromes("Dad plays many solos at noon, and sees a racecar."))
