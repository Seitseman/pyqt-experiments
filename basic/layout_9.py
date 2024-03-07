import sys
import matplotlib.colors as matcolors

from PySide6.QtCore import Qt, QMargins, QSize
from PySide6.QtGui import QAction, QIcon, QImage, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QDialog,
    QDialogButtonBox,
    QListWidget,
    QMainWindow,
    QStatusBar,
    QTabWidget,
    QToolBar,
    QVBoxLayout,
)

from layout_colorwidget import Color

class Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        
        self.setWindowTitle("!Dialog!")
        
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        
        self.layout = QVBoxLayout()
        
        self.layout.addWidget(QLabel("Dialog appeared, is that OK?"))
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Tab Widget")
        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        
        tool_bar = QToolBar("Main Tool Bar")
        tool_bar.setIconSize(QSize(16, 16))
        self.addToolBar(tool_bar)
        
        
        button_action = QAction(QPixmap.fromImage(
            QImage.fromData(b'<svg fill="#000000" viewBox="0 0 30 30" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"><path d="M11.448 10c-.4-.01-.796.065-1.082.345-.287.28-.373.675-.366 1.08.008.404.093.864.25 1.42l4.515 15.986c.088.31.205.575.39.784.184.208.447.35.714.38.532.056.975-.228 1.372-.595l3.144-2.91c.244-.244.468-.174.636-.006l3.252 3.122c.284.272.652.383 1.01.385.357.002.73-.11 1.013-.392l3.306-3.305c.284-.284.396-.655.397-1.016 0-.36-.11-.74-.405-1.02l-3.25-3.123c-.177-.176-.166-.436.013-.615l3.027-3.142c.378-.394.668-.844.607-1.38-.03-.267-.174-.53-.383-.714-.21-.184-.475-.3-.786-.39L12.846 10.25c-.544-.157-.998-.237-1.398-.25zm-.03 1c.26.006.662.068 1.17.216l15.976 4.644c.646.188.362.562.102.822l-3.027 3.144c-.274.284-.387.65-.39 1.01-.002.358.11.74.403 1.02l3.25 3.12c.228.227.095.508-.007.61L25.59 28.89c-.14.164-.466.15-.623-.006l-3.25-3.12c-.285-.273-.655-.382-1.01-.38-.353 0-.716.108-1 .372l-3.145 2.91c-.48.396-.712.325-.83-.093l-4.517-15.987c-.147-.52-.21-.922-.215-1.18 0-.407.198-.407.418-.407zm-6.92 15c-.45 0-.66-.55-.354-.853l2-2c.457-.455 1.165.25.71.707l-2.003 2c-.093.097-.217.146-.353.146zM25.5 4c.45 0 .66.55.356.853l-2 2c-.457.455-1.165-.25-.71-.707l2.003-2c.093-.097.214-.146.35-.146zM4.497 4c-.45 0-.658.55-.353.853l2 2c.457.455 1.165-.25.71-.707l-2.003-2C4.758 4.05 4.634 4 4.498 4zM0 14.5c0-.277.223-.5.5-.5h3c.277 0 .5.223.5.5s-.223.5-.5.5h-3c-.277 0-.5-.223-.5-.5zM14.5 0c.277 0 .5.223.5.5v3c0 .277-.223.5-.5.5s-.5-.223-.5-.5v-3c0-.277.223-.5.5-.5z"></path></g></svg>')),
                                 "Check this button", self)
        button_action.setCheckable(True)
        button_action.setStatusTip("Button action")
        button_action.triggered.connect(self.onButtonActionTriggered)
        tool_bar.addAction(button_action)
        
        tool_bar.addSeparator()
        
        button_action_new = QAction(QPixmap.fromImage(
            QImage.fromData(b'')
        ), "New Action", self)
        button_action_new.setCheckable(True)
        button_action_new.setStatusTip("New Action")
        button_action_new.triggered.connect(self.onButtonActionTriggered)
        tool_bar.addAction(button_action_new);
        
        
        tool_bar.addWidget(QLabel("<font color='red'><b>Important!</b></font>"))
        
        list_widget_colors = QListWidget()
        tool_bar.addWidget(list_widget_colors)
        list_widget_colors.setMaximumHeight(tool_bar.minimumSizeHint().height())
        
        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.West)
        tabs.setMovable(True)
        
        for n, color in enumerate(matcolors.CSS4_COLORS):
            tabs.addTab(Color(color), color)
            
        list_widget_colors.addItems(matcolors.CSS4_COLORS)
        
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(QMargins())
        main_layout.addWidget(tabs)
        
        menu = self.menuBar()
        
        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)
        file_menu.addSeparator()
        file_menu.addAction(button_action_new)
        
        sub_menu = file_menu.addMenu("2lvl menu")
        sub_menu.addAction(button_action_new)
        
        widget = Color("red")
        widget.setLayout(main_layout)
        
        self.setCentralWidget(widget)
        self.setStatusBar(QStatusBar(self))
        
    def onButtonActionTriggered(self, s):
        print(f"triggered {s}. \nSender: {self.sender()}")
        
        dialog = Dialog(self)
        dialog.setWindowTitle("Test Dialog")
        if dialog.exec():
            print("OK!")
        else:
            print("Canceled")
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()