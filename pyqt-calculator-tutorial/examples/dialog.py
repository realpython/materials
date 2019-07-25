# filename: dialog.py

"""Dialog-Style application."""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QDialogButtonBox


class Dialog(QDialog):
    """Dialog."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle('QDialog')
        dlg_layout = QVBoxLayout()
        form_layout = QFormLayout()
        form_layout.addRow('Name:', QLineEdit())
        form_layout.addRow('Age:', QLineEdit())
        form_layout.addRow('Job:', QLineEdit())
        form_layout.addRow('Hobbies:', QLineEdit())
        dlg_layout.addLayout(form_layout)
        btns = QDialogButtonBox()
        btns.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        dlg_layout.addWidget(btns)
        self.setLayout(dlg_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
