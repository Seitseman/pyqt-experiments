import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QStackedLayout,
    QVBoxLayout,
    QWidget
)

from layout_colorwidget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Layout Stacked")
        
        page_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.stack_layout = QStackedLayout()
        
        page_layout.addLayout(button_layout)
        page_layout.addLayout(self.stack_layout)
        
        button = QPushButton("#F00F5C")
        button.pressed.connect(lambda: self.stack_layout.setCurrentIndex(0))
        button_layout.addWidget(button)
        self.stack_layout.addWidget(Color("#F00F5C"))
        
        button = QPushButton("#5CF00F")
        button.pressed.connect(lambda: self.stack_layout.setCurrentIndex(1))
        button_layout.addWidget(button)
        self.stack_layout.addWidget(Color("#5CF00F"))
        
        button = QPushButton("#0F5CF0")
        button.pressed.connect(lambda: self.stack_layout.setCurrentIndex(2))
        button_layout.addWidget(button)
        self.stack_layout.addWidget(Color("#0F5CF0"))
        
        widget = QWidget()
        widget.setLayout(page_layout)
        self.setCentralWidget(widget)
        
        self.setMinimumWidth(300)
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()