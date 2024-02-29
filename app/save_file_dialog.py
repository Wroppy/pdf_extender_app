from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class SaveFileDialog(QFileDialog):
    def __init__(self):
        super().__init__()

        # User can only select existing pdf files.
        self.setFileMode(QFileDialog.FileMode.AnyFile)
        self.setAcceptMode(QFileDialog.AcceptSave)
        self.setNameFilter("PDF (*.pdf)")

    def get_filename(self):
        return self.selectedFiles()[0]


if __name__ == "__main__":
    app = QApplication()
    window = LoadFileDialog()
    if (window.exec()):
        print(window.get_filename())
    else:
        print("User cancelled")
    window = QWidget()
    window.show()
    app.exec()
