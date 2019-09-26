# Filename: signals_slots_partial.py

"""Signals and slots example."""

import functools
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget


def greeting(who):
    """Slot function."""
    if msg.text():
        msg.setText("")
    else:
        msg.setText(f"Hello {who}")


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Signals, and Slots")
layout = QVBoxLayout()

btn = QPushButton("Greet")
btn.clicked.connect(functools.partial(greeting, "World!"))

layout.addWidget(btn)
msg = QLabel("")
layout.addWidget(msg)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
