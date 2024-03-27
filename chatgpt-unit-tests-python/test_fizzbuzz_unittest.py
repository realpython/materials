import unittest

from fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        """Test numbers divisible by 3 but not by 5"""
        self.assertEqual(fizzbuzz(3), "fizz")
        self.assertEqual(fizzbuzz(6), "fizz")
        self.assertNotEqual(fizzbuzz(15), "fizz")

    def test_buzz(self):
        """Test numbers divisible by 5 but not by 3"""
        self.assertEqual(fizzbuzz(5), "buzz")
        self.assertEqual(fizzbuzz(10), "buzz")
        self.assertNotEqual(fizzbuzz(15), "buzz")

    def test_fizz_buzz(self):
        """Test numbers divisible by both 3 and 5"""
        self.assertEqual(fizzbuzz(15), "fizz buzz")
        self.assertEqual(fizzbuzz(30), "fizz buzz")

    def test_neither(self):
        """Test numbers not divisible by 3 or 5"""
        self.assertEqual(fizzbuzz(1), 1)
        self.assertEqual(fizzbuzz(2), 2)
        self.assertEqual(fizzbuzz(4), 4)


if __name__ == "__main__":
    unittest.main()
