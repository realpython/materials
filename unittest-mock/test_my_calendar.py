import datetime
import unittest
from unittest.mock import Mock, patch

import requests
from requests.exceptions import Timeout

from my_calendar import get_holidays, is_weekday


class TestCalendar(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.wednesday = datetime.datetime(year=2025, month=1, day=1)
        cls.sunday = datetime.datetime(year=2025, month=1, day=5)
        cls.holidays = {"12/25": "Christmas", "7/4": "Independence Day"}
        cls.response_setup_dict = {
            "json.return_value": TestCalendar.holidays,
            "status_code": 200,
        }

    def log_request(self, url):
        """Helper function that logs and returns a mock successful request."""
        print(f"Making a request to {url}.")
        print("Request received!")
        response_mock = Mock(**TestCalendar.response_setup_dict)
        return response_mock

    @patch("my_calendar.datetime")
    def test_is_weekday_returns_true_on_weekdays(self, mock_datetime):
        mock_datetime.today.return_value = TestCalendar.wednesday
        self.assertTrue(is_weekday())

    @patch("my_calendar.datetime")
    def test_is_weekday_returns_false_on_weekends(self, mock_datetime):
        mock_datetime.today.return_value = TestCalendar.sunday
        self.assertFalse(is_weekday())

    # Example of patching only a specific object
    @patch.object(requests, "get", side_effect=requests.exceptions.Timeout)
    def test_get_holidays_timeout(self, mock_requests):
        with self.assertRaises(requests.exceptions.Timeout):
            get_holidays()

    # Example of using the `with` statement with `patch()`
    def test_get_holidays_logging(self):
        with patch("my_calendar.requests") as mock_requests:
            mock_requests.get.side_effect = self.log_request
            self.assertEqual(get_holidays()["12/25"], "Christmas")

    @patch("my_calendar.requests")
    def test_get_holidays_retry(self, mock_requests):
        response_mock = Mock(**TestCalendar.response_setup_dict)
        # Set the side effect of .get()
        mock_requests.get.side_effect = [Timeout, response_mock]
        # Test that the first request raises a Timeout
        with self.assertRaises(Timeout):
            get_holidays()
        # Now retry, expecting a successful response
        self.assertEqual(get_holidays()["12/25"], "Christmas")
        # Finally, assert .get() was called twice
        self.assertEqual(mock_requests.get.call_count, 2)


if __name__ == "__main__":
    unittest.main()
