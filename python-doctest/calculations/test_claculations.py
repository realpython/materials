import doctest
import unittest

import calculations


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocFileSuite("tests_file.txt"))
    tests.addTests(doctest.DocTestSuite(calculations))
    return tests


if __name__ == '__main__':
    unittest.main()
