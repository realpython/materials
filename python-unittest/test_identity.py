import unittest


class TestListIdentity(unittest.TestCase):
    def test_list_aliases(self):
        a = ["Python", "unittest"]
        b = a
        self.assertIs(a, b)

    def test_list_objects(self):
        a = ["Python", "unittest"]
        b = ["Python", "unittest"]
        self.assertIsNot(a, b)


if __name__ == "__main__":
    unittest.main(verbosity=2)
