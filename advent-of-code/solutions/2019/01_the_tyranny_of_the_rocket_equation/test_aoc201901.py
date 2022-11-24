"""Tests for AoC 1, 2019: The Tyranny of the Rocket Equation"""

# Standard library imports
import pathlib

# Third party imports
import aoc201901 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == [12, 14, 1969, 100756]


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc.part1(example1) == 2 + 2 + 654 + 33583


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc.part2(example1) == 2 + 2 + 966 + 50346
