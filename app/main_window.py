import sys
import pathlib
sys.path.insert(0, f"{pathlib.Path().resolve()}\\")

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from header import Header
from pdf_load_widget import PDFLoadWidget
from load_page import LoadingPage
from pdf_viewer import PDFViewer
from utils import PDFScaler



class PDFScalerWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.create_widgets()
        self.__pdf_path = ""

    def pdf_path(self) -> str:
        return self.__pdf_path

    def set_pdf_path(self, path: str):
        self.__pdf_path = path

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
        pdf_load_widget.file_selected.connect(
            lambda filename: self.show_loading_page())
        pdf_load_widget.file_selected.connect(pdf_viewer.load_pdf)

        # Sets the PDF path to the file selected
        pdf_load_widget.file_selected.connect(self.set_pdf_path)

        # When the pdf has been loaded, the user goes to the PDF viewer
        # Also shows the scaler
        pdf_viewer.loaded.connect(self.show_pdf_page)
        pdf_viewer.loaded.connect(lambda: self.header.set_scaler_visible(True))

        self.header.scale_pdf.connect(self.start_scaling)

    def show_pdf_page(self):
        self.header.set_heading("Preview loaded PDF")
        self.pages.setCurrentIndex(2)

    def show_load_pdf_page(self):
        self.header.set_heading("Pick your file")
        self.pages.setCurrentIndex(0)

    def show_loading_page(self):
        self.header.set_heading("Loading...")
        self.pages.setCurrentIndex(1)

    def return_header(self) -> QWidget:
        self.header = QWidget()
        layout = QHBoxLayout(header)

    def scale_pdf(self, scale_factor: float, desired_path: str):
        """
        Takes a scale factor and the desired path to write to, uses the PDFScaler class to
        scale and write the pdf  
        """

        scaler = PDFScaler()
        scaler.scale_pdf(self.pdf_path(), scale_factor)
        scaler.write_pdf(desired_path)

    def start_scaling(self, scale_factor: float, desired_path: str):
        self.show_loading_page()
        self.scale_pdf(scale_factor / 100, desired_path)


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
