from importlib.resources import as_file, files

from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QMainWindow


def load_ui(name, parent=None):
    """Load a Qt Designer .ui file that ships inside the package."""
    resource = files("notely.views") / "ui" / name
    with as_file(resource) as path:
        return QUiLoader().load(str(path), parent)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = load_ui("main_window.ui", self)
        self.setCentralWidget(self.ui)
        self.setWindowTitle("Notely")
        self.resize(640, 400)
        self.notes_list = self.ui.notesList
        self.editor = self.ui.editor
        self.new_button = self.ui.newButton
        self.save_button = self.ui.saveButton
