from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys
from random import choice

window_titles = [
    "SigSlot",
    "My SigSlot",
    "SigSlot My SigSlot",
    "PySide",
    "Wow",
    "What on earth",
    "Surprise",
    "Error"
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
    
        self.n_times_clicked = 0
    
        self.setWindowTitle("SigSlot")
    
        self.button = QPushButton("Button!")
        self.button.clicked.connect(self.the_button_was_clicked)
        
        self.windowTitleChanged.connect(self.the_window_title_changed)
        
        self.setCentralWidget(self.button)
    
    def the_button_was_clicked(self):
        print("Clicked")
        new_window_title = choice(window_titles)
        print("Title: %s" % new_window_title)
        self.setWindowTitle(new_window_title)
        
    def the_window_title_changed(self, window_title):
        print("title changed: %s " % window_title)
        
        if window_titles == "Error":
            self.button.setDisabled(True)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()