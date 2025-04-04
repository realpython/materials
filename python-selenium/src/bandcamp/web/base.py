from dataclasses import dataclass
from pprint import pformat

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

MAX_WAIT_SECONDS = 10.0
DEFAULT_WINDOW_SIZE = (1920, 3000)


@dataclass
class Track:
    album: str
    artist: str
    genre: str
    url: str

    def __str__(self):
        return pformat(self)


class WebPage:
    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver
        self._driver.set_window_size(*DEFAULT_WINDOW_SIZE)
        self._driver.implicitly_wait(5)
        self._wait = WebDriverWait(driver, MAX_WAIT_SECONDS)


class WebComponent(WebPage):
    def __init__(self, parent: WebElement, driver: WebDriver) -> None:
        super().__init__(driver)
        self._parent = parent
