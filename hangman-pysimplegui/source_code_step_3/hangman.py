import PySimpleGUI as sg


class Hangman:
    def __init__(self) -> None:
        self._window = sg.Window(
            title="Hangman", layout=[[]], finalize=True, margins=(100, 100)
        )

    def read_event(self):
        return self._window.read()

    def close(self):
        self._window.close()


if __name__ == "__main__":
    game = Hangman()
    # Event loop
    while True:
        event, values = game.read_event()
        if event in {sg.WIN_CLOSED}:
            break
    game.close()
