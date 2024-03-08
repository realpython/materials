import unittest

from calculations import (
    add,
    divide,
    mean,
    median,
    mode,
    multiply,
    subtract,
)


class TestFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(multiply(10, 5), 50)

    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_mean(self):
        self.assertEqual(mean([1, 2, 3, 4, 5]), 3)

    def test_median_even(self):
        self.assertEqual(median([1, 2, 3, 4, 5, 6]), 3.5)

    def test_median_odd(self):
        self.assertEqual(median([1, 2, 3, 4, 5]), 3)

    def test_mode_single(self):
        self.assertEqual(
            sorted(mode([1, 2, 2, 3, 4, 4, 4, 5])), [4]
        )

    def test_mode_multi(self):
        self.assertEqual(sorted(mode([1, 1, 2, 3, 3])), [1, 3])


def suite():
    arithmetic_suite = unittest.TestSuite()
    statistic_suite = unittest.TestSuite()

    arithmetic_suite.addTest(TestFunctions("test_add"))
    arithmetic_suite.addTest(TestFunctions("test_subtract"))
    arithmetic_suite.addTest(TestFunctions("test_multiply"))
    arithmetic_suite.addTest(TestFunctions("test_divide"))

    statistic_suite.addTest(TestFunctions("test_mean"))
    statistic_suite.addTest(TestFunctions("test_median_even"))
    statistic_suite.addTest(TestFunctions("test_median_odd"))
    statistic_suite.addTest(TestFunctions("test_mode_single"))
    statistic_suite.addTest(TestFunctions("test_mode_multi"))

    return arithmetic_suite, statistic_suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()

    arithmetic_suite, statistical_suite = suite()

    print("Running arithmetic functions tests:")
    runner.run(arithmetic_suite)

    print("\nRunning statistical functions tests:")
    runner.run(statistical_suite)
