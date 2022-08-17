"""PyCalc is a simple calculator built with Python and PyQt."""

import sys
from functools import partial
from typing import NamedTuple

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

ERROR_MSG = "ERROR"
WINDOW_SIZE = 235
DISPLAY_HEIGHT = 35
BUTTON_SIZE = 40


class GridPosition(NamedTuple):
    row: int
    col: int


class PyCalcWindow(QMainWindow):
    """PyCalc's main window (GUI or view)."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyCalc")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(DISPLAY_HEIGHT)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        self.buttonMap = {}
        buttonsLayout = QGridLayout()
        # Key Symbol | Key position
        keyMap = {
            "7": GridPosition(0, 0),
            "8": GridPosition(0, 1),
            "9": GridPosition(0, 2),
            "/": GridPosition(0, 3),
            "C": GridPosition(0, 4),
            "4": GridPosition(1, 0),
            "5": GridPosition(1, 1),
            "6": GridPosition(1, 2),
            "*": GridPosition(1, 3),
            "(": GridPosition(1, 4),
            "1": GridPosition(2, 0),
            "2": GridPosition(2, 1),
            "3": GridPosition(2, 2),
            "-": GridPosition(2, 3),
            ")": GridPosition(2, 4),
            "0": GridPosition(3, 0),
            "00": GridPosition(3, 1),
            ".": GridPosition(3, 2),
            "+": GridPosition(3, 3),
            "=": GridPosition(3, 4),
        }

        for keySymbol, keyPosition in keyMap.items():
            self.buttonMap[keySymbol] = QPushButton(keySymbol)
            self.buttonMap[keySymbol].setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
            buttonsLayout.addWidget(
                self.buttonMap[keySymbol], keyPosition.row, keyPosition.col
            )

        self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self, text):
        """Set the display's text."""
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        """Get the display's text."""
        return self.display.text()

    def clearDisplay(self):
        """Clear the display."""
        self.setDisplayText("")


def evaluateExpression(expression):
    """Evaluate an expression (Model)."""
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MSG
    return result


class PyCalc:
    """PyCalc's controller class."""

    def __init__(self, model, view):
        self._evaluate = model
        self._view = view
        self._connectSignalsAndSlots()

    def _calculateResult(self):
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)

    def _buildExpression(self, sub_exp):
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()
        expression = self._view.displayText() + sub_exp
        self._view.setDisplayText(expression)

    def _connectSignalsAndSlots(self):
        for keySymbol, button in self._view.buttonMap.items():
            if keySymbol not in {"=", "C"}:
                button.clicked.connect(
                    partial(self._buildExpression, keySymbol)
                )
        self._view.buttonMap["="].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttonMap["C"].clicked.connect(self._view.clearDisplay)


def main():
    """PyCalc's main function."""
    pycalcApp = QApplication([])
    pycalcWindow = PyCalcWindow()
    pycalcWindow.show()
    PyCalc(model=evaluateExpression, view=pycalcWindow)
    sys.exit(pycalcApp.exec())


if __name__ == "__main__":
    main()
