#!/usr/bin/env python3
""" Caesar Cipher
    A caesar cipher is a simple substitution cipher where each letter of the
    plain text is substituted with a letter found by moving 'n' places down the
    alphabet. For an example, if the input plain text is:

        abcd xyz

    and the shift value, n, is 4. The encrypted text would be:

        efgh bcd

    You are to write a function which accepts two arguments, a plain-text
    message and a number of letters to shift in the cipher. The function will
    return an encrypted string with all letters being transformed while all
    punctuation and whitespace remains unchanged.

    Note: You can assume the plain text is all lowercase ascii, except for
    whitespace and punctuation.
"""
import unittest


def caesar(plain_text, shift_num=1):
    # TODO: Your code goes here!
    result = plain_text
    return result


class CaesarTestCase(unittest.TestCase):
    def test_a(self):
        start = "aaa"
        result = caesar(start, 1)
        self.assertEqual(result, "bbb")
        result = caesar(start, 5)
        self.assertEqual(result, "fff")

    def test_punctuation(self):
        start = "aaa.bbb"
        result = caesar(start, 1)
        self.assertEqual(result, "bbb.ccc")
        result = caesar(start, -1)
        self.assertEqual(result, "zzz.aaa")

    def test_whitespace(self):
        start = "aaa    bb b"
        result = caesar(start, 1)
        self.assertEqual(result, "bbb    cc c")
        result = caesar(start, 3)
        self.assertEqual(result, "ddd    ee e")

    def test_wraparound(self):
        start = "abc"
        result = caesar(start, -1)
        self.assertEqual(result, "zab")
        result = caesar(start, -2)
        self.assertEqual(result, "yza")
        result = caesar(start, -3)
        self.assertEqual(result, "xyz")

        start = "xyz"
        result = caesar(start, 1)
        self.assertEqual(result, "yza")
        result = caesar(start, 2)
        self.assertEqual(result, "zab")
        result = caesar(start, 3)
        self.assertEqual(result, "abc")


if __name__ == "__main__":
    unittest.main()
