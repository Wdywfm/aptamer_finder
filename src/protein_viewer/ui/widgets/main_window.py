from PySide6 import QtGui
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QHBoxLayout,
    QWidget,
    QVBoxLayout,
    QComboBox,
    QTableWidgetItem,
    QLineEdit,
)

from protein_viewer.ui.widgets.aptamer_table import AptamerListTableWidget
from protein_viewer.ui.widgets.hist_canvas import HistCanvas
from protein_viewer.ui.widgets.label import Label
from protein_viewer.ui.layouts.option_layout import OptionLayout
from protein_viewer.ui.widgets.menu_bar import MenuBar
from protein_viewer.ui.icons.app_icon import app_icon


# TODO: finalize methods
# TODO: add full sequences
# TODO: add 3d graph


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.widget = QWidget()
        self.setCentralWidget(self.widget)

        self.setWindowTitle("Protein Viewer")
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(app_icon)
        self.setWindowIcon(QtGui.QIcon(pixmap))

        self.table = AptamerListTableWidget(self)

        self.canvas = HistCanvas(self, dpi=100)

        self.chain_1 = QComboBox()
        self.chain_2 = QComboBox()
        self.aptamer_size = QLineEdit()
        self.method = QComboBox()

        self.options_layout = OptionLayout()
        self.options_layout.addWidget(Label(self, "Chain 1"), 0, 0)
        self.options_layout.addWidget(Label(self, "Chain 2"), 0, 1)
        self.options_layout.addWidget(Label(self, "Size"), 0, 2)
        self.options_layout.addWidget(Label(self, "Method"), 0, 3)
        self.options_layout.addWidget(self.chain_1, 1, 0)
        self.options_layout.addWidget(self.chain_2, 1, 1)
        self.options_layout.addWidget(self.aptamer_size, 1, 2)
        self.options_layout.addWidget(self.method, 1, 3)

        self.right_layout = QVBoxLayout()
        self.right_layout.addLayout(self.options_layout, 0)
        self.right_layout.addWidget(self.table, 1)

        self.vert_layout = QHBoxLayout()
        self.vert_layout.addWidget(self.canvas, 0)
        self.vert_layout.addLayout(self.right_layout, 1)

        self.file_name = Label(self)
        self.file_name.setAlignment(Qt.AlignCenter)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.file_name, 0)
        self.layout.addLayout(self.vert_layout, 1)

        self.widget.setLayout(self.layout)

        self.setMenuBar(MenuBar(self))

        # Init slots
        self.chain_1.currentTextChanged.connect(self.chain_1_changed)
        self.chain_2.currentTextChanged.connect(self.chain_2_changed)
        self.aptamer_size.textChanged.connect(self.aptamer_size_changed)

    def chain_1_changed(self, value):
        self.chain_2.model().item(self.chain_1_items.index(self.chain_1_value)).setEnabled(True)
        for i, chain in enumerate(self.protein.chains):
            if chain == value:
                self.chain_2.model().item(i).setEnabled(False)
        self.chain_1_value = value
        self.show_protein_structure()

    def chain_2_changed(self, value):
        self.chain_1.model().item(self.chain_1_items.index(self.chain_2_value)).setEnabled(True)
        for i, chain in enumerate(self.protein.chains):
            if chain == value:
                self.chain_1.model().item(i).setEnabled(False)
        self.chain_2_value = value
        self.show_protein_structure()

    def aptamer_size_changed(self, value):
        self.aptamer_size_value = value
        self.show_protein_structure()

    def show_protein_structure(self):
        kmer_strings_with_distances = sorted(
            self.protein.get_kmer_strings_with_distances(
                self.chain_1_value,
                self.chain_2_value,
                int(self.aptamer_size_value),
            ),
            key=lambda x: x[-1],
        )

        self.table_data, self.hist_data, self.hist_labels = (
            [],
            [],
            [],
        )

        for kmer_pair in kmer_strings_with_distances:
            self.table_data.append([f"{kmer_pair[0]}\n{kmer_pair[1]}", str(kmer_pair[3])])
            self.hist_data.append(kmer_pair[2])
            self.hist_labels.append([f"{char}\n{kmer_pair[1][i]}" for i, char in enumerate(kmer_pair[0])])

        self.table.setRowCount(len(self.table_data))
        self.table.setColumnCount(len(self.table_data[0]))
        for i, table_row in enumerate(self.table_data):
            for j, value in enumerate(self.table_data[i]):
                item = QTableWidgetItem(value)
                item.setTextAlignment(Qt.AlignCenter)
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.table.setItem(i, j, item)

        self.table.setCurrentItem(self.table.item(0, 0))
        self.table.draw_hist(0, 0)


