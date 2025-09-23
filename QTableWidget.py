import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QMenu, QInputDialog
from PyQt6.QtGui import QAction
from PyQt6.QtCore import QPoint


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setMinimumSize(1000, 500)
        self.setWindowTitle("QTableWidget Example")

        self.item_text = None

        self.setUpMainWindow()
        self.createActions()
        self.createMenu()

        self.show()

    def setUpMainWindow(self):
        self.table_widget = QTableWidget()

        self.table_widget.setRowCount(10)
        self.table_widget.setColumnCount(10)

        self.table_widget.setCurrentCell(0, 0)

        h_header = self.table_widget.horizontalHeader()
        h_header.sectionDoubleClicked.connect(self.changeHeader)

        self.setCentralWidget(self.table_widget)

    def createActions(self):
        self.quit_act = QAction("Quit", self)
        self.quit_act.setShortcut("Ctrl+Q")
        self.quit_act.triggered.connect(self.close)

        self.add_row_above_act = QAction("Add Row Above", self)
        self.add_row_above_act.triggered.connect(self.addRowAbove)

        self.add_row_below_act = QAction("Add Row Below", self)
        self.add_row_below_act.triggered.connect(self.addRowBelow)

        self.add_col_before_act = QAction("Add Column Before", self)
        self.add_col_before_act.triggered.connect(self.addColumnBefore)

        self.add_col_after_act = QAction("Add Column After", self)
        self.add_col_after_act.triggered.connect(self.addColumnAfter)

        self.delete_row_act = QAction("Delete Row", self)
        self.delete_row_act.triggered.connect(self.deleteRow)

        self.delete_col_act = QAction("Delete Column", self)
        self.delete_col_act.triggered.connect(self.deleteColumn)

        self.clear_table_act = QAction("Clear All", self)
        self.clear_table_act.triggered.connect(self.clearTable)

    def createMenu(self):
        self.menuBar().setNativeMenuBar(False)

        file_menu = self.menuBar().addMenu('File')
        file_menu.addAction(self.quit_act)

        table_menu = self.menuBar().addMenu('Table')
        table_menu.addAction(self.add_row_above_act)
        table_menu.addAction(self.add_row_below_act)
        table_menu.addSeparator()
        table_menu.addAction(self.add_col_before_act)
        table_menu.addAction(self.add_col_after_act)
        table_menu.addSeparator()
        table_menu.addAction(self.delete_row_act)
        table_menu.addAction(self.delete_col_act)
        table_menu.addSeparator()
        table_menu.addAction(self.clear_table_act)

    def contextMenuEvent(self, event):
        context_menu = QMenu(self)
        context_menu.addAction(self.add_row_above_act)
        context_menu.addAction(self.add_row_below_act)
        context_menu.addSeparator()
        context_menu.addAction(self.add_col_before_act)
        context_menu.addAction(self.add_col_after_act)
        context_menu.addSeparator()
        context_menu.addAction(self.delete_row_act)
        context_menu.addAction(self.delete_col_act)
        context_menu.addSeparator()
        copy_act = context_menu.addAction("Copy")
        paste_act = context_menu.addAction("Paste")
        context_menu.addSeparator()
        context_menu.addAction(self.clear_table_act)


        action = context_menu.exec(self.mapToGlobal(event.pos()))

        if action == copy_act:
            self.copyItem()
        if action == paste_act:
            self.pasteItem()

    def changeHeader(self):
        col = self.table_widget.currentColumn()
        text, ok = QInputDialog.getText(self, "Enter Header", "Header text:")
        if ok and text != "":
            self.table_widget.setHorizontalHeaderItem(col, QTableWidgetItem(text))

    def copyItem(self):
        if self.table_widget.currentItem() != None:
            self.item_text = self.table_widget.currentItem().text()

    def pasteItem(self):
        if self.item_text != None:
            row = self.table_widget.currentRow()
            column = self.table_widget.currentColumn()
            self.table_widget.setItem(row, column, QTableWidgetItem(self.item_text))

    def addRowAbove(self):
        current_row = self.table_widget.currentRow()
        self.table_widget.insertRow(current_row)

    def addRowBelow(self):
        current_row = self.table_widget.currentRow()
        self.table_widget.insertRow(current_row + 1)

    def addColumnBefore(self):
        current_col = self.table_widget.currentColumn()
        self.table_widget.insertColumn(current_col)

    def addColumnAfter(self):
        current_col = self.table_widget.currentColumn()
        self.table_widget.insertColumn(current_col + 1)

    def deleteRow(self):
        current_row = self.table_widget.currentRow()
        self.table_widget.removeRow(current_row)

    def deleteColumn(self):
        current_col = self.table_widget.currentColumn()
        self.table_widget.removeColumn(current_col)

    def clearTable(self):
        self.table_widget.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
