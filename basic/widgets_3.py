import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QCheckBox, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Checkbox")
        
        widget = QCheckBox("This is a checkbox")
        widget.setCheckState(Qt.Checked)
        
        widget.stateChanged.connect(self.show_state)
        
        self.setCentralWidget(widget)
        
    def show_state(self, s):
        print(s == Qt.Checked)
        print(s)
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()