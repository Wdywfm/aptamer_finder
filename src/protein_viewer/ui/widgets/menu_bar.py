from PySide6.QtWidgets import QMenuBar


class MenuBar(QMenuBar):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self._add_menus()

    def _add_menus(self):
        file_menu = self.addMenu('&File')
        file_menu.addAction(self.parent.exit_action)


