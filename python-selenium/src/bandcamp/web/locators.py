from selenium.webdriver.common.by import By


class DiscoverPageLocatorMixin:
    DISCOVER_RESULTS = (By.CLASS_NAME, "results-grid")
    ITEM = (By.CLASS_NAME, "results-grid-item")
    PAGINATION_BUTTON = (By.ID, "view-more")
    COOKIE_ACCEPT_NECESSARY = (
        By.CSS_SELECTOR,
        "#cookie-control-dialog button.g-button.outline",
    )


class TrackLocatorMixin:
    PLAY_BUTTON = (By.CSS_SELECTOR, "button.play-pause-button")
    URL = (By.CSS_SELECTOR, "div.meta p a")
    ALBUM = (By.CSS_SELECTOR, "div.meta p a strong")
    GENRE = (By.CSS_SELECTOR, "div.meta p.genre")
    ARTIST = (By.CSS_SELECTOR, "div.meta p a span")
