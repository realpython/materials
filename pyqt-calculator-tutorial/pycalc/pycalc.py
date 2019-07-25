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

# 1. Import QApplication, and the required widgets from PyQt5.QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget

__version__ = '0.1'
__author__ = 'Leodanis Pozo Ramos'


# 2. Create a subclass of QMainWindow to setup the application's GUI
class PyCalcUi(QMainWindow):
    """PyCalc's View (GUI)."""

    def __init__(self):
        """View initializer."""
        super().__init__()
        # Set some main window's properties
        self.setWindowTitle('PyCalc')
        self.setFixedSize(235, 235)
        # Create and set the central widget
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)


# Client code
def main():
    """Main function."""
    # 3. Create an instance of the application's GUI
    pycalc = QApplication(sys.argv)

    # 4. Create an instance of the application's GUI
    view = PyCalcUi()

    # 5. Run .show() on the GUI instance
    view.show()

    # 10. Execute the application's main loop
    sys.exit(pycalc.exec_())


if __name__ == '__main__':
    main()
