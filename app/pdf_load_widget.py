from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from load_file_dialog import LoadFileDialog

class PDFLoadWidget(QFrame):
    file_selected = Signal(str)

    def __init__(self):
        super().__init__()

        self.create_widgets()
        self.style_widgets()

    def create_widgets(self):
        """
        Initializes and lays the widgets in a vertical layout.

        This widget consist of:
            - A frame for spacing and styling
                - A label to direct the user
                - Horizontal Layout (for centering)
                    - A file dialog button to select a file
        """

        self.setSizePolicy(QSizePolicy.Policy.Expanding,
                           QSizePolicy.Policy.Expanding)

        # Widget for spacing and styling
        inner_widget = QFrame()
        layout = QVBoxLayout(inner_widget)

        heading = QLabel("Select a PDF file")
        heading.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(heading)

        choose_file_button = QPushButton("Choose File")
        choose_file_button.setMaximumWidth(150)
        choose_file_button.clicked.connect(self.open_dialog)

        # Widget for centering the file dialog button
        # setAlignment is not a function for buttons
        center_layout = QHBoxLayout()
        center_layout.addWidget(choose_file_button)
        layout.addLayout(center_layout)

        main_layout = QVBoxLayout(self)

        main_layout.addStretch(1)
        main_layout.addWidget(inner_widget)
        main_layout.addStretch(1)

    def style_widgets(self):
        # TODO Style the widgets
        style = """
            QLabel, QPushButton {
                font-size: 15px;
            }

        """

        self.setStyleSheet(style)


    def open_dialog(self):
        dialog = LoadFileDialog()

        # If the user selects a pdf, emits the pdf filename 
        if dialog.exec():
            pdf_filename = dialog.get_filename()
            self.emit_signal(pdf_filename)

    def emit_signal(self, pdf_path):
        self.file_selected.emit(pdf_path)
    
    