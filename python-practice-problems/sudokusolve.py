#!/usr/bin/env python3
""" Sudoku Solver
    NOTE: A description of the Sudoku puzzle can be found at:

        https://en.wikipedia.org/wiki/Sudoku

    Given a string in SDM format, described below, write a program to find and
    return the solution for the Sudoku puzzle given in the string. The solution
    should be returned in the same SDM format as the input.

    Some puzzles will not be solvable. In that case, return the string
    "Unsolvable".

    The general sdx format is described here:

        http://www.sudocue.net/fileformats.php

    For our purposes, each SDX string will be a sequence of 81 digits, one for
    each position on the Sudoku puzzle. Known numbers will be given and unknown
    positions will have a zero value.

    For example, this string of digits (split onto two lines for readability):

        0040060790000006020560923000780610305090004
             06020540890007410920105000000840600100

    represents this starting Sudoku puzzle:

             0 0 4   0 0 6   0 7 9
             0 0 0   0 0 0   6 0 2
             0 5 6   0 9 2   3 0 0

             0 7 8   0 6 1   0 3 0
             5 0 9   0 0 0   4 0 6
             0 2 0   5 4 0   8 9 0

             0 0 7   4 1 0   9 2 0
             1 0 5   0 0 0   0 0 0
             8 4 0   6 0 0   1 0 0

    The unit tests provide may take a while to run, so be patient.
"""
import unittest


def sudoku_solve(input_string):
    # TODO: Your code goes here!
    return input_string


class SudokuSolverTestCase(unittest.TestCase):
    problems = [
        "00400607900000060205609230007806103050900040602054089000741092010500"
        "0000840600100",
        "01640000020000900040000006207023010010000000300308704096000000500080"
        "0007000006820",
        "04900860500300700000000003000040080006081502000100900001000000000060"
        "0400804500390",
        "76050000000006000800000040320040080008000003000500100780900000060001"
        "0000000003041",
        "00060500000302080004509027050000000106200054040000000709806045000604"
        "0700000203000",
        "40900070500001000000620780020000000900370420080000000400280150000006"
        "0000905000406",
        "00001003004007050100200800668000000300030200030000004520050080080104"
        "0020090020000",
        "08007003026005001800000040000060200039001008600070900000400080081004"
        "0052050090070",
        "00009300600080090002000610000008005300600020037005000000250004000100"
        "9000700130007",
    ]
    expected = [
        "28413657991375468275689234147896123553928741662154389736741592819532"
        "8764842679153",
        "31645297828567931449731856287923415614296578365318724996872143552184"
        "3697734596821",
        "14923867562395714875814623993547286146781592328136975431679458259268"
        "3417874521396",
        "76354812942136975895817246329743681518679523434582169781925437663491"
        "7582572683941",
        "82967531467312489514539827658743692196281754343195268739876145221654"
        "9738754283169",
        "41963872572851964353624789125418637919375426886792315464289153737146"
        "5982985372416",
        "76891543294327658151243879668519427317435296832968714523756981485174"
        "3629496821357",
        "48197623526745391893582146717863254939251478654678932172416589381934"
        "7652653298174",
        "Unsolvable",
    ]

    def test_solver(self):
        for index, problem in enumerate(self.problems):
            print(f"Testing puzzle {index+1}")
            result = sudoku_solve(problem)
            self.assertEqual(result, self.expected[index])


if __name__ == "__main__":
    unittest.main()
