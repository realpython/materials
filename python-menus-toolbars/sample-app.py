# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Sample PyQt application."""

import sys
from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QLabel,
    QMainWindow,
    QMenu,
    QSpinBox,
    QToolBar,
)

# NOTE: Uncomment this import to enable icons
# import qrc_resources


class Window(QMainWindow):
    """Main Window."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("Python Menus & Toolbars")
        self.resize(400, 200)
        self.centralWidget = QLabel("Hello, World")
        self.centralWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.centralWidget)
        self._createActions()
        self._createMenuBar()
        self._createToolBars()

        # Uncomment the call to ._createContextMenu() below to create a context
        # menu using menu policies. To test this out, you also need to
        # comment .contextMenuEvent() and uncomment ._createContextMenu()

        # self._createContextMenu()

        self._connectActions()
        self._createStatusBar()

    def _createMenuBar(self):
        menuBar = self.menuBar()
        # File menu
        fileMenu = QMenu("&File", self)
        menuBar.addMenu(fileMenu)
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.openAction)
        # Open Recent submenu
        self.openRecentMenu = fileMenu.addMenu("Open Recent")
        fileMenu.addAction(self.saveAction)
        # Separator
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAction)
        # Edit menu
        editMenu = menuBar.addMenu("&Edit")
        editMenu.addAction(self.copyAction)
        editMenu.addAction(self.pasteAction)
        editMenu.addAction(self.cutAction)
        # Separator
        editMenu.addSeparator()
        # Find and Replace submenu
        findMenu = editMenu.addMenu("Find and Replace")
        findMenu.addAction("Find...")
        findMenu.addAction("Replace...")
        # Help menu
        helpMenu = menuBar.addMenu(QIcon(":help-content.svg"), "&Help")
        helpMenu.addAction(self.helpContentAction)
        helpMenu.addAction(self.aboutAction)

    def _createToolBars(self):
        # File toolbar
        fileToolBar = self.addToolBar("File")
        fileToolBar.setMovable(False)
        fileToolBar.addAction(self.newAction)
        fileToolBar.addAction(self.openAction)
        fileToolBar.addAction(self.saveAction)
        # Edit toolbar
        editToolBar = QToolBar("Edit", self)
        self.addToolBar(editToolBar)
        editToolBar.addAction(self.copyAction)
        editToolBar.addAction(self.pasteAction)
        editToolBar.addAction(self.cutAction)
        # Widgets
        self.fontSizeSpinBox = QSpinBox()
        self.fontSizeSpinBox.setFocusPolicy(Qt.NoFocus)
        editToolBar.addWidget(self.fontSizeSpinBox)

    def _createStatusBar(self):
        self.statusbar = self.statusBar()
        # Temporary message
        self.statusbar.showMessage("Ready", 3000)
        # Permanent widget
        self.wcLabel = QLabel(f"{self.getWordCount()} Words")
        self.statusbar.addPermanentWidget(self.wcLabel)

    def _createActions(self):
        # File actions
        self.newAction = QAction(self)
        self.newAction.setText("&New")
        self.newAction.setIcon(QIcon(":file-new.svg"))
        self.openAction = QAction(QIcon(":file-open.svg"), "&Open...", self)
        self.saveAction = QAction(QIcon(":file-save.svg"), "&Save", self)
        self.exitAction = QAction("&Exit", self)
        # String-based key sequences
        self.newAction.setShortcut("Ctrl+N")
        self.openAction.setShortcut("Ctrl+O")
        self.saveAction.setShortcut("Ctrl+S")
        # Help tips
        newTip = "Create a new file"
        self.newAction.setStatusTip(newTip)
        self.newAction.setToolTip(newTip)
        self.newAction.setWhatsThis("Create a new and empty text file")
        # Edit actions
        self.copyAction = QAction(QIcon(":edit-copy.svg"), "&Copy", self)
        self.pasteAction = QAction(QIcon(":edit-paste.svg"), "&Paste", self)
        self.cutAction = QAction(QIcon(":edit-cut.svg"), "C&ut", self)
        # Standard key sequence
        self.copyAction.setShortcut(QKeySequence.Copy)
        self.pasteAction.setShortcut(QKeySequence.Paste)
        self.cutAction.setShortcut(QKeySequence.Cut)
        # Help actions
        self.helpContentAction = QAction("&Help Content...", self)
        self.aboutAction = QAction("&About...", self)

    # Uncomment this method to create a context menu using menu policies
    # def _createContextMenu(self):
    #     # Setting contextMenuPolicy
    #     self.centralWidget.setContextMenuPolicy(Qt.ActionsContextMenu)
    #     # Populating the widget with actions
    #     self.centralWidget.addAction(self.newAction)
    #     self.centralWidget.addAction(self.openAction)
    #     self.centralWidget.addAction(self.saveAction)
    #     self.centralWidget.addAction(self.copyAction)
    #     self.centralWidget.addAction(self.pasteAction)
    #     self.centralWidget.addAction(self.cutAction)

    def contextMenuEvent(self, event):
        # Context menu
        menu = QMenu(self.centralWidget)
        # Populating the menu with actions
        menu.addAction(self.newAction)
        menu.addAction(self.openAction)
        menu.addAction(self.saveAction)
        # Separator
        separator = QAction(self)
        separator.setSeparator(True)
        menu.addAction(separator)
        menu.addAction(self.copyAction)
        menu.addAction(self.pasteAction)
        menu.addAction(self.cutAction)
        # Launching the menu
        menu.exec(event.globalPos())

    def _connectActions(self):
        # Connect File actions
        self.newAction.triggered.connect(self.newFile)
        self.openAction.triggered.connect(self.openFile)
        self.saveAction.triggered.connect(self.saveFile)
        self.exitAction.triggered.connect(self.close)
        # Connect Edit actions
        self.copyAction.triggered.connect(self.copyContent)
        self.pasteAction.triggered.connect(self.pasteContent)
        self.cutAction.triggered.connect(self.cutContent)
        # Connect Help actions
        self.helpContentAction.triggered.connect(self.helpContent)
        self.aboutAction.triggered.connect(self.about)
        # Connect Open Recent to dynamically populate it
        self.openRecentMenu.aboutToShow.connect(self.populateOpenRecent)

    # Slots
    def newFile(self):
        # Logic for creating a new file goes here...
        self.centralWidget.setText("<b>File > New</b> clicked")

    def openFile(self):
        # Logic for opening an existing file goes here...
        self.centralWidget.setText("<b>File > Open...</b> clicked")

    def saveFile(self):
        # Logic for saving a file goes here...
        self.centralWidget.setText("<b>File > Save</b> clicked")

    def copyContent(self):
        # Logic for copying content goes here...
        self.centralWidget.setText("<b>Edit > Copy</b> clicked")

    def pasteContent(self):
        # Logic for pasting content goes here...
        self.centralWidget.setText("<b>Edit > Paste</b> clicked")

    def cutContent(self):
        # Logic for cutting content goes here...
        self.centralWidget.setText("<b>Edit > Cut</b> clicked")

    def helpContent(self):
        # Logic for launching help goes here...
        self.centralWidget.setText("<b>Help > Help Content...</b> clicked")

    def about(self):
        # Logic for showing an about dialog content goes here...
        self.centralWidget.setText("<b>Help > About...</b> clicked")

    def populateOpenRecent(self):
        # Step 1. Remove the old options from the menu
        self.openRecentMenu.clear()
        # Step 2. Dynamically create the actions
        actions = []
        filenames = [f"File-{n}" for n in range(5)]
        for filename in filenames:
            action = QAction(filename, self)
            action.triggered.connect(partial(self.openRecentFile, filename))
            actions.append(action)
        # Step 3. Add the actions to the menu
        self.openRecentMenu.addActions(actions)

    def openRecentFile(self, filename):
        # Logic for opening a recent file goes here...
        self.centralWidget.setText(f"<b>{filename}</b> opened")

    def getWordCount(self):
        # Logic for computing the word count goes here...
        return 42


if __name__ == "__main__":
    # Create the application
    app = QApplication(sys.argv)
    # Create and show the main window
    win = Window()
    win.show()
    # Run the event loop
    sys.exit(app.exec_())
