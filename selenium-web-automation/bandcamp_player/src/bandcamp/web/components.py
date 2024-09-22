"""
Abstractions over page fragments that appear on the Bandcamp home page.
"""

import time

from selenium.webdriver.common.by import By

from bandcamp.storage.models import Track
from bandcamp.web.base import FindBy, WebComponent


class Player(WebComponent):
    LOCATOR = (By.CSS_SELECTOR, ".discover-detail-inner")

    _play_button = FindBy(By.CSS_SELECTOR, ".playbutton")
    _title = FindBy(By.CSS_SELECTOR, ".title")
    _album = FindBy(By.CSS_SELECTOR, ".detail-album a")
    _artist = FindBy(By.CSS_SELECTOR, ".detail-artist a")

    @property
    def current_track(self) -> Track:
        return Track(
            title=self._title.text,
            album=self._album.text,
            album_url=self._album.get_attribute("href"),
            artist=self._artist.text,
            artist_url=self._artist.get_attribute("href"),
        )

    def play(self) -> None:
        if not self.is_playing():
            self._play_button.click()
            self._wait.until(lambda _: self.is_playing())

    def pause(self) -> None:
        if self.is_playing():
            self._play_button.click()
            self._wait.until(lambda _: not self.is_playing())

    def is_playing(self) -> bool:
        return "playing" in self._play_button.get_attribute("class")


class PagerButton(WebComponent):
    def click(self) -> None:
        if self.is_clickable():
            self._parent.click()

    def is_clickable(self) -> bool:
        return "disabled" not in self._parent.get_attribute("class")


class TrackItem(WebComponent):
    _title = FindBy(By.CSS_SELECTOR, ".item-title", cache=False)
    _artist = FindBy(By.CSS_SELECTOR, ".item-artist", cache=False)
    _genre = FindBy(By.CSS_SELECTOR, ".item-genre", cache=False)

    @property
    def track(self) -> Track:
        return Track(
            title=self._title.text,
            artist=self._artist.text,
            artist_url=self._artist.get_attribute("href"),
            genre=self._genre.text,
        )

    def play(self) -> None:
        self._parent.click()
        self._wait.until(lambda _: not self.is_loading())

    def is_loading(self):
        play_button = self._driver.find_element(
            By.CSS_SELECTOR, ".detail-player .playbutton"
        )
        return "busy" in play_button.get_attribute("class")


class Discover(WebComponent):
    LOCATOR = (By.CSS_SELECTOR, ".discover-results")
    CSS_TRANSITION_SECONDS = 0.5

    track_items: list[TrackItem] = FindBy(
        By.CSS_SELECTOR,
        ".discover-result.result-current .discover-item",
        cache=False,
    )
    _page_number = FindBy(By.CSS_SELECTOR, ".item-page.selected", cache=False)
    _previous: PagerButton = FindBy(
        By.XPATH,
        "//a[contains(@class, 'item-page')][text()='previous']",
        cache=False,
    )
    _next: PagerButton = FindBy(
        By.XPATH,
        "//a[contains(@class, 'item-page')][text()='next']",
        cache=False,
    )

    @property
    def visible_tracks(self) -> list[Track]:
        return [x.track for x in self.track_items]

    @property
    def page_number(self) -> int:
        return int(self._page_number.text)

    def click_previous(self) -> None:
        self._previous.click()
        time.sleep(Discover.CSS_TRANSITION_SECONDS)

    def click_next(self) -> None:
        self._next.click()
        time.sleep(Discover.CSS_TRANSITION_SECONDS)
