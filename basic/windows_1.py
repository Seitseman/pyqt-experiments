import random
import sys
import cv2


from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

class MyWindow(QWidget):
    '''
    If this widget has no parent, it will be shown as a window
    '''
    
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.label = QLabel(f"My Window! {random.randint(0, 100)}")
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.widget = None
        self.button = QPushButton("Click Me!")
        self.button.clicked.connect(self.on_button_clicked)
        self.setCentralWidget(self.button)
        
    def on_button_clicked(self):
        if self.widget is None:
            self.widget = MyWindow()
            self.widget.show()
        else:
            self.widget = None
        
app = QApplication(sys.argv)

w = MainWindow()
w.show()

app.exec()