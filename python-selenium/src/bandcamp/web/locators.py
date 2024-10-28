from selenium.webdriver.common.by import By


class HomePageLocator:
    DISCOVER_RESULTS = (By.CLASS_NAME, "discover-results")
    TRACK = (By.CLASS_NAME, "discover-item")
    PAGINATION_BUTTON = (By.CLASS_NAME, "item-page")


class TrackLocator:
    PLAY_BUTTON = (By.CSS_SELECTOR, "a")
    ALBUM = (By.CLASS_NAME, "item-title")
    GENRE = (By.CLASS_NAME, "item-genre")
    ARTIST = (By.CLASS_NAME, "item-artist")
