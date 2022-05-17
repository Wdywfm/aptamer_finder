import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

matplotlib.use("Qt5Agg")


class HistCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.set_text()
        super(HistCanvas, self).__init__(fig)

    def set_text(self):
        self.axes.set_ylabel("Distance")
        self.axes.set_xlabel("Residues")
        self.axes.set_title("CA - CA distance distribution")
