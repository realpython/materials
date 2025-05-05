from textual.app import App
from textual.widgets import Footer, Header

from bandcamp.tui.state import AppStateMixin
from bandcamp.tui.widgets import Player, Playlist


class BandcampApp(AppStateMixin, App):
    CSS_PATH = "app.css"
    TITLE = "Bandcamp Player"
    BINDINGS = [
        ("q", "quit", "Quit"),
        ("space", "toggle_play", "Play/Pause"),
    ]

    def __init__(self, storage_worker, web_worker):
        super().__init__()
        self.storage_worker = storage_worker
        self.web_worker = web_worker

    def compose(self):
        yield Header()
        yield Footer()
        yield Player(classes="horizontal")
        yield Playlist(classes="horizontal")
