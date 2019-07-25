#!/usr/bin/env python3

# filename: pycalc.py

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""PyCalc is a simple calculator built using Python, and PyQt5."""

import sys
from functools import partial

# 1. Import QApplication, and the required widgets from PyQt5.QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt

__version__ = '0.1'
__author__ = 'Leodanis Pozo Ramos'

ERROR_MSG = 'ERROR'


# 2. Create a subclass of QMainWindow to setup the application's GUI
class PyCalcUi(QMainWindow):
    """PyCalc's View (GUI)."""

    def __init__(self):
        """View initializer."""
        super().__init__()
        # Set some main window's properties
        self.setWindowTitle('PyCalc')
        self.setFixedSize(235, 235)
        # Create and set the central widget, and the general layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        # Create the display, and the buttons
        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        """Create the display."""
        # Create the display widget
        self.display = QLineEdit()
        # Set some display's properties
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        # Add the display to the general layout
        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        """Create the buttons."""
        self.buttons = {}
        buttonsLayout = QGridLayout()
        #     btn_text | position in the QGridLayout
        buttons = {'7': (0, 0),
                   '8': (0, 1),
                   '9': (0, 2),
                   '/': (0, 3),
                   'C': (0, 4),
                   '4': (1, 0),
                   '5': (1, 1),
                   '6': (1, 2),
                   '*': (1, 3),
                   '(': (1, 4),
                   '1': (2, 0),
                   '2': (2, 1),
                   '3': (2, 2),
                   '-': (2, 3),
                   ')': (2, 4),
                   '0': (3, 0),
                   '00': (3, 1),
                   '.': (3, 2),
                   '+': (3, 3),
                   '=': (3, 4),
                   }
        # Create the buttons
        for btn_text, pos in buttons.items():
            self.buttons[btn_text] = QPushButton(btn_text)
            self.buttons[btn_text].setFixedSize(40, 40)
            buttonsLayout.addWidget(self.buttons[btn_text], pos[0], pos[1])
        # Add the buttons to the general layout
        self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self, text):
        """Set display's text."""
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        """Get display's text."""
        return self.display.text()

    def clearDisplay(self):
        """Clear the display."""
        self.setDisplayText('')


# 6. Create a Controller class to connect the GUI and the Model
class PyCalcCtrl:
    """PyCalc Controller class."""

    def __init__(self, view):
        """Controller initializer."""
        super(PyCalcCtrl, self).__init__()
        self._view = view
        # Connect signals and slots
        self._connectSignals()

    def _buildExpression(self, sub_exp):
        """Build expression."""
        expression = self._view.displayText() + sub_exp
        self._view.setDisplayText(expression)

    def _connectSignals(self):
        """Connect signals and slots."""
        for btn_text, btn in self._view.buttons.items():
            if btn_text not in {'=', 'C'}:
                btn.clicked.connect(partial(self._buildExpression, btn_text))

        self._view.buttons['C'].clicked.connect(self._view.clearDisplay)


# 7. Create a Model to handle the application's data
def evaluateExpression(expression):
    """Evaluate an expression."""
    try:
        result = str(eval(expression, {}, {}))
    except:
        result = ERROR_MSG

    return result


# Client code
def main():
    """Main function."""
    # 3. Create an instance of the application's GUI
    pycalc = QApplication(sys.argv)

    # 4. Create an instance of the application's GUI
    view = PyCalcUi()

    # 5. Run .show() on the GUI instance
    view.show()

    # 9. Create an instance of the Controller
    ctrl = PyCalcCtrl(view=view)

    # 10. Execute the application's main loop
    sys.exit(pycalc.exec_())


if __name__ == '__main__':
    main()
