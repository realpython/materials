import unittest


def adder(a: int, b: int) -> int:
    return a + b


class TestAdder(unittest.TestCase):
    def test_adder_adds_two_numbers(self):
        self.assertEqual(adder(1, 2), 3)


if __name__ == "__main__":
    unittest.main()
