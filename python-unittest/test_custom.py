import unittest


class CustomTestCase(unittest.TestCase):
    def assertAllIntegers(self, values):
        for value in values:
            self.assertIsInstance(
                value,
                int,
            )


class TestIntegerList(CustomTestCase):
    def test_values_are_integers(self):
        integers_list = [1, 2, 3, 4, 5]
        self.assertAllIntegers(integers_list)

    def test_values_not_all_integers(self):
        mixed_list = [1, "2", 3.0, 4, 5]
        with self.assertRaises(AssertionError):
            self.assertAllIntegers(mixed_list)


if __name__ == "__main__":
    unittest.main()
