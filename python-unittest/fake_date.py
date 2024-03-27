import unittest
from datetime import date
from unittest.mock import Mock, patch

mocked_date = Mock()
mocked_date.today = Mock(return_value=date(year=2018, month=2, day=18))


class TestDate(unittest.TestCase):
    def test_full_date(self):
        with patch("fake_date.date", mocked_date) as fake_date:
            self.assertEqual(
                fake_date.today(), date(year=2018, month=2, day=18)
            )

    def test_year(self):
        with patch("fake_date.date", mocked_date) as fake_date:
            self.assertEqual(fake_date.today().year, 2018)

    def test_month(self):
        with patch("fake_date.date", mocked_date) as fake_date:
            self.assertEqual(fake_date.today().month, 2)

    def test_day(self):
        with patch("fake_date.date", mocked_date) as fake_date:
            self.assertEqual(fake_date.today().day, 18)


if __name__ == "__main__":
    unittest.main(verbosity=2)
