import math

import pytest

from statkit import mean, median, stdev


def test_mean():
    assert mean([1, 2, 3, 4]) == 2.5


def test_median_odd_length():
    assert median([3, 1, 2]) == 2


def test_median_even_length():
    assert median([4, 1, 3, 2]) == 2.5


def test_stdev():
    assert math.isclose(stdev([2, 4, 4, 4, 5, 5, 7, 9]), 2.138089935299395)


@pytest.mark.parametrize("function", [mean, median, stdev])
def test_empty_data_raises(function):
    with pytest.raises(ValueError):
        function([])
