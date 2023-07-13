import sys
from PyQt6.QtWidgets import QApplication, QWidget,QLineEdit, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import Qt

string = "hello"
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CRM") # adding title to the page
        self.resize(250,250) # adding specific size to the page

        layout = QVBoxLayout()
        self.setLayout(layout)

        text = QLabel("Enter text here")
        layout.addWidget(text)

        self.input = QLineEdit()
        self.input.setDragEnabled(False)
        layout.addWidget(self.input, alignment= Qt.AlignmentFlag.AlignCenter)

        button = QPushButton("Get Text")
        button.clicked.connect(self.get)
        layout.addWidget(button)

        button = QPushButton("Clear Text")
        button.clicked.connect(self.input.clear)
        layout.addWidget(button)

    def get(self):
        text = self.input.text()
        print(text)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())