from PyQt6.QtWidgets import  QApplication, QLineEdit,QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 400)
        self.setWindowTitle("CodersLegacy")

        self.labels("Username :", 'Times New Roman', 10, 60, 90)
        self.fields(60, 120, QLineEdit.EchoMode.Normal)

        self.labels("Password :", 'Times New Roman', 10, 60, 180)
        self.fields(60, 210, QLineEdit.EchoMode.Password)

        self.images(300, 300, "login_image.png")

    def images(self, new_width:int, new_height:int, image_url:str):

        self.label = QLabel(self)

        # Load the image using QPixmap
        pixmap = QPixmap(image_url)

        scaled_pixmap = pixmap.scaled(new_width, new_height)
        

        # Set the pixmap as the content of the QLabel
        self.label.setPixmap(scaled_pixmap)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)

        # Set the alignment of the label within the layout (center)
        layout.setAlignment(Qt.AlignmentFlag.AlignRight)

        # Set the layout as the main layout for the window
        self.setLayout(layout)


    def labels(self, text:str, font_family:str, size:int, x:int, y: int):
        label = QLabel(text, self)
        label.setFont(QFont(font_family, size))
        label.move(x, y)

    def fields(self, x:int, y:int, Echomode):
        self.input = QLineEdit(self)
        self.input.setGeometry(x, y, 150, 25)
        self.input.setEchoMode(Echomode)
        self.input.setDragEnabled(False)
        self.input.move(x, y)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())