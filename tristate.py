import sys
from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QGroupBox, QButtonGroup, QVBoxLayout
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__() 
        self.initializeUI()

    def initializeUI(self):
        self.setMinimumSize(300, 200)
        self.setWindowTitle("Tri-State Example")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        self.tristate_cb = QCheckBox("Select all toppings")
        self.tristate_cb.stateChanged.connect(self.updateTristateCb)

        topping1_cb = QCheckBox("Chocolate Chips")
        topping1_cb.setStyleSheet("padding-left: 20px")
        topping2_cb = QCheckBox("Gummy Bears")
        topping2_cb.setStyleSheet("padding-left: 20px")
        topping3_cb = QCheckBox("Oreos, Peanuts")
        topping3_cb.setStyleSheet("padding-left: 20px")

        self.button_group = QButtonGroup(self)
        self.button_group.setExclusive(False)
        self.button_group.addButton(topping1_cb)
        self.button_group.addButton(topping2_cb)
        self.button_group.addButton(topping3_cb)
        self.button_group.buttonToggled.connect(self.checkButtonState)

        gb_v_box = QVBoxLayout()
        gb_v_box.addWidget(self.tristate_cb)
        gb_v_box.addWidget(topping1_cb)
        gb_v_box.addWidget(topping2_cb)
        gb_v_box.addWidget(topping3_cb)
        gb_v_box.addStretch()

        group_box = QGroupBox("Choose the toppings for your ice cream")
        group_box.setLayout(gb_v_box)

        main_v_box = QVBoxLayout()
        main_v_box.addWidget(group_box)
        self.setLayout(main_v_box)

    def updateTristateCb(self, state):
        for button in self.button_group.buttons():
            if state == 2: # Qt.CheckState.Checked
                button.setChecked(True)
            elif state == 0: # Qt.CheckState.Unchecked
                button.setChecked(False)

    def checkButtonState(self, button, checked):
        button_states = []

        for button in self.button_group.buttons():
            button_states.append(button.isChecked())

        if all(button_states):
            self.tristate_cb.setCheckState(Qt.CheckState.Checked)
            self.tristate_cb.setTristate(False)
        elif any(button_states) == False:
            self.tristate_cb.setCheckState(Qt.CheckState.Unchecked)
            self.tristate_cb.setTristate(False)
        else:
            self.tristate_cb.setCheckState(Qt.CheckState.PartiallyChecked)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
