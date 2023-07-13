import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel

string = "hello"
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CRM") # adding title to the page
        self.setGeometry(0,0,1530,800) # adding specific size to the page
        self.input = QLineEdit(self)
        self.input.move(80,100)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()