from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from bandcamp.web.base import Track, WebComponent
from bandcamp.web.locators import HomePageLocatorMixin, TrackLocatorMixin


class TrackElement(WebComponent, TrackLocatorMixin):
    """Models a playable track in Bandcamp's Discover section."""

    def play(self) -> None:
        """Plays the track."""
        if not self.is_playing():
            self._get_play_button().click()
            self._wait.until(lambda _: self.is_playing())

    def is_playing(self) -> bool:
        return "playing" in self._get_play_button().get_attribute("class")

    def _get_track_info(self) -> Track:
        """Creates a representation of the track's relevant information."""
        full_url = self._parent.find_element(*self.ALBUM).get_attribute("href")
        # Cut off the referrer query parameter
        clean_url = full_url.split("?")[0] if full_url else ""
        return Track(
            album=self._parent.find_element(*self.ALBUM).text,
            artist=self._parent.find_element(*self.ARTIST).text,
            genre=self._parent.find_element(*self.GENRE).text,
            url=clean_url,
        )

    def _get_play_button(self):
        return self._parent.find_element(*self.PLAY_BUTTON)


class DiscoverTrackList(WebComponent, HomePageLocatorMixin):
    """Models the track list in Bandcamp's Discover section."""

    def __init__(self, parent: WebElement, driver: WebDriver = None) -> None:
        super().__init__(parent, driver)
        self.available_tracks = self._get_available_tracks()

    def load_more(self) -> None:
        """Loads additional tracks in the Discover section."""
        self._get_next_page_button().click()
        self.available_tracks = self._get_available_tracks()

    def _get_available_tracks(self) -> list:
        """Finds all currently available tracks in the Discover section."""
        all_tracks = self._driver.find_elements(*self.TRACK)
        return [track for track in all_tracks if track.is_displayed()]

    def _get_next_page_button(self):
        """Locates and returns the 'Next' button that loads more results."""
        return self._driver.find_elements(*self.PAGINATION_BUTTON)[-1]
