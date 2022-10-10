import tkinter as tk
from queue import Queue
from tkinter import ttk

from tic_tac_toe.game.renderers import Renderer
from tic_tac_toe.logic.models import GameState


class Window(tk.Tk):
    def __init__(self, events: Queue) -> None:
        super().__init__()
        self.title("Tic-Tac-Toe")
        self.events = events
        self.buttons = []
        for row in range(3):
            for col in range(3):
                button = ttk.Button(master=self, text="", width=5)
                self.buttons.append(button)
                button.bind("<ButtonPress-1>", self.on_button_click)
                button.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, event):
        clicked_button = event.widget
        self.events.put(self.buttons.index(clicked_button))


class WindowRenderer(Renderer):
    def __init__(self, window: Window) -> None:
        self.window = window

    def render(self, game_state: GameState) -> None:
        for label, button in zip(game_state.grid.cells, self.window.buttons):
            button.config(text=label)
        if game_state.winner:
            self.window.title(f"{game_state.winner} wins \N{party popper}")
            bold_style = ttk.Style()
            bold_style.configure("Bold.TButton", font=(None, 9, "bold"))
            for i in game_state.winning_cells:
                self.window.buttons[i].config(style="Bold.TButton")
        elif game_state.tie:
            self.window.title("Tie \N{neutral face}")
