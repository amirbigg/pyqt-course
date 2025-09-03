import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QCheckBox, QMessageBox
from PyQt6.QtGui import QFont, QPixmap
from registration import NewUserDialog


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        self.setFixedSize(360, 220)
        self.setWindowTitle("User Login")
        self.setup_window()
        self.show()

    def setup_window(self):
        self.login_is_successful = False

        login_label = QLabel("Login", self)
        login_label.setFont(QFont("Arial", 20))
        login_label.move(160, 10)

        username_label = QLabel("Username: ", self)
        username_label.move(20, 54)

        self.username_edit = QLineEdit(self)
        self.username_edit.resize(250, 24)
        self.username_edit.move(90, 50)

        password_label = QLabel("Password: ", self)
        password_label.move(20, 86)

        self.password_edit = QLineEdit(self)
        self.password_edit.resize(250, 24)
        self.password_edit.move(90, 82)
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)

        self.show_password_cb = QCheckBox("Show password", self)
        self.show_password_cb.move(90, 110)
        self.show_password_cb.toggled.connect(self.display_password_if_checked)

        login_button = QPushButton("Login", self)
        login_button.resize(320, 34)
        login_button.move(20, 140)
        login_button.clicked.connect(self.click_login_button)

        not_member_label = QLabel("Not a member?", self)
        not_member_label.move(20, 186)

        sign_up_button = QPushButton("Sign up", self)
        sign_up_button.move(120, 180)
        sign_up_button.clicked.connect(self.create_new_user)

    def click_login_button(self):
        users = {}
        file = "files/users.txt"
        with open(file, "r") as f:
            for line in f:
                user_info = line.split(" ")
                username_info = user_info[0]
                password_info = user_info[1].strip("\n")
                users[username_info] = password_info

        username = self.username_edit.text()
        password = self.password_edit.text()

        if (username, password) in users.items():
            QMessageBox.information(self, "Login successful!", "you logged in successfully..!",
                                    QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
            self.login_is_successful = True
            self.close()
            self.open_application_window()
        else:
            QMessageBox.warning(self, "Error!", "username or password is wrong..!",
                                QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)


    def display_password_if_checked(self, checked):
        if checked:
            self.password_edit.setEchoMode(QLineEdit.EchoMode.Normal)
        elif checked == False:
            self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)

    def create_new_user(self):
        self.create_new_user_window = NewUserDialog()
        self.create_new_user_window.show()

    def open_application_window(self):
        self.main_window = MainWindow()
        self.main_window.show()

    def closeEvent(self, event):
        if self.login_is_successful == True:
            event.accept()
        else:
            answer = QMessageBox.question(self, "Quit Application", "Are you sure you want to QUIT?",
                                          QMessageBox.StandardButton.No | QMessageBox.StandardButton.Yes,
                                          QMessageBox.StandardButton.No)
            if answer == QMessageBox.StandardButton.Yes:
                event.accept()
            if answer == QMessageBox.StandardButton.No:
                event.ignore()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        self.setMinimumSize(640, 426)
        self.setWindowTitle("User login")
        self.setup_main_window()
        self.show()

    def setup_main_window(self):
        image = "./images/background_kingfisher.jpg"
        with open(image):
            main_label = QLabel(self)
            pixmap = QPixmap(image)
            main_label.setPixmap(pixmap)
            main_label.move(0, 0)
            main_label.resize(640, 426)

if __name__ == '__main__':
    app = QApplication([])
    window = LoginWindow()
    sys.exit(app.exec())
