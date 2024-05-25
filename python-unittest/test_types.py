import unittest


class TestTypes(unittest.TestCase):
    def test_is_list_objects(self):
        a = [1, 2, 3, 4, 5]
        self.assertIsInstance(a, list)

    def test_is_not_list_objects(self):
        a = (1, 2, 3, 4, 5)
        self.assertNotIsInstance(a, list)


if __name__ == "__main__":
    unittest.main(verbosity=2)
