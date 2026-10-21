import queue
import threading

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from bandcamp.web.pages import BANDCAMP_URL, BandcampHome
from bandcamp.workers.messages import Message


class WebWorker(threading.Thread):
    def __init__(self):
        super().__init__()
        self.inbox = queue.Queue()
        self.outbox = queue.Queue()

    def run(self):
        driver = open_headless_browser()
        home_page = navigate_home(driver)
        try:
            while True:
                try:
                    match self.inbox.get():
                        case Message.GRACEFUL_STOP:
                            break
                        case [Message.PLAY_TRACK, index]:
                            track = home_page.discover.visible_tracks[index]
                            self.outbox.put(track.title)
                            home_page.discover.track_items[index].play()
                        case Message.PLAY:
                            home_page.player.play()
                        case Message.PAUSE:
                            home_page.player.pause()
                        case Message.CURRENT_TRACK:
                            track = home_page.player.current_track
                            self.outbox.put(track)
                        case Message.FIRST_TRACK:
                            track = home_page.discover.visible_tracks[0]
                            self.outbox.put(track)
                        case Message.PAGE:
                            page_number = home_page.discover.page_number
                            visible_tracks = home_page.discover.visible_tracks
                            self.outbox.put((page_number, visible_tracks))
                        case Message.NEXT_PAGE:
                            home_page.discover.click_next()
                            self.outbox.put(Message.ACKNOWLEDGE)
                        case Message.PREVIOUS_PAGE:
                            home_page.discover.click_previous()
                            self.outbox.put(Message.ACKNOWLEDGE)
                finally:
                    self.inbox.task_done()
        finally:
            if driver:
                driver.close()

    def request(self, message: Message):
        self.inbox.put(message)
        try:
            return self.outbox.get()
        finally:
            self.outbox.task_done()


def open_headless_browser() -> WebDriver:
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    return webdriver.Chrome(options=options)


def navigate_home(driver) -> BandcampHome:
    driver.get(BANDCAMP_URL)
    return BandcampHome(driver)
