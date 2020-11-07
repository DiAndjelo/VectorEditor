from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Figures.Ellipse import Ellipse
from Figures.Line import Line
from Figures.Rectangle import Rectangle
from Painter import Painter


class GraphicsScene(QGraphicsScene):
    clicked = pyqtSignal(QPointF)

    def mousePressEvent(self, event):
        sp = event.scenePos()
        self.clicked.emit(sp)
        super().mousePressEvent(event)


class GraphObject(QMainWindow):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        # Определение размеров и title окна GraphObject
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
        # Подключаем actions к сцене
        self.set_actions()
        # Подключаем дополнительные виджеты
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        layout = QVBoxLayout(self.centralWidget)
        layout.setContentsMargins(0, 0, 0, 0)  # +
        layout.addWidget(self.grview)
        self.painter = Painter(self)
        self.show()

    def set_actions(self):
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

    def mousePressEvent(self, event):
        """
        Действие по нажатию на клавишу мыши
        :param event: Событие
        """
        # ToDo: написать корректные методы отрисовки
        if self.parent.state == "rect":
            self.painter.rect(self.parent.pen, self.parent.brush, self.parent.x, self.parent.y, 200, 200)
        elif self.parent.state == "circle":
            self.painter.ellipse(self.parent.pen, self.parent.brush, self.parent.x, self.parent.y, 200, 200)
        elif self.parent.state == "line":
            self.painter.line(self.parent.pen, self.parent.x, self.parent.y, 200, 200)
        super(GraphObject, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        """
        Метод движения мыши???
        :param event: Событие
        """
        # ToDo: понять зачем оно надо
        super(GraphObject, self).mouseMoveEvent(event)
