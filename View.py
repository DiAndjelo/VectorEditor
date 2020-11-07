from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Figures.Rectangle import Rectangle


class GraphicsScene(QGraphicsScene):
    clicked = pyqtSignal(QPointF)

    def mousePressEvent(self, event):
        sp = event.scenePos()
        self.clicked.emit(sp)
        super().mousePressEvent(event)


class Editor(QMainWindow):
    def __init__(self):
        super().__init__()
        # Статус (что нажато). прим. rect, line, clear etc...
        self.state = ""
        # Определение размеров и title окна Editor
        self.resize(520, 550)
        self.setWindowTitle('GraphicsEditor')
        # Виджет для отображение GraphicsScene()
        self.grview = QGraphicsView()
        self.grview.scale(1, -1)
        # Фрейм на котором происходит отрисовка
        self.scene = GraphicsScene()
        self.scene.setSceneRect(-250, -250, 500, 500)
        # Включаем поддержку отслеживания нажатия/движения мыши
        self.setMouseTracking(True)
        # Подключаем GraphicsScene к QGraphicsView
        self.grview.setScene(self.scene)
        # Подключаем основу и контур
        self.pen = QPen(Qt.red)
        self.brush = QBrush(Qt.green)
        self.scene.clicked.connect(self.handle_clicked)
        # Подключаем actions к сцене
        self.set_figure()
        # Подключаем методы по нажатию на action
        self.trash_action.triggered.connect(self.clear)
        self.line_action.triggered.connect(self.click_line)
        self.rect_action.triggered.connect(self.click_rect)
        self.circle_action.triggered.connect(self.click_circle)
        self.color_selection.triggered.connect(self.openColorDialog)
        self.circuit_selection.triggered.connect(self.openColorBrush)
        # Подключаем дополнительные виджеты
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        layout = QVBoxLayout(self.centralWidget)
        layout.setContentsMargins(0, 0, 0, 0)  # +
        layout.addWidget(self.grview)

    def mousePressEvent(self, event):
        """
        Действие по нажатию на клавишу мыши
        :param event: Событие
        """
        # ToDo: написать корректные методы отрисовки
        if self.state == "rect":
                rect = Rectangle(self.pen, self.brush, self.x, self.y, 200, 200)
                # rect = self.scene.addRect(self.x, self.y, 100, 100, self.pen, self.brush)
                # rect.setFlag(QGraphicsItem.ItemIsMovable)
                self.scene.addItem(rect)
        elif self.state == "circle":
                circle = self.scene.addEllipse(self.x, self.y, 100, 100, self.pen, self.brush)
                circle.setFlag(QGraphicsItem.ItemIsMovable)
        elif self.state == "line":
                line = self.scene.addLine(self.x, self.y, 100, 100, self.pen)
                line.setFlag(QGraphicsItem.ItemIsMovable)
        super(Editor, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        """
        Метод движения мыши???
        :param event: Событие
        """
        # ToDo: понять зачем оно надо
        super(Editor, self).mouseMoveEvent(event)

    def set_figure(self):
        # Тул бар(хрень, которая наверху фрейма)
        self.figure_toolbar = QToolBar("figure")
        self.figure_toolbar.setIconSize(QSize(14, 14))
        self.basicToolBar = self.addToolBar(self.figure_toolbar)
        # кнопка line
        self.line_action = QAction(QIcon("images/line.png"), 'line', self)
        self.line_action.setStatusTip("line")
        self.figure_toolbar.addAction(self.line_action)
        # кнопка rectangle
        self.rect_action = QAction(QIcon("images/rect.png"), 'rectangle', self)
        self.rect_action.setStatusTip("rect")
        self.figure_toolbar.addAction(self.rect_action)
        # кнопка круг
        self.circle_action = QAction(QIcon("images/circle.ico"), 'circle', self)
        self.circle_action.setStatusTip("circle")
        self.figure_toolbar.addAction(self.circle_action)
        # кнопка select
        self.select_action = QAction(QIcon("images/select.ico"), 'select', self)
        self.select_action.setStatusTip("select")
        self.figure_toolbar.addAction(self.select_action)
        # кнопка очистки
        self.trash_action = QAction(QIcon("images/trash.png"), 'trash', self)
        self.trash_action.setStatusTip("trash")
        self.figure_toolbar.addAction(self.trash_action)
        # кнопка выбора цвета
        self.color_selection = QAction('Сменить цвет \nфигуры', self)
        self.color_selection.setStatusTip("color")
        self.figure_toolbar.addAction(self.color_selection)
        # кнопка выбора цвета
        self.circuit_selection = QAction('Сменить цвет \nконтура', self)
        self.circuit_selection.setStatusTip("color")
        self.figure_toolbar.addAction(self.circuit_selection)

    def openColorDialog(self):
        """
        Смена цвета фигуры
        """
        self.color = QColorDialog.getColor()
        self.brush = QBrush(self.color)

    def openColorBrush(self):
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
        self.scene.clear()

    def handle_clicked(self, p):
        """
        Считывание параметров положения мыши
        """
        self.x = p.x()
        self.y = p.y()
