"""Tests for AoC 5, 2020: Binary Boarding"""

# Standard library imports
import pathlib

# Third party imports
import aoc202005 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == [357, 567, 119, 820]


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc.part1(example1) == 820


def test_part2():
    """Test part 2 on example input"""
    seat_ids = [3, 9, 4, 8, 5, 10, 7, 11]
    assert aoc.part2(seat_ids) == 6
