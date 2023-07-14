from PyQt6.QtWidgets import QMainWindow, QLabel, QApplication
from PyQt6.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(500, 250, 500, 400)

        text = QLabel("Hello")
        text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(text)

        menu = self.menuBar()

        file_menu = menu.addMenu("&File")

        file_menu2 = menu.addMenu("&Tools")

app = QApplication([sys.argv])        
window = MainWindow()
window.show()
sys.exit(app.exec())
