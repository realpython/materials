from unittest import TestCase
from unittest.mock import patch


class TestPrint(TestCase):
    @patch("builtins.print")
    def test_print(self, mock_print):
        print("Not a real print()")
        mock_print.assert_called_with("Not a real print()")

    @patch("builtins.print")
    def test_greet(self, mock_print):
        greet("John")
        mock_print.assert_called_with("Hello, John!")


def greet(name):
    print(f"Hello, {name}!")
