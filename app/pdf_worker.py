from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class PDFWorkerSignal(QObject):
    finished = Signal()


class PDFWorker(QRunnable):

    def __init__(self, fn, scale_factor: float, desired_path: str):
        super().__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.scale_factor = scale_factor
        self.desired_path = desired_path

        self.signals = PDFWorkerSignal()


    @Slot() 
    def run(self):
        self.fn(self.scale_factor, self.desired_path)
        self.signals.finished.emit()