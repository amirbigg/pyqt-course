import sys
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt6.QtGui import QFont, QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        self.setGeometry(100, 150, 350, 400)
        self.setWindowTitle("User Profile GUI")
        self.setup_main_window()
        self.show()

    def setup_main_window(self):
        self.create_image_labels()

        user_label = QLabel("Amir big", self)
        user_label.setFont(QFont("Arial", 20))
        user_label.move(120, 140)

        bio_label = QLabel(self)
        bio_label.setText("Biography")
        bio_label.setFont(QFont("Arial", 15))
        bio_label.move(15, 190)

        about_label = QLabel("I'm a software engineer with more than 10 years of experience", self)
        about_label.setWordWrap(True)
        about_label.resize(300, 40)
        about_label.move(15, 220)

        skills_label = QLabel("Skills", self)
        skills_label.setFont(QFont("Arial", 15))
        skills_label.move(15, 280)

        language_label = QLabel(self)
        language_label.setText("Python | PHP | SQL")
        language_label.resize(200, 40)
        language_label.move(15, 300)

    def create_image_labels(self):
        background_img = QLabel(self)
        background_pixmap = QPixmap("images/skyblue.png")
        background_img.setPixmap(background_pixmap)
        background_img.setGeometry(0, 0, 350, 100)
        background_img.setScaledContents(True)

        profile_img = QLabel(self)
        profile_pixmap = QPixmap("images/profile_image.png")
        profile_img.setPixmap(profile_pixmap)
        profile_img.resize(200, 100)
        profile_img.move(120, 30)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec())
