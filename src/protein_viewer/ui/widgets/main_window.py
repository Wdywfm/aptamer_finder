from PySide6 import QtGui
from PySide6.QtWidgets import QMainWindow

from protein_viewer.ui.widgets.menu_bar import MenuBar
from protein_viewer.ui.icons.app_icon import app_icon


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Protein Viewer")
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(app_icon)
        self.setWindowIcon(QtGui.QIcon(pixmap))
        self.exit_action = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
        self.exit_action.setShortcut('Ctrl+Q')
        self.exit_action.setStatusTip('Exit application')
        self.exit_action.triggered.connect(self.close)
        self.setMenuBar(MenuBar(self))


