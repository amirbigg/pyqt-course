from PyQt6.QtWidgets import QWidget, QApplication, QFrame, QPushButton
from PyQt6.QtCore import QRect, QPropertyAnimation
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        self.button = QPushButton("Start", self)
        self.button.clicked.connect(self.do_animation)
        self.button.move(30, 30)

        self.frame = QFrame(self)
        self.frame.setFrameStyle(QFrame.Shape.WinPanel | QFrame.Shadow.Plain)
        self.frame.setGeometry(150, 30, 100, 100)

        self.setGeometry(300, 300, 380, 300)
        self.setWindowTitle('Animation')
        self.show()

    def do_animation(self):
        self.anim = QPropertyAnimation(self.frame, b"geometry")
        self.anim.setDuration(2000)
        self.anim.setStartValue(QRect(150, 30, 100, 100))
        self.anim.setEndValue(QRect(150, 30, 200, 200))
        self.anim.start()


if __name__ == "__main__":
    app = QApplication([])
    ex = MainWindow()
    sys.exit(app.exec())
