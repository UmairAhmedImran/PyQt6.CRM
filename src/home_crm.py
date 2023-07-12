import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CRM")
        

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()