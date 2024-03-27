import unittest

from even import is_even

#     def test_even_number(self):
#         self.assertEqual(is_even(2), True)

#     def test_odd_number(self):
#         self.assertEqual(is_even(3), False)

#     def test_negative_even_number(self):
#         self.assertEqual(is_even(-2), True)

#     def test_negative_odd_number(self):
#         self.assertEqual(is_even(-3), False)


class TestIsEven(unittest.TestCase):
    def test_even_number(self):
        for number in [2, 4, 6, -8, -10, -12]:
            with self.subTest(number=number):
                self.assertEqual(is_even(number), True)

    def test_odd_number(self):
        for number in [1, 3, 5, -7, -9, -11]:
            with self.subTest(number=number):
                self.assertEqual(is_even(number), False)


if __name__ == "__main__":
    unittest.main(verbosity=2)
