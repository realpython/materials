while True:
    word = input("Enter a word (or type 'exit' to stop): ")

    if word == "exit":
        break

    for letter in word:
        print(letter)
