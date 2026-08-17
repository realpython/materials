import pytest
from version_check import Version


def test_equal_versions_compare_equal():
    assert Version("1.2.0") == Version("1.2.0")


def test_smaller_release_sorts_first():
    assert Version("1.2.0") < Version("1.3.0")


def test_double_digit_segments_sort_numerically():
    assert Version("3.9") < Version("3.10")


@pytest.mark.parametrize(
    "lower, higher",
    [
        ("1.0.dev1", "1.0"),  # Dev before final
        ("1.0a1", "1.0"),  # Pre-release before final
        ("1.0", "1.0.post1"),  # Post-release after final
        ("1.0.dev1", "1.0a1"),  # Dev before pre-release
        ("1.0a1", "1.0b1"),  # Alpha before beta
        ("1.0b1", "1.0rc1"),  # Beta before release candidate
        ("1.0.dev1", "1.0.post1"),  # Dev before post, spanning the release
    ],
)
def test_phase_ordering(lower, higher):
    assert Version(lower) < Version(higher)


@pytest.mark.parametrize(
    "text",
    [
        "",  # Empty string
        "   ",  # Whitespace only
        "1.x.0",  # Non-numeric segment
        "banana",  # Not a version at all
        "1..0",  # Empty segment
        "v1.0",  # Leading junk
    ],
)
def test_invalid_input_raises(text):
    with pytest.raises(ValueError):
        Version(text)
