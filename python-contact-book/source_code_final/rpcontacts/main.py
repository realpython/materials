# -*- coding: utf-8 -*-

"""This module provides RP Contacts application."""

import sys

from PyQt5.QtWidgets import QApplication

from .database import createConnection
from .views import Window


def main():
    """RP Contacts main function."""
    # Create the application
    app = QApplication(sys.argv)
    # Connect to the database before creating any window
    if not createConnection("contacts.sqlite"):
        sys.exit(1)
    # Create the main window if the connection succeeded
    win = Window()
    win.show()
    # Run the event loop
    sys.exit(app.exec_())
