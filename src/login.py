from PyQt6.QtWidgets import  QApplication, QWidget, QLabel
from PyQt6.QtGui import QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 400)
        self.setWindowTitle("CodersLegacy")

        label = QLabel("Username :", self)
        label.setFont(QFont('Arial', 10))
        label.move(80, 80)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())