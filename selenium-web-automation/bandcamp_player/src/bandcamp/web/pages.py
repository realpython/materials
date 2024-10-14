"""
Page objects modeling the individual views.
"""

from bandcamp.web.base import FindBy, WebPage
from bandcamp.web.components import Discover, Player

BANDCAMP_URL = "https://bandcamp.com/"


class BandcampHome(WebPage):
    player: Player = FindBy(*Player.LOCATOR)
    discover: Discover = FindBy(*Discover.LOCATOR)
