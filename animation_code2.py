from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QHBoxLayout, QSizePolicy
from PyQt6.QtGui import QColor
from PyQt6.QtCore import QPropertyAnimation, pyqtProperty
import sys


class MyLabel(QLabel):
    def __init__(self, text):
        super().__init__(text)

    def _set_color(self, col):
        palette = self.palette()
        palette.setColor(self.foregroundRole(), col)
        self.setPalette(palette)

    color = pyqtProperty(QColor, fset=_set_color)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)
        self.button = QPushButton("Start", self)
        self.button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        hbox.addWidget(self.button)
        hbox.addSpacing(40)

        self.label = MyLabel("Hello User..!")
        font = self.label.font()
        font.setPointSize(35)
        self.label.setFont(font)
        hbox.addWidget(self.label)

        self.anim = QPropertyAnimation(self.label, b"color")
        self.anim.setDuration(3000)
        self.anim.setLoopCount(2)
        self.anim.setStartValue(QColor(0, 0, 0))
        self.anim.setEndValue(QColor(0, 110, 150))

        self.button.clicked.connect(self.anim.start)

        self.setGeometry(300, 300, 380, 250)
        self.setWindowTitle('Color anim')
        self.show()


if __name__ == "__main__":
    app = QApplication([])
    ex = MainWindow()
    sys.exit(app.exec())
