from shopping import average, total


def test_total():
    assert total([1, 2, 3]) == 6


def test_average():
    assert average([2, 4]) == 3
