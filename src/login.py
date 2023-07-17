from PyQt6.QtWidgets import  QApplication, QWidget, QLabel
from PyQt6.QtGui import QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 400)
        self.setWindowTitle("CodersLegacy")

        self.labels("Username :", 'Arial', 10, 80, 80)

        self.labels("Password :", 'Arial', 10, 80, 180)

    def labels(self, text:str, font_family:str, size:int, x:int, y: int):
        label = QLabel(text, self)
        label.setFont(QFont(font_family, size))
        label.move(x, y)

        # label = QLabel("Username :", self)
        # label.setFont(QFont('Arial', 10))
        # label.move(80, 80)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())