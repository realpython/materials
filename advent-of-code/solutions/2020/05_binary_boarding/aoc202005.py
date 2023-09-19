"""AoC 5, 2020: Binary Boarding"""

# Standard library imports
import pathlib
import sys

BP2BINARY = str.maketrans({"F": "0", "B": "1", "L": "0", "R": "1"})


def parse(puzzle_input):
    """Parse input"""
    return [
        int(bp.translate(BP2BINARY), base=2) for bp in puzzle_input.split("\n")
    ]


def part1(seat_ids):
    """Solve part 1"""
    return max(seat_ids)


def part2(seat_ids):
    """Solve part 2"""
    all_ids = set(range(min(seat_ids), max(seat_ids) + 1))
    return (all_ids - set(seat_ids)).pop()


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
