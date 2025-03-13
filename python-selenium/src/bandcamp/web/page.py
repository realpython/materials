from selenium.webdriver.remote.webdriver import WebDriver

from bandcamp.web.base import WebPage
from bandcamp.web.element import DiscoverTrackList
from bandcamp.web.locators import DiscoverPageLocator


class DiscoverPage(WebPage, DiscoverPageLocator):
    """Model the relevant parts of the Bandcamp Discover page."""

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self._accept_cookie_consent()
        self.discover_tracklist = DiscoverTrackList(
            self._driver.find_element(*self.DISCOVER_RESULTS), self._driver
        )

    def _accept_cookie_consent(self) -> None:
        """Accept the necessary cookie consent."""
        self._driver.find_element(*self.COOKIE_ACCEPT_NECESSARY).click()
