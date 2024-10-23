from selenium.webdriver.remote.webdriver import WebDriver

from bandcamp.web.base import WebPage
from bandcamp.web.element import DiscoverTrackList
from bandcamp.web.locators import HomePageLocatorMixin


class HomePage(WebPage, HomePageLocatorMixin):
    """Models the relevant parts of the Bandcamp home page."""

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.discover_tracklist = DiscoverTrackList(
            self._driver.find_element(*self.DISCOVER_RESULTS), self._driver
        )
