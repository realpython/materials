# Filename: h_layout.py

"""Horizontal layout example."""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("QHBoxLayout")
layout = QHBoxLayout()
layout.addWidget(QPushButton("Left"))
layout.addWidget(QPushButton("Center"))
layout.addWidget(QPushButton("Right"))
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
