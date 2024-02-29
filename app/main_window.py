from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from header import Header
from pdf_load_widget import PDFLoadWidget

class PDFScalerWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.create_widgets()

    def create_widgets(self):
        layout = QVBoxLayout(self)

        header = Header()
        layout.addWidget(header)

        pdf_load_widget = PDFLoadWidget()
        # pdf_load_widget.file_selected.connect(print)
        layout.addWidget(pdf_load_widget)

    def return_header(self) -> QWidget:
        self.header = QWidget()
        layout = QHBoxLayout(header)



class PDFScalerWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        scaler_widget = PDFScalerWidget()

        self.setCentralWidget(scaler_widget)


if __name__ == "__main__":
    app = QApplication()
    window = PDFScalerWindow()
    window.show()
    app.exec()
