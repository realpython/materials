import unittest

from fruit import capitalize_fruit_names


class TestFruit(unittest.TestCase):
    def test_empty_list(self):
        """with empty list"""
        self.assertEqual(capitalize_fruit_names([]), [])

    def test_lowercase(self):
        """with lowercase strings"""
        self.assertEqual(
            capitalize_fruit_names(["apple", "banana", "cherry"]),
            ["Apple", "Banana", "Cherry"],
        )

    def test_uppercase(self):
        """with uppercase strings"""
        self.assertEqual(
            capitalize_fruit_names(["APPLE", "BANANA", "CHERRY"]),
            ["Apple", "Banana", "Cherry"],
        )

    def test_mixed_case(self):
        """with mixed case strings"""
        self.assertEqual(
            capitalize_fruit_names(["mAnGo", "grApE"]),
            ["Mango", "Grape"],
        )

    def test_non_string_element(self):
        """with a mix of integer and string elements"""
        self.assertEqual(
            capitalize_fruit_names([123, "banana"]),
            ["", "Banana"],
        )


if __name__ == "__main__":
    unittest.main()
