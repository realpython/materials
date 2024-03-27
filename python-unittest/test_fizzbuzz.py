import unittest

from fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), "fizz")

    def test_buzz(self):
        self.assertEqual(fizzbuzz(5), "buzz")

    def test_fizz_buzz(self):
        self.assertEqual(fizzbuzz(15), "fizz buzz")

    def test_neither(self):
        self.assertEqual(fizzbuzz(1), 1)
        self.assertEqual(fizzbuzz(2), 2)
        self.assertEqual(fizzbuzz(4), 4)


if __name__ == "__main__":
    unittest.main(verbosity=2)
