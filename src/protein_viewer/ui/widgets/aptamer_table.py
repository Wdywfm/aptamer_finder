from PySide6 import QtGui
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QAbstractItemView,
    QTableWidget,
    QHBoxLayout,
    QWidget,
    QPushButton,
    QHeaderView,
)


class AptamerListTableWidget(QTableWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self._configure_table()

    def _configure_table(self):
        self.setMaximumWidth(545)
        self.table_font = QtGui.QFont("Consolas", 12)
        self.setFont(self.table_font)
        self.verticalHeader().setDefaultSectionSize(80)
        self.horizontalHeader().setDefaultSectionSize(240)
        self.verticalHeader().setDefaultAlignment(Qt.AlignCenter)
        self.setShowGrid(False)
        self.horizontalHeader().hide()
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setFocusPolicy(Qt.NoFocus)
        self.setStyleSheet(
            "QTableWidget::item:selected{background-color: white; color: black; border: 1px solid black;}"
        )

        # Init signals
        self.cellClicked.connect(self.draw_hist)

    def draw_hist(self, row, column):
        self.parent.canvas.axes.cla()
        self.parent.canvas.set_text()
        self.parent.canvas.axes.bar(self.parent.hist_labels[row], self.parent.hist_data[row])
        self.parent.canvas.draw()
