# feel_young.py


def make_young(text):
    words = [replace_by_age(w) for w in text.split()]
    return " ".join(words)


def replace_by_age(word, new_age=24, age_range=(25, 120)):
    if word.isdigit() and int(word) in range(*age_range):
        return str(new_age)
    return word


if __name__ == "__main__":
    text = input("Tell me something: ")
    print(make_young(text))
