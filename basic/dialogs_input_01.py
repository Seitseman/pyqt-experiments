import sys

from PySide6.QtWidgets import (
    QApplication,
    QInputDialog,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Input Dialogs")
        
        layout = QVBoxLayout()
        
        buttonInt = QPushButton("Integer")
        buttonInt.clicked.connect(self.get_int)
        layout.addWidget(buttonInt)
        
        buttonFloat = QPushButton("Float")
        buttonFloat.clicked.connect(self.get_float)
        layout.addWidget(buttonFloat)
        
        buttonSel = QPushButton("Select")
        buttonSel.clicked.connect(self.get_selection)
        layout.addWidget(buttonSel)
        
        buttonStr = QPushButton("String")
        buttonStr.clicked.connect(self.get_str)
        layout.addWidget(buttonStr)
        
        
        buttonText = QPushButton("Text")
        buttonText.clicked.connect(self.get_text)
        layout.addWidget(buttonText)
        
        widget = QWidget()
        widget.setLayout(layout)
        
        self.setCentralWidget(widget)
        
    def get_int(self):
        int_val, ok = QInputDialog.getInt(
            self, "Get Int value", "Enter a number",
            value=0, minValue=-100, maxValue=100, step=1
        )
        
        print(f"Res: {ok} value: {int_val}")
        
    def get_float(self):
        float_value, ok = QInputDialog.getDouble(
            self,
            "Enter a Floan Number",
            "Type or paste the number here",
            value=0,
            minValue=-21.1,
            maxValue=13.3,
        )
        
        print(f"Res: {ok}, Val: {float_value}")
        
    def get_selection(self):
        title = "Select an entry"
        label = "Scroll the list and select item"
        items = ["color", "shape", "time", "distance"]
        selection = 2
        selected_item, ok = QInputDialog.getItem(
            self, title, label, items, current=selection, editable=False
        )
        
        print(f"Res: {ok}, selected item: {selected_item}")
    
    def get_str(self):
        seleted_str, ok = QInputDialog.getText(
            self, "Enter a string", "Type the pass", QLineEdit.Password, "my secret password"
        )
        
        print(f"Res: {ok}, pass: {seleted_str}")
    
    def get_text(self):
        selected_text, ok = QInputDialog.getMultiLineText(
            self, "Enter text", "Type your novel here", "Once upon a time..."
        )
        
        print(f"Result: {ok}. My selected text: \n {selected_text}")
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()