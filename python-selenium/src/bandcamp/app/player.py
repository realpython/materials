from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

from bandcamp.web.element import TrackElement
from bandcamp.web.page import HomePage

BANDCAMP_FRONTPAGE_URL = "https://bandcamp.com/"


class Player:
    """Play tracks from Bandcamp's Discover section."""

    def __init__(self) -> None:
        self._driver = self._set_up_driver()
        self.home = HomePage(self._driver)
        self.discover = self.home.discover_tracklist
        self._current_track = TrackElement(
            self.home.discover_tracklist.available_tracks[0], self._driver
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        """Close the headless browser."""
        self._driver.close()

    def play(self, track_number=None):
        """Play the first track, or one of the available numbered tracks."""
        if track_number:
            self._current_track = TrackElement(
                self.home.discover_tracklist.available_tracks[
                    track_number - 1
                ],
                self._driver,
            )
        self._current_track.play()

    def _set_up_driver(self):
        """Create a headless browser pointing to Bandcamp."""
        options = Options()
        options.add_argument("--headless")
        browser = Firefox(options=options)
        browser.get(BANDCAMP_FRONTPAGE_URL)
        return browser
