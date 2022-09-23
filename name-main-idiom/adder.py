import unittest


def add(a: int, b: int) -> int:
    return a + b


class TestAdder(unittest.TestCase):
    def test_add_adds_two_numbers(self):
        self.assertEqual(add(1, 2), 3)


if __name__ == "__main__":
    unittest.main()
