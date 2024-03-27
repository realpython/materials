import unittest

from prime_v1 import is_prime


class TestIsPrime(unittest.TestCase):
    def test_prime_numbers(self):
        for num in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
            with self.subTest(num=num):
                self.assertTrue(is_prime(num))

    def test_non_prime_numbers(self):
        for num in [-1, 0, 1, 4, 6, 8, 9, 10, 12, 15]:
            with self.subTest(num=num):
                self.assertFalse(is_prime(num))

    # def test_prime_number(self):
    #     self.assertTrue(is_prime(17))

    # def test_non_prime_number(self):
    #     self.assertFalse(is_prime(10))


if __name__ == "__main__":
    unittest.main(verbosity=2)
