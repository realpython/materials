from textual import on
from textual.widgets import Button, DataTable, Label, Static

from bandcamp.tui.state import PlayerStateMixin, PlaylistStateMixin


class Player(PlayerStateMixin, Static):
    def compose(self):
        yield Button("Play", variant="success", id="play")
        yield Button("Pause", variant="error", id="pause", classes="hidden")
        yield Label("N/A", id="current_track")

    @on(Button.Pressed, "#play")
    def on_play_click(self):
        self.call_after_refresh(self.app.action_toggle_play)

    @on(Button.Pressed, "#pause")
    def on_pause_click(self):
        self.call_after_refresh(self.app.action_toggle_play)


class Playlist(PlaylistStateMixin, Static):
    def compose(self):
        table = DataTable(id="table")
        table.cursor_type = "row"
        table.add_columns("Track", "Title", "Artist", "Genre")
        table.move_cursor(row=0)
        table.focus()
        yield table
        with Static(id="pager-buttons"):
            yield Button("Next Page ›", id="next")
            yield Button("‹ Previous Page", id="previous")

    @on(Button.Pressed, "#next")
    def on_next_click(self):
        self.call_after_refresh(self.move_next)

    @on(Button.Pressed, "#previous")
    def on_previous_click(self):
        self.call_after_refresh(self.move_previous)

    @on(DataTable.RowSelected, "#table")
    def on_row_selected(self, event):
        self.call_after_refresh(self.play_row, event.cursor_row)
