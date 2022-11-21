"""AoC 5, 2021: Hydrothermal Venture"""

# Standard library imports
import collections
import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    lines = []
    for line in puzzle_input.split("\n"):
        point1, point2 = line.split(" -> ")
        x1, y1 = point1.split(",")
        x2, y2 = point2.split(",")
        lines.append((int(x1), int(y1), int(x2), int(y2)))
    return lines


def part1(lines):
    """Solve part 1"""
    vertical = [(x1, y1, x2, y2) for x1, y1, x2, y2 in lines if x1 == x2]
    horizontal = [(x1, y1, x2, y2) for x1, y1, x2, y2 in lines if y1 == y2]
    return count_overlaps(vertical + horizontal)


def part2(lines):
    """Solve part 2"""
    return count_overlaps(lines)


def count_overlaps(lines):
    """Count overlapping points between a list of lines

    ## Example:

    >>> count_overlaps(
    ...     [(3, 3, 3, 5), (3, 3, 6, 3), (6, 6, 6, 3), (4, 5, 6, 5)]
    ... )
    3
    """
    overlaps = collections.Counter(
        point for line in lines for point in points(line)
    )
    return sum(num_points >= 2 for num_points in overlaps.values())


def points(line):
    """List all points making up a line

    ## Examples:

    >>> points((0, 3, 3, 3))  # Horizontal line
    [(0, 3), (1, 3), (2, 3), (3, 3)]
    >>> points((3, 3, 3, 0))  # Vertical line
    [(3, 3), (3, 2), (3, 1), (3, 0)]
    >>> points((1, 2, 3, 4))  # Diagonal line
    [(1, 2), (2, 3), (3, 4)]
    """
    match line:
        case (x1, y1, x2, y2) if x1 == x2:
            return [(x1, y) for y in coords(y1, y2)]
        case (x1, y1, x2, y2) if y1 == y2:
            return [(x, y1) for x in coords(x1, x2)]
        case (x1, y1, x2, y2):
            return [(x, y) for x, y in zip(coords(x1, x2), coords(y1, y2))]


def coords(start, stop):
    """List coordinates between start and stop, inclusive.

    ## Examples:

    >>> list(coords(0, 3))
    [0, 1, 2, 3]
    >>> list(coords(2, -2))
    [2, 1, 0, -1, -2]
    """
    step = 1 if start <= stop else -1
    return range(start, stop + step, step)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
