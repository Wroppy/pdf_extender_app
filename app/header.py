from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *


class Header(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("header")

        self.create_widgets()
        self.style_widgets()

        self.set_scaler_visible(False)

    def create_widgets(self):
        """
        Creates and lays the header widgets out in a horizontal layout.
        Header consists of:
            - Heading label
            - Scale slider 
            - Scale label
        """
        layout = QHBoxLayout(self)

        self.heading = QLabel("Pick your file")

        layout.addWidget(self.heading)
        layout.addStretch(1)

        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setFixedWidth(200)

        # Slider is 20-60 to account for a range of 40 values, between 100 and 300.
        # Step size viewed from the user is 5%
        self.slider.setMinimum(20)
        self.slider.setMaximum(60)

        self.slider.valueChanged.connect(self.update_text)

        layout.addWidget(self.slider)

        self.label = QLabel("100%")
        layout.addWidget(self.label)

    def style_widgets(self):
        style = f"""
            QLabel {{
                font-size: 18px;
            }}

            QSlider::groove:horizontal {{
            }}

        """

        self.setStyleSheet(style)

    def update_text(self, slider_number: int):
        """
        Updates the scale label based on the value of the slider.
        """

        # Multiplies by 5 to account for the intended step size
        self.label.setText(f"{5 * slider_number}%")

    def set_scaler_visible(self, visible: bool):
        self.slider.setVisible(visible)
        self.label.setVisible(visible)
