from pathlib import Path

from PySide6 import QtGui
from PySide6.QtWidgets import QMenuBar, QFileDialog, QTableWidgetItem
from PySide6.QtCore import Qt

from protein_viewer.protein_utils.protein import Protein


class MenuBar(QMenuBar):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self._protein = None
        self._add_menus()

    def _add_menus(self):
        file_menu = self.addMenu("&File")
        open_action = QtGui.QAction(QtGui.QIcon("open.png"), "&Open", self.parent)
        open_action.triggered.connect(self.read_pdb_file_action)
        exit_action = QtGui.QAction(QtGui.QIcon("exit.png"), "&Exit", self.parent)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.setStatusTip("Exit application")
        exit_action.triggered.connect(self.parent.close)
        file_menu.addAction(open_action)
        file_menu.addAction(exit_action)

    def read_pdb_file_action(self):
        pdb_path = QFileDialog.getOpenFileName(self, "Open Image", "", "PDB Files (*.pdb)")[0]
        self.parent.file_name.setText(f"{Path(pdb_path).stem} protein structure")
        self.parent.protein = Protein(pdb_path)
        self.parent.chain_1_items, self.parent.chain_2_items = [], []
        for chain in self.parent.protein.chains:
            self.parent.chain_1.addItem(chain)
            self.parent.chain_1_items.append(chain)
            self.parent.chain_2.addItem(chain)
            self.parent.chain_2_items.append(chain)
        for method in self.parent.protein.methods:
            self.parent.method.addItem(method)
        self.parent.chain_1_value = self.parent.chain_1.currentText()
        self.parent.chain_2_value = self.parent.chain_2.currentText()
        self.parent.chain_1.model().item(0).setEnabled(True)
        self.parent.chain_2.model().item(0).setEnabled(False)
        self.parent.chain_2.setCurrentIndex(1)
        self.parent.chain_2_value = self.parent.chain_2.currentText()

        self.parent.aptamer_size_value = "5"
        self.parent.aptamer_size.setText(self.parent.aptamer_size_value)

        self.parent.show_protein_structure()
