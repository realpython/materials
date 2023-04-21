def concatenate(iterable, sep=" "):
    sentence = iterable[0]
    for word in iterable[1:]:
        sentence += sep + word
    return sentence
