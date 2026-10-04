import pytest
from version_check import Version


def test_equal_versions_compare_equal():
    assert Version("1.2.0") == Version("1.2.0")


def test_smaller_release_sorts_first():
    assert Version("1.2.0") < Version("1.3.0")


def test_versions_with_different_lengths_compare():
    assert Version("1.2") < Version("1.2.1")


def test_greater_than_works():
    assert Version("2.0.0") > Version("1.9.9")


def test_unequal_versions_are_not_equal():
    assert Version("1.0.0") != Version("1.0.1")


def test_double_digit_segments_sort_numerically():
    assert Version("3.9") < Version("3.10")


@pytest.mark.parametrize(
    "lower, higher",
    [
        ("1.0.dev1", "1.0"),
        ("1.0a1", "1.0"),
        ("1.0", "1.0.post1"),
        ("1.0.dev1", "1.0a1"),
        ("1.0a1", "1.0b1"),
        ("1.0b1", "1.0rc1"),
        ("1.0.dev1", "1.0.post1"),
    ],
)
def test_phase_ordering(lower, higher):
    assert Version(lower) < Version(higher)


@pytest.mark.parametrize(
    "text",
    [
        "",
        "   ",
        "1.x.0",
        "banana",
        "1..0",
    ],
)
def test_invalid_input_raises(text):
    with pytest.raises(ValueError):
        Version(text)


def test_comparing_against_other_types_returns_notimplemented():
    assert Version("1.0").__eq__("1.0") is NotImplemented
