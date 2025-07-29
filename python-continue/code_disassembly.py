import instaviz


def add_numbers():
    total = 0

    for number in range(-10, 10):
        if number < 0:
            continue
        total += number

    return total


instaviz.show(add_numbers)
