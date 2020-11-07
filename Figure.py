from PyQt5 import QtWidgets

from Properties import Properties


class Figure(QtWidgets):
    """
    Абстрактный класс всех фигур
    """
    def __init__(self):
        self.prop = Properties()

    def draw_geometry(self, painter):
        pass
