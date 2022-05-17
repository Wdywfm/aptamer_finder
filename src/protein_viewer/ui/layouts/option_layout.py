from PySide6.QtWidgets import QGridLayout
from PySide6.QtCore import Qt


class OptionLayout(QGridLayout):
    def __init__(self, parent=None):
        super().__init__(parent)

    def addWidget(self, widget, row, column, alignment=Qt.Alignment()):
        widget.setMaximumWidth(130)
        widget.setMaximumHeight(20)
        super().addWidget(widget, row, column, alignment)
