import os, sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QStatusBar, QToolTip, QColorDialog, QFileDialog
from PyQt6.QtCore import Qt, QSize, QPoint, QRect
from PyQt6.QtGui import QPainter, QPixmap, QPen, QColor, QIcon, QFont, QAction


class Canvas(QLabel):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        width, height = parent.width(), parent.height()

        self.pixmap = QPixmap(width, height)
        self.pixmap.fill(Qt.GlobalColor.white)
        self.setPixmap(self.pixmap)

        self.mouse_track_label = QLabel()
        self.setMouseTracking(True)

        self.antialiasing_status = False
        self.eraser_selected = False

        self.last_mouse_pos = QPoint()
        self.drawing = False
        self.pen_color = Qt.GlobalColor.black
        self.pen_width = 2

    def selectDrawingTool(self, tool):
        if tool == "pencil":
            self.eraser_selected = False
            self.pen_width = 2
        elif tool == "marker":
            self.eraser_selected = False
            self.pen_width = 8
        elif tool == "eraser":
            self.eraser_selected = True
        elif tool == "color":
            self.eraser_selected = False
            color = QColorDialog.getColor()
            if color.isValid():
                self.pen_color = color

    def drawOnCanvas(self, points):
        painter = QPainter(self.pixmap)

        if self.antialiasing_status:
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        if self.eraser_selected == False:
            pen = QPen(QColor(self.pen_color), self.pen_width)
            painter.setPen(pen)
            painter.drawLine(self.last_mouse_pos, points)
            self.last_mouse_pos = points
        elif self.eraser_selected == True:
            eraser = QRect(points.x(), points.y(), 12, 12)
            painter.eraseRect(eraser)
        self.update()

    def mouseMoveEvent(self, event):
        mouse_pos = event.pos()
        if (event.buttons() and Qt.MouseButton.LeftButton) and self.drawing:
            self.drawOnCanvas(mouse_pos)

        self.mouse_track_label.setVisible(True)
        sb_text = f"<p>Mouse Coordinates: ({mouse_pos.x()}, {mouse_pos.y()})</p>"
        self.mouse_track_label.setText(sb_text)
        self.parent.status_bar.addWidget(self.mouse_track_label)

    def newCanvas(self):
        self.pixmap.fill(Qt.GlobalColor.white)
        self.update()

    def saveFile(self):
        file_format = "png"
        default_name = os.path.curdir + "/untitled." + file_format
        file_name, _ = QFileDialog.getSaveFileName(self, "Save As", default_name, "PNG Format (*.png)")

        if file_name:
            self.pixmap.save(file_name, file_format)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.last_mouse_pos = event.pos()
            self.drawing = True

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = False
        elif self.eraser_selected == True:
            self.eraser_selected = False

    def paintEvent(self, event):
        painter = QPainter(self)
        source_rect = event.rect()
        target_rect = event.rect()
        painter.drawPixmap(target_rect, self.pixmap, source_rect)
        painter.end()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setMinimumSize(900, 600)
        self.setWindowTitle("Painter GUI")

        self.setUpMainWindow()
        self.createActions()
        self.createMenu()
        self.createToolbar()
        self.show()

    def setUpMainWindow(self):
        self.canvas = Canvas(self)
        self.setCentralWidget(self.canvas)

    def createActions(self):
        self.new_act = QAction("New Canvas")
        self.new_act.setShortcut("Ctrl+N")
        self.new_act.triggered.connect(self.canvas.newCanvas)

        self.save_file_act = QAction("Save File")
        self.save_file_act.setShortcut("Ctrl+S")
        self.save_file_act.triggered.connect(self.canvas.saveFile)

        self.quit_act = QAction("Quit")
        self.quit_act.setShortcut("Ctrl+Q")
        self.quit_act.triggered.connect(self.close)

        self.anti_al_act = QAction("AntiAliasing", checkable=True)
        self.anti_al_act.triggered.connect(self.turnAntiAliasingOn)

    def createMenu(self):
        self.menuBar().setNativeMenuBar(False)

        file_menu = self.menuBar().addMenu("File")
        file_menu.addAction(self.new_act)
        file_menu.addAction(self.save_file_act)
        file_menu.addSeparator()
        file_menu.addAction(self.quit_act)

        tools_menu = self.menuBar().addMenu("Tools")
        tools_menu.addAction(self.anti_al_act)

        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

    def createToolbar(self):
        QToolTip.setFont(QFont("Helvetica", 12))
        tool_bar = QToolBar("Painting Toolbar")
        tool_bar.setIconSize(QSize(24, 24))
        self.addToolBar(Qt.ToolBarArea.LeftToolBarArea, tool_bar)
        tool_bar.setMovable(False)

        pencil_act = QAction(QIcon("icons/pencil.png"), "Pencil", tool_bar)
        pencil_act.setToolTip("This is the <b>Pencil</b>")
        pencil_act.triggered.connect(lambda: self.canvas.selectDrawingTool("pencil"))

        marker_act = QAction(QIcon("icons/marker.png"), "Marker", tool_bar)
        marker_act.setToolTip("This is the <b>Marker</b>")
        marker_act.triggered.connect(lambda: self.canvas.selectDrawingTool("marker"))

        eraser_act = QAction(QIcon("icons/eraser.png"), "Eraser", tool_bar)
        eraser_act.setToolTip("Use the <b>Eraser</b> to make it all disappear")
        eraser_act.triggered.connect(lambda: self.canvas.selectDrawingTool("eraser"))

        color_act = QAction(QIcon("icons/colors.png"), "Colors", tool_bar)
        color_act.setToolTip("Choose a <b>Color</b> from the Color dialog")
        color_act.triggered.connect(lambda: self.canvas.selectDrawingTool("color"))

        tool_bar.addAction(pencil_act)
        tool_bar.addAction(marker_act)
        tool_bar.addAction(eraser_act)
        tool_bar.addAction(color_act)

    def turnAntiAliasingOn(self, state):
        if state:
            self.canvas.antialiasing_status = True
        else:
            self.canvas.antialiasing_status = False

    def leaveEvent(self, event):
        self.canvas.mouse_track_label.setVisible(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setAttribute(Qt.ApplicationAttribute.AA_DontShowIconsInMenus, True)
    window = MainWindow()
    sys.exit(app.exec())
