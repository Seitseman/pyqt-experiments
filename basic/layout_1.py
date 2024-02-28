import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow

from layout_colorwidget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Layout")
        
        widget = Color("crimson")
        self.setCentralWidget(widget)
        
app = QApplication(sys.argv)
w = MainWindow()
w.show()

app.exec()