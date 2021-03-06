from PyQt5.QtCore import Qt, QRectF, QPointF, QLineF
from PyQt5.QtGui import QBrush, QPainterPath, QPainter, QColor, QPen
from PyQt5.QtWidgets import (QGraphicsItem, QGraphicsLineItem)


class Line(QGraphicsLineItem):
    """
    Класс объекта прямоугольник
    """
    handleTopLeft = 1
    handleTopMiddle = 2
    handleTopRight = 3
    handleMiddleLeft = 4
    handleMiddleRight = 5
    handleBottomLeft = 6
    handleBottomMiddle = 7
    handleBottomRight = 8

    handleSize = +8.0
    handleSpace = -4.0

    handleCursors = {
        handleTopLeft: Qt.SizeFDiagCursor,
        handleTopMiddle: Qt.SizeVerCursor,
        handleTopRight: Qt.SizeBDiagCursor,
        handleMiddleLeft: Qt.SizeHorCursor,
        handleMiddleRight: Qt.SizeHorCursor,
        handleBottomLeft: Qt.SizeBDiagCursor,
        handleBottomMiddle: Qt.SizeVerCursor,
        handleBottomRight: Qt.SizeFDiagCursor,
    }

    def __init__(self, color, th, *args):
        super().__init__(*args)
        self.color = color
        self.thick = th
        self.handles = {}
        self.handleSelected = None
        self.mousePressPos = None
        self.mousePressline = None
        self.setAcceptHoverEvents(True)
        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges, True)
        self.setFlag(QGraphicsItem.ItemIsFocusable, True)
        self.updateHandlesPos()

    def handleAt(self, point):
        """  Возвращает маркер изменения размера ниже заданной точки.
        """
        for k, v, in self.handles.items():
            if v.contains(point):
                return k
        return None

    def hoverMoveEvent(self, moveEvent):
        if self.isSelected():
            handle = self.handleAt(moveEvent.pos())
            cursor = Qt.ArrowCursor if handle is None else self.handleCursors[handle]
            self.setCursor(cursor)

        super().hoverMoveEvent(moveEvent)

    def hoverLeaveEvent(self, moveEvent):
        self.setCursor(Qt.ArrowCursor)

        super().hoverLeaveEvent(moveEvent)

    def mousePressEvent(self, mouseEvent):
        """ Выполняется при нажатии мыши на item.
        """
        self.handleSelected = self.handleAt(mouseEvent.pos())
        if self.handleSelected:
            self.mousePressPos = mouseEvent.pos()
            self.mousePressline = self.boundingline()

        super().mousePressEvent(mouseEvent)

    def mouseMoveEvent(self, mouseEvent):
        """ Выполняется, когда мышь перемещается по элементу при нажатии.
        """

        if self.handleSelected is not None:
            self.interactiveResize(mouseEvent.pos())
        else:
            super().mouseMoveEvent(mouseEvent)

    def mouseReleaseEvent(self, mouseEvent):
        """ Выполняется, когда мышь is released from the item.
        """

        super().mouseReleaseEvent(mouseEvent)
        self.handleSelected = None
        self.mousePressPos = None
        self.mousePressline = None
        self.update()

    def boundingline(self):
        """ Возвращает ограничивающий прямоугольник фигуры
        (включая маркеры изменения размера).
        """
        o = self.handleSize + self.handleSpace
        return self.line().setLine(-o, -o, o, o)

    def updateHandlesPos(self):
        """ Обновите текущие маркеры изменения размера
        в соответствии с размером и положением фигуры.
        """
        s = self.handleSize
        b = self.boundingline()
        self.handles[self.handleTopLeft] = QLineF(b.left(), b.top(), s, s)
        self.handles[self.handleTopMiddle] = QLineF(b.center().x() - s / 2, b.top(), s, s)
        self.handles[self.handleTopRight] = QLineF(b.right() - s, b.top(), s, s)
        self.handles[self.handleMiddleLeft] = QLineF(b.left(), b.center().y() - s / 2, s, s)
        self.handles[self.handleMiddleRight] = QLineF(b.right() - s, b.center().y() - s / 2, s, s)
        self.handles[self.handleBottomLeft] = QLineF(b.left(), b.bottom() - s, s, s)
        self.handles[self.handleBottomMiddle] = QLineF(b.center().x() - s / 2, b.bottom() - s, s, s)
        self.handles[self.handleBottomRight] = QLineF(b.right() - s, b.bottom() - s, s, s)

    def interactiveResize(self, mousePos):
        """ Выполните интерактивное изменение размера формы.
        """
        offset = self.handleSize + self.handleSpace
        boundingline = self.boundingline()
        line = self.line()
        diff = QPointF(0, 0)

        self.prepareGeometryChange()

        if self.handleSelected == self.handleTopLeft:
            fromX = self.mousePressline.left()
            fromY = self.mousePressline.top()
            toX = fromX + mousePos.x() - self.mousePressPos.x()
            toY = fromY + mousePos.y() - self.mousePressPos.y()
            diff.setX(toX - fromX)
            diff.setY(toY - fromY)
            boundingline.setLeft(toX)
            boundingline.setTop(toY)
            line.setLeft(boundingline.left() + offset)
            line.setTop(boundingline.top() + offset)
            self.setline(line)
        elif self.handleSelected == self.handleTopMiddle:
            fromY = self.mousePressline.top()
            toY = fromY + mousePos.y() - self.mousePressPos.y()
            diff.setY(toY - fromY)
            boundingline.setTop(toY)
            line.setTop(boundingline.top() + offset)
            self.setline(line)
        elif self.handleSelected == self.handleTopRight:
            fromX = self.mousePressline.right()
            fromY = self.mousePressline.top()
            toX = fromX + mousePos.x() - self.mousePressPos.x()
            toY = fromY + mousePos.y() - self.mousePressPos.y()
            diff.setX(toX - fromX)
            diff.setY(toY - fromY)
            boundingline.setRight(toX)
            boundingline.setTop(toY)
            line.setRight(boundingline.right() - offset)
            line.setTop(boundingline.top() + offset)
            self.setline(line)
        elif self.handleSelected == self.handleMiddleLeft:
            fromX = self.mousePressline.left()
            toX = fromX + mousePos.x() - self.mousePressPos.x()
            diff.setX(toX - fromX)
            boundingline.setLeft(toX)
            line.setLeft(boundingline.left() + offset)
            self.setline(line)
        elif self.handleSelected == self.handleMiddleRight:
            fromX = self.mousePressline.right()
            toX = fromX + mousePos.x() - self.mousePressPos.x()
            diff.setX(toX - fromX)
            boundingline.setRight(toX)
            line.setRight(boundingline.right() - offset)
            self.setline(line)
        elif self.handleSelected == self.handleBottomLeft:
            fromX = self.mousePressline.left()
            fromY = self.mousePressline.bottom()
            toX = fromX + mousePos.x() - self.mousePressPos.x()
            toY = fromY + mousePos.y() - self.mousePressPos.y()
            diff.setX(toX - fromX)
            diff.setY(toY - fromY)
            boundingline.setLeft(toX)
            boundingline.setBottom(toY)
            line.setLeft(boundingline.left() + offset)
            line.setBottom(boundingline.bottom() - offset)
            self.setline(line)
        elif self.handleSelected == self.handleBottomMiddle:
            fromY = self.mousePressline.bottom()
            toY = fromY + mousePos.y() - self.mousePressPos.y()
            diff.setY(toY - fromY)
            boundingline.setBottom(toY)
            line.setBottom(boundingline.bottom() - offset)
            self.setline(line)
        elif self.handleSelected == self.handleBottomRight:
            fromX = self.mousePressline.right()
            fromY = self.mousePressline.bottom()
            toX = fromX + mousePos.x() - self.mousePressPos.x()
            toY = fromY + mousePos.y() - self.mousePressPos.y()
            diff.setX(toX - fromX)
            diff.setY(toY - fromY)
            boundingline.setRight(toX)
            boundingline.setBottom(toY)
            line.setRight(boundingline.right() - offset)
            line.setBottom(boundingline.bottom() - offset)
            self.setline(line)

        self.updateHandlesPos()

    def shape(self):
        """ Возвращает форму этого элемента в виде QPainterPath в локальных координатах.
        """
        path = QPainterPath()
        path.addline(self.line())
        if self.isSelected():
            for shape in self.handles.values():
                path.addEllipse(shape)
        return path

    def paint(self, painter, option, widget=None):
        """ Нарисуйте узел в графическом представлении.
        """
        painter.setBrush(self.thick)
        painter.setPen(self.color)
        painter.drawLine(self.line())
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(QColor(255, 255, 0, 255)))  # маркеры
        painter.setPen(QPen(QColor(0, 0, 0, 255), 1.0, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        for handle, line in self.handles.items():
            if self.handleSelected is None or handle == self.handleSelected:
                painter.drawEllipse(line)
