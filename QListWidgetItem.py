import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QListWidget, QListWidgetItem,
                             QInputDialog, QHBoxLayout, QVBoxLayout)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setMinimumSize(400, 200)
        self.setWindowTitle("QListWidget Example")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        self.list_widget = QListWidget()
        self.list_widget.setAlternatingRowColors(True)

        items = ["grapes", "garlic", "cheese", "bacon", "eggs", "rice", "soda"]
        for item in items:
            list_item = QListWidgetItem()
            list_item.setText(item)
            self.list_widget.addItem(list_item)

        add_button = QPushButton("Add")
        add_button.clicked.connect(self.addListItem)

        insert_button = QPushButton("Insert")
        insert_button.clicked.connect(self.insertItemInList)

        remove_button = QPushButton("Remove")
        remove_button.clicked.connect(self.removeOneItem)

        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.list_widget.clear)

        right_v_box = QVBoxLayout()
        right_v_box.addWidget(add_button)
        right_v_box.addWidget(insert_button)
        right_v_box.addWidget(remove_button)
        right_v_box.addWidget(clear_button)

        main_h_box = QHBoxLayout()
        main_h_box.addWidget(self.list_widget)
        main_h_box.addLayout(right_v_box)

        self.setLayout(main_h_box)


    def addListItem(self):
        text, ok = QInputDialog.getText(self, "New Item", "Add item:")
        if ok and text != "":
            list_item = QListWidgetItem()
            list_item.setText(text)
            self.list_widget.addItem(list_item)

    def insertItemInList(self):
        text, ok = QInputDialog.getText(self, "Insert Item", "Insert item:")
        if ok and text != "":
            row = self.list_widget.currentRow()
            row = row + 1
            new_item = QListWidgetItem()
            new_item.setText(text)
            self.list_widget.insertItem(row, new_item)

    def removeOneItem(self):
        row = self.list_widget.currentRow()
        item = self.list_widget.takeItem(row)
        return item


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())