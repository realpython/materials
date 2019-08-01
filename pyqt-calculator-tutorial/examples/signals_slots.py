# filename: signals_slots.py

"""Signals, and Slots example."""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QVBoxLayout


def greeting():
    msg.setText('Hello World!')


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Signals, and Slots')
layout = QVBoxLayout()
btn = QPushButton('Greet')
btn.clicked.connect(greeting)
layout.addWidget(btn)
msg = QLabel('')
layout.addWidget(msg)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
