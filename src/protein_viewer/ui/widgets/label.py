from PySide6.QtGui import QFont
from PySide6.QtWidgets import QLabel


class Label(QLabel):
    def __init__(self, parent=None, text=None):
        super().__init__(parent=parent, text=text)
        self.set_defaults()

    def set_defaults(self):
        self.setFont(QFont("Consolas", 12))
