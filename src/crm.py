from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit ,QVBoxLayout ,QPushButton, QMainWindow, QWidget
import sys
from PyQt6.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CRM") # adding title to the page
        self.resize(250,250) # adding specific size to the page

        layout = QVBoxLayout()
        self.setLayout(layout)

        text = QLabel("Enter text here")
        layout.addWidget(text, alignment=Qt.AlignmentFlag.AlignJustify)

        self.input = QLineEdit()
        self.input.setDragEnabled(False)
        layout.addWidget(self.input, alignment= Qt.AlignmentFlag.AlignCenter)

        button = QPushButton("Get Text")
        button.clicked.connect(self.get)
        layout.addWidget(button)

        button = QPushButton("Clear Text")
        button.clicked.connect(self.input.clear)
        layout.addWidget(button)

        text_button = Mainwindow.buttons(self, 70, 70, 130, 30, "text", self.get)

    def get(self):
        text = self.input.text()
        print(text)

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(400,300,500,400)
        self.setWindowTitle("Login")

        self.buttons(100, 100, 130, 30, "Push for window", self.show_new_window)
        self.buttons(300, 300, 130, 30, "text", self.no_window)

    "Creating a function which take the position  of the button and the function upon clicking the button"
    "can be used to create many types of same button with simple modification"
    
    def buttons(self, w: int, x: int, y: int, z: int, text: str, fn):
        button = QPushButton(text, self)
        button.setFocus()
        button.setGeometry(w, x, y, z)
        button.clicked.connect(fn)
        

    def show_new_window(self):
        self.close()
        self.w = Window()
        self.w.show()

    def no_window(self):
        print("no window")
app = QApplication(sys.argv)
window = Mainwindow()
window.show()
sys.exit(app.exec())