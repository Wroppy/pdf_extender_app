from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class AfterScalingPage(QWidget):
    return_to_start = Signal()

    def __init__(self):
        super().__init__()

        self.create_widgets()
        self.style_widgets()

    def create_widgets(self):
        layout = QVBoxLayout(self)

        self.file_location_label = QLabel()
        self.file_location_label.setAlignment(Qt.AlignCenter)

        new_file_button = QPushButton("Scale another file")
        new_file_button.setFixedWidth(200)
        new_file_button.clicked.connect(lambda e: self.return_to_start.emit())

        # Layout purely for centering a button
        center_button_layout = QHBoxLayout()
        center_button_layout.addWidget(new_file_button)

        layout.addStretch(1)
        layout.addWidget(self.file_location_label)
        layout.addLayout(center_button_layout)
        layout.addStretch(1)


    def style_widgets(self):
        style = """
        QLabel, QPushButton {
            font-size: 15px;
        }
        """

        self.setStyleSheet(style)   

    def change_file_text(self, scale_factor: float, new_file_location: str):
        text = f"File location: {new_file_location}\nScale factor: {int(scale_factor)}%"
        self.file_location_label.setText(text)
