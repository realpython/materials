import requests

__version__ = "1.0.0"
__author__ = "Real Python"

__all__ = ["get_page_content", "WebPage", "__version__", "__author__"]


BASE_URL = "http://example.com"


def get_page_content(page):
    return _fetch_page(page).text


def _fetch_page(page):
    url = f"{BASE_URL}/{page}"
    return requests.get(url)


class WebPage:
    def __init__(self, page):
        self.response = _fetch_page(page)

    def get_content(self):
        return self.response.text
