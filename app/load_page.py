from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from spinner.spinner import WaitingSpinner


class LoadingPage(QWidget):
    def __init__(self):
        super().__init__()

        self.create_widgets()
        self.style_widgets()

    def create_widgets(self):
        """
        A centered circular loading page 
        """
        layout = QVBoxLayout(self)

        # Sets the spinner specs
        spinner = WaitingSpinner(self)

        spinner.setRoundness(100.0)
        spinner.setMinimumTrailOpacity(15.0)
        spinner.setTrailFadePercentage(80.0)
        spinner.setNumberOfLines(80)
        spinner.setLineLength(10)
        spinner.setLineWidth(5)
        spinner.setInnerRadius(15)
        spinner.setRevolutionsPerSecond(1)
        spinner.setColor(QColor(0, 145, 216))

        spinner.start()

        # Centers the circular loading icon
        layout.addStretch(1)
        layout.addWidget(spinner)
        layout.addStretch(1)

    def style_widgets(self):
        style = """

        """

        self.setStyleSheet(style)


if __name__ == "__main__":
    app = QApplication()
    window = LoadingPage()
    window.show()
    app.exec()
