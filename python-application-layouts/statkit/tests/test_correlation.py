import math

import pytest

from statkit import pearson, spearman


def test_pearson_perfect_positive():
    assert math.isclose(pearson([1, 2, 3, 4], [2, 4, 6, 8]), 1.0)


def test_pearson_perfect_negative():
    assert math.isclose(pearson([1, 2, 3, 4], [8, 6, 4, 2]), -1.0)


def test_spearman_monotonic_but_not_linear():
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    assert pearson(x, y) < 1.0
    assert math.isclose(spearman(x, y), 1.0)


def test_spearman_with_ties():
    assert math.isclose(
        spearman([1, 2, 2, 3], [1, 2, 3, 4]), 0.9486832980505138
    )


def test_mismatched_lengths_raise():
    with pytest.raises(ValueError):
        pearson([1, 2, 3], [1, 2])
