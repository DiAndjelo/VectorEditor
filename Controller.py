from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from GraphObject import GraphObject


class Controller:
    def __init__(self):
        # Статус (что нажато). прим. rect, line, clear etc...
        self.state = ""
        # Инициализация GraphObject
        self.graph = GraphObject(self)
        # Подключаем основу и контур
        self.pen = QPen(Qt.red)
        self.brush = QBrush(Qt.green)

        # Подключаем методы по нажатию на action
        self.graph.scene.clicked.connect(self.handle_clicked)
        self.graph.trash_action.triggered.connect(self.clear)
        self.graph.line_action.triggered.connect(self.click_line)
        self.graph.rect_action.triggered.connect(self.click_rect)
        self.graph.circle_action.triggered.connect(self.click_circle)
        self.graph.color_selection.triggered.connect(self.open_color_dialog)
        self.graph.circuit_selection.triggered.connect(self.open_color_brush)

    def open_color_dialog(self):
        """
        Смена цвета фигуры
        """
        self.color = QColorDialog.getColor()
        self.brush = QBrush(self.color)

    def open_color_brush(self):
        """
        Смена цвета контура фигуры
        """
        self.color = QColorDialog.getColor()
        self.pen = QPen(self.color)

    def click_line(self):
        """
        Смена состояния на line
        """
        self.state = "line"

    def click_rect(self):
        """
        Смена состояния на rect
        """
        self.state = "rect"

    def click_circle(self):
        """
        Смена состояния на circle
        """
        self.state = "circle"

    def clear(self):
        """
        Очистка сцены
        """
        self.graph.scene.clear()

    def handle_clicked(self, p):
        """
        Считывание параметров положения мыши
        """
        self.x = p.x()
        self.y = p.y()
