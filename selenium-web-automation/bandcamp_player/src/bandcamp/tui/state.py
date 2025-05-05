from rich.text import Text
from textual.widgets import DataTable, Label

from bandcamp.workers.messages import Message


class AppStateMixin:
    def action_toggle_play(self):
        if self.query_one("#play").has_class("hidden"):
            self.query_one("#pause").add_class("hidden")
            self.query_one("#play").remove_class("hidden")
            self.call_after_refresh(self.pause)
        else:
            self.query_one("#play").add_class("hidden")
            self.query_one("#pause").remove_class("hidden")
            self.call_after_refresh(self.play)
            self.call_after_refresh(self.persist_current_track)

    def play(self):
        self.web_worker.inbox.put(Message.PLAY)

    def pause(self):
        self.web_worker.inbox.put(Message.PAUSE)

    def persist_current_track(self):
        track = self.web_worker.request(Message.CURRENT_TRACK)
        self.storage_worker.inbox.put(track)


class PlayerStateMixin:
    def on_mount(self):
        label = self.query_one("#current_track", Label)
        track = self.app.web_worker.request(Message.FIRST_TRACK)
        label.update(track.title)


class PlaylistStateMixin:
    def on_mount(self):
        self.update_table()

    def move_next(self):
        self.app.web_worker.request(Message.NEXT_PAGE)
        self.update_table()

    def move_previous(self):
        self.app.web_worker.request(Message.PREVIOUS_PAGE)
        self.update_table()

    def play_row(self, index: int):
        title = self.app.web_worker.request((Message.PLAY_TRACK, index))
        self.app.query_one("#current_track", Label).update(title)
        self.app.query_one("#play").add_class("hidden")
        self.app.query_one("#pause").remove_class("hidden")
        self.call_after_refresh(self.app.persist_current_track)

    def update_table(self):
        page_number, visible_tracks = self.app.web_worker.request(Message.PAGE)
        offset = 8 * (page_number - 1)
        rows = [
            [
                Text(f"{offset + i}.", justify="right"),
                track.title,
                track.artist,
                track.genre,
            ]
            for i, track in enumerate(visible_tracks, 1)
        ]
        table = self.query_one("#table", DataTable)
        table.clear()
        table.add_rows(rows)
