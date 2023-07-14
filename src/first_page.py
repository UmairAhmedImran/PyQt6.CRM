from PyQt6.QtWidgets import QMainWindow, QPushButton, QApplication
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

app = QApplication([sys.argv])        
window = MainWindow()
window.show()
sys.exit(app.exec())
