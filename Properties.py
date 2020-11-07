from PyQt5 import QtGui


class Properties:
    """
    Класс свойств
    """
    def __init__(self):
        """
        Добавление свойств ручки и кисти
        """
        list_prop = []
        color = QtGui.QColor(0, 0, 255, 155)
        list_prop.append(PenProps(color, 1))
        list_prop.append(BrushProps(color))


class PropGroup:
    """
    Абстрактный класс свойств
    """
    def apply_props(self, painter):
        """
        Применение всех свойств к Painter'у
        :param painter: класс Painter
        """
        pass


class PenProps(PropGroup):
    """
    Класс свойств ручки
    """
    pen_color = QtGui.QColor(0, 0, 255, 155)
    pen_width = 1

    def __init__(self, _pen_color, _pen_width):
        self.pen_color = _pen_color
        self.pen_width = _pen_width

    def apply_props(self, painter):
        """
        Перезаписываем применение всех свойств к Painter'у для ручки
        :param painter: класс Painter
        """
        painter.pen_color = self.pen_color
        painter.pen_width = self.pen_width


class BrushProps(PropGroup):
    """
    Класс свойств кисти
    """
    brush_prop = QtGui.QColor(0, 0, 255, 155)

    def __init__(self, _brush_prop):
        self.brush_prop = _brush_prop

    def apply_props(self, painter):
        """
        Перезаписываем применение всех свойств к Painter'у для кисти
        :param painter: класс Painter
        """
        painter.brush_prop = self.brush_prop
