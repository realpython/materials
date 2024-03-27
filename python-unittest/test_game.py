import unittest

from game import rock_paper_scissors


class TestRockPaperScissors(unittest.TestCase):
    def test_out_of_range(self):
        with self.assertRaises(ValueError):
            rock_paper_scissors(42)

    def test_rock(self):
        self.assertEqual(rock_paper_scissors(0), "rock")

    def test_paper(self):
        self.assertEqual(rock_paper_scissors(1), "paper")

    def test_scissors(self):
        self.assertEqual(rock_paper_scissors(2), "scissors")


if __name__ == "__main__":
    unittest.main()
