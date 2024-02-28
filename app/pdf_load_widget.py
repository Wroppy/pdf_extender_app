from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class PDFLoadWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.create_widgets()
        self.style_widgets()

    def create_widgets(self):
        self.setSizePolicy(QSizePolicy.Policy.Expanding,
                           QSizePolicy.Policy.Expanding)

    def style_widgets(self):
        style = """ 

        """

        self.setStyleSheet(style)
