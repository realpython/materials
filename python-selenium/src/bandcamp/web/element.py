from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

from bandcamp.web.base import Track, WebComponent
from bandcamp.web.locators import DiscoverPageLocator, TrackLocator


class TrackElement(WebComponent):
    """Model a playable track in Bandcamp's Discover section."""

    def play(self) -> None:
        """Play the track."""
        if not self.is_playing:
            self._get_play_button().click()

    def pause(self) -> None:
        """Pause the track."""
        if self.is_playing:
            self._get_play_button().click()

    @property
    def is_playing(self) -> bool:
        return "Pause" in self._get_play_button().get_attribute("aria-label")

    def _get_track_info(self) -> Track:
        """Create a representation of the track's relevant information."""
        full_url = self._parent.find_element(*TrackLocator.URL).get_attribute("href")
        # Cut off the referrer query parameter
        clean_url = full_url.split("?")[0] if full_url else ""
        # Some tracks don't have a genre
        try:
            genre = self._parent.find_element(*TrackLocator.GENRE).text
        except NoSuchElementException:
            genre = ""
        return Track(
            album=self._parent.find_element(*TrackLocator.ALBUM).text,
            artist=self._parent.find_element(*TrackLocator.ARTIST).text,
            genre=genre,
            url=clean_url,
        )

    def _get_play_button(self):
        return self._parent.find_element(*TrackLocator.PLAY_BUTTON)


class DiscoverTrackList(WebComponent):
    """Model the track list in Bandcamp's Discover section."""

    def __init__(self, parent: WebElement, driver: WebDriver = None) -> None:
        super().__init__(parent, driver)
        self.available_tracks = self._get_available_tracks()

    def load_more(self) -> None:
        """Load additional tracks in the Discover section."""
        view_more_button = self._driver.find_element(
            *DiscoverPageLocator.PAGINATION_BUTTON
        )
        view_more_button.click()
        # The button is disabled until all new tracks are loaded.
        self._wait.until(EC.element_to_be_clickable(DiscoverPageLocator.PAGINATION_BUTTON))
        self.available_tracks = self._get_available_tracks()

    def _get_available_tracks(self) -> list:
        """Find all currently available tracks in the Discover section."""
        self._wait.until(
            self._track_text_loaded,
            message="Timeout waiting for track text to load",
        )

        all_items = self._driver.find_elements(*DiscoverPageLocator.ITEM)
        all_tracks = []
        for item in all_items:
            if item.find_element(*TrackLocator.PLAY_BUTTON):
                all_tracks.append(item)

        # Filter tracks that are displayed and have text.
        return [
            track for track in all_tracks if track.is_displayed() and track.text.strip()
        ]

    def _track_text_loaded(self, driver):
        """Check if the track text has loaded."""
        return any(
            e.is_displayed() and e.text.strip()
            for e in driver.find_elements(*DiscoverPageLocator.ITEM)
        )
