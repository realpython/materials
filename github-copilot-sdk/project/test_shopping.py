from shopping import compute_average, compute_total


def test_compute_total():
    assert compute_total([1, 2, 3]) == 6


def test_compute_average():
    assert compute_average([2, 4]) == 3
