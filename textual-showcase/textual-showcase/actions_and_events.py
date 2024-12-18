from itertools import cycle
from textual import on
from textual.app import App
from textual.containers import Horizontal
from textual.widgets import Button, Label, Footer 

COLORS = cycle (['red','yellow','blue','green'])
FRAMES = cycle(['dashed','double','inner','round'])
TEXT ="""[b]Dock this label[/b]:\n
:backhand_index_pointing_up: [@click=app.set_dock('top')]Top[/]\n
:backhand_index_pointing_right: [@click=app.set_dock('right')]Right[/]\n
:backhand_index_pointing_down: [@click=app.set_dock('bottom')]Bottom[/]\n
:backhand_index_pointing_left: [@click=app.set_dock('left')]Left[/]\n
"""

class ActionApp(App):
    CSS_PATH = "actions_and_events.tcss"
    BINDINGS = [
        ("t", "set_dock('top')","Top"),
        ("b", "set_dock('bottom')","Bottom"),
        ("l", "set_dock('left')","Left"),
        ("r", "set_dock('right')","Right"),
    ]

    def compose(self):
        yield Label(TEXT, id="output")  
        with Horizontal():
            yield Button("Change Frame", id="change_frame") 
            yield Button("Change Color", id="change_color")
        yield Footer()

    @on(Button.Pressed, "#change_frame")
    def change_frame(self):
        target = self.query_one("#output", Label)
        target.styles.border = (f"{next(FRAMES)}", "ansi_white")
      
    @on(Button.Pressed, "#change_color")
    def change_color(self):
        target = self.query_one("#output", Label)
        target.styles.background = next(COLORS)
   
    def action_set_dock(self, dock):
        target = self.query_one("#output", Label)
        target.styles.dock = dock
  
if __name__ == "__main__":
    app = ActionApp()
    app.run()