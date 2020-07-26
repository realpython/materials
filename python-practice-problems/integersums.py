#!/usr/bin/env python3
""" Sum of Integers Up To n
    Write a function, add_it_up, which returns the sum of the integers from 0
    to the single integer input parameter.

    The function should return 0 if a non-integer is passed in.
"""
import unittest


def add_it_up(n):
    # TODO: Your code goes here!
    return n


class IntegerSumTestCase(unittest.TestCase):
    def test_to_ten(self):
        results = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
        for n in range(10):
            self.assertEqual(add_it_up(n), results[n])

    def test_string(self):
        self.assertEqual(add_it_up("testing"), 0)

    def test_float(self):
        self.assertEqual(add_it_up(0.124), 0)

    def test_negative(self):
        self.assertEqual(add_it_up(-19), 0)


if __name__ == "__main__":
    unittest.main()
