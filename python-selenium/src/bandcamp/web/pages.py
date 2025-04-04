from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver

from bandcamp.web.base import WebPage
from bandcamp.web.elements import TrackListElement
from bandcamp.web.locators import DiscoverPageLocator


class DiscoverPage(WebPage):
    """Model the relevant parts of the Bandcamp Discover page."""

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self._accept_cookie_consent()
        self.discover_tracklist = TrackListElement(
            self._driver.find_element(*DiscoverPageLocator.DISCOVER_RESULTS),
            self._driver,
        )

    def _accept_cookie_consent(self) -> None:
        """Accept the necessary cookie consent."""
        try:
            self._driver.find_element(
                *DiscoverPageLocator.COOKIE_ACCEPT_NECESSARY
            ).click()
        except NoSuchElementException:
            pass
