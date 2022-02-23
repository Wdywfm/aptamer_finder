import sys

from PySide6.QtWidgets import QApplication

from protein_viewer.ui.widgets.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication([])

    widget = MainWindow()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())

