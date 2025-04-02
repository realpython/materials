from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

from bandcamp.web.page import DiscoverPage

BANDCAMP_DISCOVER_URL = "https://bandcamp.com/discover/"


class Player:
    """Play tracks from Bandcamp's Discover page."""

    def __init__(self) -> None:
        self._driver = self._set_up_driver()
        self.page = DiscoverPage(self._driver)
        self.tracklist = self.page.discover_tracklist
        self._current_track = self.tracklist.available_tracks[0]

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        """Close the headless browser."""
        self._driver.quit()

    def play(self, track_number=None):
        """Play the first track, or one of the available numbered tracks."""
        if track_number:
            self._current_track = self.tracklist.available_tracks[track_number - 1]
        self._current_track.play()

    def pause(self):
        """Pause the current track."""
        self._current_track.pause()

    def _set_up_driver(self):
        """Create a headless browser pointing to Bandcamp."""
        options = Options()
        options.add_argument("--headless")
        browser = Firefox(options=options)
        browser.get(BANDCAMP_DISCOVER_URL)
        return browser
