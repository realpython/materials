import unittest

from calculations import add, divide, mean, median, mode, multiply, subtract


class TestArithmeticOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(10, 5), 50)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)
        self.assertEqual(divide(-1, 1), -1)
        self.assertEqual(divide(-1, -1), 1)
        with self.assertRaises(ValueError):
            divide(10, 0)


class TestStatisticalOperations(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(mean([1, 2, 3, 4, 5]), 3)
        self.assertEqual(mean([1, 2, 3, 4, 5, 6]), 3.5)

    def test_median_odd(self):
        self.assertEqual(median([1, 3, 3, 6, 7, 8, 9]), 6)

    def test_median_even(self):
        self.assertEqual(median([1, 2, 3, 4, 5, 6, 8, 9]), 4.5)

    def test_median_unsorted(self):
        self.assertEqual(median([7, 1, 3, 3, 2, 6]), 3)

    def test_mode_single(self):
        self.assertEqual(mode([1, 2, 2, 3, 4, 4, 4, 5]), [4])

    def test_mode_multiple(self):
        self.assertEqual(set(mode([1, 1, 2, 3, 4, 4, 5, 5])), {1, 4, 5})


def load_tests(loader, tests, pattern):
    suite = unittest.TestSuite()
    # suite.addTests(loader.loadTestsFromTestCase(TestArithmeticOperations))
    suite.addTests(loader.loadTestsFromTestCase(TestStatisticalOperations))
    return suite


if __name__ == "__main__":
    unittest.main()
