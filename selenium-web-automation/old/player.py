import atexit
import csv
import logging
import threading
from dataclasses import asdict, dataclass, fields
from pathlib import Path
from time import ctime, sleep
from typing import List, Optional

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

logging.basicConfig(level=logging.INFO)

BANDCAMP_FRONTPAGE = "https://bandcamp.com/"
DEFAULT_DB_PATH = "bandcamp_history.csv"
DB_REGISTRATION_DELAY = 0.5
DB_CHECK_DELAY = 20


@dataclass
class TrackRec:
    title: str
    artist: str
    artist_url: str
    album: str
    album_url: str
    timestamp: str


class BandLeader:
    """A class to control playback of Bandcamp music using Selenium."""

    def __init__(self, csv_path: str = DEFAULT_DB_PATH):
        """Initialize a BandLeader object.

        Args:
            csv_path (str): The path to the CSV file
                            to load/save track records.
        """
        self.browser = self._set_up_bandcamp_browser()
        self._lock = threading.RLock()
        atexit.register(self._close_headless_browser)

        self.database_path = Path(csv_path)
        self.temp_database: List[TrackRec] = self._load_db_state()
        self._current_track_record: Optional[TrackRec] = None

        self.db_update_thread = threading.Thread(
            target=self._maintain, daemon=True
        )
        self.db_update_thread.start()

        self._current_track_number = 0
        self.playable_tracks = self._fetch_tracks()
        self.skip_song = False
        self.stop_stream = False

        self.show_tracks()

    def __enter__(self):
        """Enter the runtime context related to this object."""
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Exit the runtime context."""
        self._close_headless_browser()

    # Public Methods - Playback Control
    def play(self, track: Optional[int] = None):
        """Play a track.

        If no track number is supplied, the presently selected track will play.
        If no track has been selected yet, the first track will play.

        Args:
            track (Optional[int]): The track number to play.
        """
        print("\nNow playing:")
        with self._lock:
            if track is None:
                play_button = self.browser.find_element(
                    By.CLASS_NAME, "playbutton"
                )
                play_button.click()
                self._current_track_number = 1
                self._show_track_info(1)
            elif 1 <= track <= len(self.playable_tracks):
                self._current_track_number = track
                self.playable_tracks[self._current_track_number - 1].click()
                self._show_track_info(track)
            else:
                logging.error(f"Invalid track number: {track}")
                return

            try:
                WebDriverWait(self.browser, 10).until(
                    lambda driver: self._is_playing()
                )
                if self._is_playing():
                    self._current_track_record = self.currently_playing()
            except Exception as e:
                logging.error(f"Error starting playback: {e}")

    def pause(self):
        """Pause and unpause the playback."""
        with self._lock:
            try:
                play_button = self.browser.find_element(
                    By.CLASS_NAME, "playbutton"
                )
                play_button.click()
            except NoSuchElementException:
                logging.error("Play button not found, can't pause playback")

    def currently_playing(self) -> Optional[TrackRec]:
        """Get the record for the currently playing track.

        Returns:
            Optional[TrackRec]: The currently playing track information,
                                or None if nothing is playing.
        """
        try:
            with self._lock:
                if self._is_playing():
                    player_element = self.browser.find_element(
                        By.CLASS_NAME, "discover-detail"
                    )
                    title = player_element.find_element(
                        By.CLASS_NAME, "title"
                    ).text
                    album_element = player_element.find_element(
                        By.CLASS_NAME, "detail-album"
                    )
                    album_title = album_element.text
                    album_url = (
                        album_element.find_element(By.TAG_NAME, "a")
                        .get_attribute("href")
                        .split("?")[0]
                    )
                    artist_element = player_element.find_element(
                        By.CLASS_NAME, "detail-artist"
                    ).find_element(By.TAG_NAME, "a")
                    artist = artist_element.text
                    artist_url = artist_element.get_attribute("href").split(
                        "?"
                    )[0]

                    return TrackRec(
                        title=title,
                        artist=artist,
                        artist_url=artist_url,
                        album=album_title,
                        album_url=album_url,
                        timestamp=ctime(),
                    )
        except NoSuchElementException as e:
            logging.error(f"Element not found in currently_playing(): {e}")
        except Exception as e:
            logging.error(f"There was an error in currently_playing(): {e}")

        return None

    def stream(self):
        """Begin streaming music, listening for user commands."""
        input_thread = threading.Thread(target=self._listen_for_input)
        input_thread.start()

        while not self.stop_stream:
            if self.skip_song:
                self._play_next()
                self.skip_song = False

            if not self._is_playing():
                self.play()

            sleep(0.1)

        input_thread.join()

    def show_tracks(self):
        """Print the available tracks to the screen."""
        for number, _ in enumerate(self.playable_tracks, start=1):
            self._show_track_info(number)

    def get_new_tracks(self):
        """Advance the catalogue and repopulate the track list."""
        if self._is_playing():
            self.pause()

        with self._lock:
            page_buttons = self.browser.find_elements(
                By.CLASS_NAME, "item-page"
            )
            next_btn = page_buttons[-1] if page_buttons else None

            if next_btn:
                next_btn.click()
                self.playable_tracks = self._fetch_tracks()
                self.show_tracks()
                self._current_track_number = 1
            else:
                logging.error("Next button not found, can't get new tracks")

    # Private Methods - Browser Management
    def _set_up_bandcamp_browser(self) -> Firefox:
        """Create a headless browser pointing to BandCamp."""
        options = Options()
        options.add_argument("--headless")
        browser = Firefox(options=options)
        browser.get(BANDCAMP_FRONTPAGE)
        WebDriverWait(browser, 10).until(EC.title_contains("Bandcamp"))
        logging.info("Bandcamp page loaded successfully.")
        return browser

    def _close_headless_browser(self):
        """Close the headless browser."""
        if self.browser:
            with self._lock:
                logging.info("Closing headless browser...")
                self.browser.quit()
                self.browser = None

    # Private Methods - Database Maintenance
    def _load_db_state(self) -> List[TrackRec]:
        """Load database from disk, or create new empty file."""
        if self.database_path and self.database_path.is_file():
            with self.database_path.open(newline="") as dbfile:
                dbreader = csv.DictReader(dbfile)
                return [TrackRec(**rec) for rec in dbreader]
        else:
            logging.info("No existing database found. Starting fresh.")
            Path.cwd().joinpath(self.database_path).touch()
            return []

    def _maintain(self):
        """Background thread that updates the database at intervals."""
        while True:
            self._update_db()
            sleep(DB_CHECK_DELAY)

    def _update_db(self):
        """Check the currently playing track and update the database."""
        try:
            needs_update = (
                self._current_track_record is not None
                and (
                    not self.temp_database
                    or self.temp_database[-1] != self._current_track_record
                )
                and self._is_playing()
            )
            if needs_update:
                self.temp_database.append(self._current_track_record)
                self._save_db()
                logging.info(
                    f"Added track to database: {self._current_track_record}"
                )
        except Exception as e:
            logging.error(f"Error while updating the db: {e}")

    def _save_db(self):
        """Save the current database to CSV file."""
        if self.database_path:
            try:
                with self.database_path.open(mode="w", newline="") as dbfile:
                    fieldnames = [field.name for field in fields(TrackRec)]
                    dbwriter = csv.DictWriter(dbfile, fieldnames=fieldnames)
                    dbwriter.writeheader()
                    for record in self.temp_database:
                        dbwriter.writerow(asdict(record))
                logging.info(f"Database saved to {self.database_path}")
            except Exception as e:
                logging.error(f"Error while saving the db: {e}")

    # Private Methods - Input Handling
    def _listen_for_input(self):
        """Listen for user input to control the stream."""
        while not self.stop_stream:
            try:
                user_input = input().lower()
                if user_input == "q":
                    self.stop_stream = True
                    print("Exiting stream...")
                    self.pause()
                elif user_input == "n":
                    self.skip_song = True
                    print("Skipping to next song...")
            except EOFError:
                break

    # Private Methods - Playback Helpers
    def _is_playing(self) -> bool:
        """Check if a track is currently playing.

        Returns:
            bool: True if a track is playing, False otherwise.
        """
        with self._lock:
            try:
                playbtn = self.browser.find_element(
                    By.CLASS_NAME, "playbutton"
                )
                return "playing" in playbtn.get_attribute("class")
            except NoSuchElementException:
                logging.error("Play button not found in ._is_playing()")
                return False

    def _play_next(self):
        """Play the next available track."""
        self._current_track_number += 1
        if self._current_track_number <= len(self.playable_tracks):
            self.play(self._current_track_number)
        else:
            self.get_new_tracks()
            self.play(1)

    # Private Methods - Track Management
    def _fetch_tracks(self):
        """Query the page to populate a list of available tracks."""
        with self._lock:
            try:
                WebDriverWait(self.browser, 10).until(
                    EC.presence_of_all_elements_located(
                        (By.CLASS_NAME, "discover-item")
                    )
                )
                all_tracks = self.browser.find_elements(
                    By.CLASS_NAME, "discover-item"
                )
                return [track for track in all_tracks if track.is_displayed()]
            except Exception as e:
                logging.error(f"Error fetching tracks: {e}")
                return []

    def _show_track_info(self, track_number: int):
        """Show information about a specific track.

        Args:
            track_number (int): The track number to display information about.
        """
        try:
            track = self.playable_tracks[track_number - 1]
            album, artist, *genre = track.text.split("\n")
            info = (
                f"[{track_number}]\n"
                f"Album  : {album}\n"
                f"Artist : {artist}\n"
                f"Genre  : {genre[0]}\n"
                if genre
                else "\n"
            )
            print(info)
        except IndexError:
            logging.error(f"Track number {track_number} is out of range")


if __name__ == "__main__":
    with BandLeader(csv_path="band_db.csv") as band_leader:
        band_leader.stream()
