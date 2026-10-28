import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication

from notely.controllers import NoteController
from notely.models import NoteStore
from notely.resources import app_icon
from notely.views import MainWindow

DEFAULT_STORE_PATH = Path.home() / ".notely.json"


def create_main_window(store_path=DEFAULT_STORE_PATH):
    """Wire the model, view, and controller together."""
    store = NoteStore(store_path)
    window = MainWindow()
    window.setWindowIcon(app_icon())
    window.controller = NoteController(store, window)
    return window


def main():
    app = QApplication(sys.argv)
    window = create_main_window()
    window.show()
    sys.exit(app.exec())
