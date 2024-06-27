import unittest
from datetime import datetime
from unittest.mock import Mock, patch

import requests
from holidays import get_holidays, is_weekday
from requests.exceptions import Timeout


class TestCalendar(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.wednesday = datetime(year=2025, month=1, day=1)
        cls.sunday = datetime(year=2025, month=1, day=5)
        cls.holidays = {"12/25": "Christmas", "7/4": "Independence Day"}
        cls.response_setup_dict = {
            "json.return_value": cls.holidays,
            "status_code": 200,
        }

    def log_request(self, url):
        """Helper function that logs and returns a mock successful request."""
        print(f"Making a request to {url}.")
        print("Request received!")
        return Mock(**self.response_setup_dict)

    @patch("holidays.datetime")
    def test_is_weekday_returns_true_on_weekdays(self, mock_datetime):
        mock_datetime.today.return_value = self.wednesday
        self.assertTrue(is_weekday())

    @patch("holidays.datetime")
    def test_is_weekday_returns_false_on_weekends(self, mock_datetime):
        mock_datetime.today.return_value = self.sunday
        self.assertFalse(is_weekday())

    # Example of patching only a specific object
    @patch.object(requests, "get", side_effect=requests.exceptions.Timeout)
    def test_get_holidays_timeout(self, mock_requests):
        with self.assertRaises(requests.exceptions.Timeout):
            get_holidays()

    # Example of using the `with` statement with `patch()`
    def test_get_holidays_logging(self):
        with patch("holidays.requests") as mock_requests:
            mock_requests.get.side_effect = self.log_request
            self.assertEqual(get_holidays()["12/25"], "Christmas")

    @patch("holidays.requests")
    def test_get_holidays_retry(self, mock_requests):
        response_mock = Mock(**self.response_setup_dict)
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
