from importlib.resources import as_file, files

from PySide6.QtGui import QIcon


def app_icon():
    """Return the app icon that ships inside the package."""
    with as_file(files("notely.resources") / "icons" / "notely.svg") as path:
        return QIcon(str(path))
