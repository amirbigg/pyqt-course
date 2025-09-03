from PyQt6.QtWidgets import QDialog, QLabel, QPushButton, QLineEdit, QMessageBox
from PyQt6.QtGui import QFont, QPixmap


class NewUserDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.initializeUI()

    def initializeUI(self):
        self.setFixedSize(360, 320)
        self.setWindowTitle("3.1 - Registration GUI")
        self.setUpWindow()

    def setUpWindow(self):
        login_label = QLabel("Create New Account", self)
        login_label.setFont(QFont("Arial", 20))
        login_label.move(90, 20)

        user_image = "images/new_user_icon.png"
        with open(user_image):
            user_label = QLabel(self)
            pixmap = QPixmap(user_image)
            user_label.setPixmap(pixmap)
            user_label.move(150, 60)

        name_label = QLabel("Username:", self)
        name_label.move(20, 144)

        self.name_edit = QLineEdit(self)
        self.name_edit.resize(250, 24)
        self.name_edit.move(90, 140)

        new_pswd_label = QLabel("Password:", self)
        new_pswd_label.move(20, 204)

        self.new_pswd_edit = QLineEdit(self)
        self.new_pswd_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.new_pswd_edit.resize(250, 24)
        self.new_pswd_edit.move(90, 200)

        confirm_label = QLabel("Confirm:", self)
        confirm_label.move(20, 234)

        self.confirm_edit = QLineEdit(self)
        self.confirm_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirm_edit.resize(250, 24)
        self.confirm_edit.move(90, 230)

        sign_up_button = QPushButton("Sign Up", self)
        sign_up_button.resize(320, 32)
        sign_up_button.move(20, 270)
        sign_up_button.clicked.connect(self.confirmSignUp)

    def confirmSignUp(self):
        name_text = self.name_edit.text()
        pswd_text = self.new_pswd_edit.text()
        confirm_text = self.confirm_edit.text()

        if name_text == "" or pswd_text == "":
            QMessageBox.warning(self, "Error!", "Please enter username or password values..!",
                                QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
        elif pswd_text != confirm_text:
            QMessageBox.warning(self, "Error!", "passwords must match..!",
                                QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
        else:
            with open("files/users.txt", "a+") as f:
                f.write("\n" + name_text + " ")
                f.write(pswd_text)
            self.close()
