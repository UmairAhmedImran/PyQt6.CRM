from PyQt6.QtWidgets import QMainWindow, QLabel, QApplication, QPushButton
from PyQt6.QtCore import Qt
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(500, 250, 500, 400)

        text = QLabel("Hello")
        text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(text)

        button = QPushButton("Next page")
        # button.clicked.connect(self.new_window)
        

        menu = self.menuBar()

        file_menu = menu.addMenu("&File")

        file_menu2 = menu.addMenu("&Tools")
    # def new_window(self):
    #     app = QApplication([sys.argv])
    #     window = home_crm.MainWindow()
    #     window.show
    #     sys.exit(app.exec())
app = QApplication([sys.argv])        
window = Window()
window.show()
sys.exit(app.exec())
