def custom_reverse(sequence):
    index = len(sequence) - 1
    while index >= 0:
        yield sequence[index]
        index -= 1
