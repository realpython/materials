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
        "004006079000000602056092300078061030509000406020540890007410920105000000840600100",
        "016400000200009000400000062070230100100000003003087040960000005000800007000006820",
        "049008605003007000000000030000400800060815020001009000010000000000600400804500390",
        "760500000000060008000000403200400800080000030005001007809000000600010000000003041",
        "000605000003020800045090270500000001062000540400000007098060450006040700000203000",
        "409000705000010000006207800200000009003704200800000004002801500000060000905000406",
        "000010030040070501002008006680000003000302000300000045200500800801040020090020000",
        "080070030260050018000000400000602000390010086000709000004000800810040052050090070",
        "000093006000800900020006100000080053006000200370050000002500040001009000700130007",
    ]
    expected = [
        "284136579913754682756892341478961235539287416621543897367415928195328764842679153",
        "316452978285679314497318562879234156142965783653187249968721435521843697734596821",
        "149238675623957148758146239935472861467815923281369754316794582592683417874521396",
        "763548129421369758958172463297436815186795234345821697819254376634917582572683941",
        "829675314673124895145398276587436921962817543431952687398761452216549738754283169",
        "419638725728519643536247891254186379193754268867923154642891537371465982985372416",
        "768915432943276581512438796685194273174352968329687145237569814851743629496821357",
        "481976235267453918935821467178632549392514786546789321724165893819347652653298174",
        "Unsolvable",
    ]

    def test_solver(self):
        for index, problem in enumerate(self.problems):
            print(f"Testing puzzle {index+1}")
            result = sudoku_solve(problem)
            self.assertEqual(result, self.expected[index])


if __name__ == "__main__":
    unittest.main()
