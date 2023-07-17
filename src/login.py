from PyQt6.QtWidgets import  QApplication, QLineEdit,QWidget, QLabel
from PyQt6.QtGui import QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 400)
        self.setWindowTitle("CodersLegacy")

        self.labels("Username :", 'Times New Roman', 10, 80, 80)
        self.fields(80, 110, QLineEdit.EchoMode.Normal)

        self.labels("Password :", 'Times New Roman', 10, 80, 180)
        self.fields(80, 210, QLineEdit.EchoMode.Password)

    def labels(self, text:str, font_family:str, size:int, x:int, y: int):
        label = QLabel(text, self)
        label.setFont(QFont(font_family, size))
        label.move(x, y)

    def fields(self, x:int, y:int, Echomode):
        self.input = QLineEdit(self)
        self.input.setEchoMode(Echomode)
        self.input.setDragEnabled(False)
        self.input.move(x, y)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())