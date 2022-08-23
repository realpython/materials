"""Simple Hello, World example with PyQt6."""

import sys

# 1. Import QApplication, and all the required widgets
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

WIN_X = 100
WIN_Y = 100
WIDTH = 280
HEIGHT = 80
LABEL_X = 60
LABEL_Y = 15

# 2. Create an instance of QApplication
app = QApplication(sys.argv)

# 3. Create an instance of your application's GUI
window = QWidget()
window.setWindowTitle("PyQt App")
window.setGeometry(WIN_X, WIN_Y, WIDTH, HEIGHT)
helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window)
helloMsg.move(LABEL_X, LABEL_Y)

# 4.Show your application's GUI
window.show()

# 5. Run your application's event loop
sys.exit(app.exec())
