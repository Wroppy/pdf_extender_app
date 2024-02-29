from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from header import Header
from pdf_load_widget import PDFLoadWidget
from load_page import LoadingPage
from pdf_viewer import PDFViewer


class PDFScalerWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.create_widgets()

    def create_widgets(self):
        layout = QVBoxLayout(self)

        self.header = Header()
        layout.addWidget(self.header)

        self.pages = QStackedWidget()
        layout.addWidget(self.pages)

        # Widget for allowing the user to select a PDF file
        pdf_load_widget = PDFLoadWidget()

        self.pages.addWidget(pdf_load_widget)

        loading_page = LoadingPage()
        self.pages.addWidget(loading_page)

        pdf_viewer = PDFViewer()
        self.pages.addWidget(pdf_viewer)


        # When the user selects a PDF file, the window shows the loading page
        # then loads the pdf
        pdf_load_widget.file_selected.connect(lambda filename: self.show_loading_page())
        pdf_load_widget.file_selected.connect(pdf_viewer.load_pdf)

        # When the pdf has been loaded, the user goes to the PDF viewer
        # Also shows the scaler
        pdf_viewer.loaded.connect(self.show_pdf_page)
        pdf_viewer.loaded.connect(lambda: self.header.set_scaler_visible(True))

    def show_pdf_page(self):
        self.pages.setCurrentIndex(2)

    def show_load_pdf_page(self):
        self.pages.setCurrentIndex(0)

    def show_loading_page(self):
        self.pages.setCurrentIndex(1)

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
