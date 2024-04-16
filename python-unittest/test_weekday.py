import datetime
import unittest
from unittest.mock import patch

import weekday


class TestWeekday(unittest.TestCase):
    @patch("weekday.datetime")
    def test_is_weekday(self, mock_datetime):
        mock_datetime.date.today.return_value = datetime.date(2024, 4, 4)
        self.assertTrue(weekday.is_weekday())

    @patch("weekday.datetime")
    def test_is_weekend(self, mock_datetime):
        mock_datetime.date.today.return_value = datetime.date(2024, 4, 6)
        self.assertFalse(weekday.is_weekday())


if __name__ == "__main__":
    unittest.main(verbosity=2)
