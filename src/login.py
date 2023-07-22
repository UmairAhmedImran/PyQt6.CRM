from PyQt6.QtWidgets import QPushButton, QApplication, QLineEdit,QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt
import sys

credentials = []
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 350)
        self.setWindowTitle("CodersLegacy")

        self.labels("Username :", 'Times New Roman', 10, 40, 50)
        self.fields(40, 80, QLineEdit.EchoMode.Normal)

        self.labels("Password :", 'Times New Roman', 10, 40, 140)
        self.fields(40, 170, QLineEdit.EchoMode.Password)
        
        self.images(300, 300, "login_image.png")

        self.buttons(40, 240, 130, 35, "Login", self.going_to_dashboard, "background-color: black; color: white;")

    def buttons(self, w: int, x: int, y: int, z: int, text: str, fn, css:str):
         self.button = QPushButton(text, self)
         self.button.setFocus()
         self.button.setGeometry(w, x, y, z)
         self.button.clicked.connect(fn)
         self.button.setCursor(Qt.CursorShape.PointingHandCursor)
         self.button.setStyleSheet(css)

    def going_to_dashboard(self):
            self.close()
            self.w = Dashboard()
            self.w.show()
            print(credentials)

    def images(self, new_width:int, new_height:int, image_url:str):

        self.label = QLabel(self)       
        pixmap = QPixmap(image_url)# Load the image using QPixmap
        scaled_pixmap = pixmap.scaled(new_width, new_height)
        
        self.label.setPixmap(scaled_pixmap)# Set the pixmap as the content of the QLabel
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)        
        layout.setAlignment(Qt.AlignmentFlag.AlignRight) # Set the alignment of the label within the layout (center)
        
        self.setLayout(layout)# Set the layout as the main layout for the window


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
        self.input.text()

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,300)
        self.setWindowTitle("Dashboard")

        Window.images(self, 300, 320, 'i_health_care_center.jpg')

        Window.buttons(self, 30, 50, 130, 30, "Appointment", self.passing, "background-color: #090; color: white;")

        Window.buttons(self, 30, 100, 130, 30, "Cancel Appointment", self.passing, "background-color: #090; color: white;")

        Window.buttons(self, 30, 150, 130, 30, "Change Appointment", self.passing, "background-color: #090; color: white;")

        Window.buttons(self, 30, 200, 130, 30, "view Appointment", self.passing, "background-color: #090; color: white;")

        Window.buttons(self, 30, 250, 130, 30, "Logout", self.passing, "background-color: #090; color: white;")

    def passing(self):
        pass

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())