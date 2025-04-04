from selenium.webdriver.common.by import By


class DiscoverPageLocator:
    DISCOVER_RESULTS = (By.CLASS_NAME, "results-grid")
    COOKIE_ACCEPT_NECESSARY = (
        By.CSS_SELECTOR,
        "#cookie-control-dialog button.g-button.outline",
    )


class TrackListLocator:
    ITEM = (By.CLASS_NAME, "results-grid-item")
    PAGINATION_BUTTON = (By.ID, "view-more")


class TrackLocator:
    PLAY_BUTTON = (By.CSS_SELECTOR, "button.play-pause-button")
    URL = (By.CSS_SELECTOR, "div.meta p a")
    ALBUM = (By.CSS_SELECTOR, "div.meta p a strong")
    GENRE = (By.CSS_SELECTOR, "div.meta p.genre")
    ARTIST = (By.CSS_SELECTOR, "div.meta p a span")
