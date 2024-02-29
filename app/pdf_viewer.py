from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEnginePage


class PDFViewer(QWidget):
    loaded = Signal()

    def __init__(self):
        super().__init__()

        self.create_widgets()
        self.style_widgets()

    def create_widgets(self):
        layout = QVBoxLayout(self)

        # A PDF viewer using a web engine
        self.pdf_view = QWebEngineView()
        self.pdf_view.settings().setAttribute(
            self.pdf_view.settings().WebAttribute.PluginsEnabled, True)
        self.pdf_view.settings().setAttribute(
            self.pdf_view.settings().WebAttribute.PdfViewerEnabled, True)

        layout.addWidget(self.pdf_view)

    def style_widgets(self):
        pass

    def load_pdf(self, path: str):
        url = QUrl.fromLocalFile(path)
        self.pdf_view.setUrl(url)
        self.loaded.emit()


if __name__ == "__main__":
    app = QApplication()
    window = PDFViewer()
    window.load_pdf("C:\\Users\\Weyman Wong\\Documents\\programming\\pdf_extender\\tests\\placeholder_pdf.pdf")
    window.show()
    app.exec()


