import os
import sys

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Pixmap")
        
        widget = QLabel("Hello")
        widget.setPixmap(QPixmap("%s/test.jpg" % os.path.dirname(__file__)))
        
        self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()