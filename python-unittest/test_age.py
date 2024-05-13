import unittest

from age import categorize_by_age


class TestCategorizeByAge(unittest.TestCase):
    def test_child(self):
        """Test for 'Child'"""
        self.assertEqual(categorize_by_age(5), "Child")

    def test_adolescent(self):
        """Test for 'Adolescent'"""
        self.assertEqual(categorize_by_age(15), "Adolescent")

    def test_adult(self):
        """Test for 'Adult'"""
        self.assertEqual(categorize_by_age(30), "Adult")

    def test_golden_age(self):
        """Test for 'Golden age'"""
        self.assertEqual(categorize_by_age(70), "Golden age")

    def test_negative_age(self):
        """Test for negative age"""
        self.assertEqual(categorize_by_age(-1), "Invalid age: -1")

    def test_too_old(self):
        """Test for too old"""
        self.assertEqual(categorize_by_age(151), "Invalid age: 151")

    def test_boundary_child_adolescent(self):
        """Test for boundary between 'Child' and 'Adolescent'"""
        self.assertEqual(categorize_by_age(9), "Child")
        self.assertEqual(categorize_by_age(10), "Adolescent")

    def test_boundary_adolescent_adult(self):
        """Test for boundary between 'Adolescent' and 'Adult'"""
        self.assertEqual(categorize_by_age(18), "Adolescent")
        self.assertEqual(categorize_by_age(19), "Adult")

    def test_boundary_adult_golden_age(self):
        """Test for boundary between 'Adult' and 'Golden age'"""
        self.assertEqual(categorize_by_age(65), "Adult")
        self.assertEqual(categorize_by_age(66), "Golden age")


if __name__ == "__main__":
    unittest.main(verbosity=2)
