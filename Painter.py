from Figures.Ellipse import Ellipse
from Figures.Rectangle import Rectangle


class Painter:
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def line(self, pen, x1, y1, x2, y2):
        # ToDo: Сделать линию отдельным обьектом Figure, как с Rectangle и Ellipse
        self.parent.scene.addLine(x1, y1, x2, y2, pen)

    def rect(self, pen, brush, x1, y1, x2, y2):
        rect = Rectangle(pen, brush, x1, y1, x2, y2)
        self.parent.scene.addItem(rect)

    def ellipse(self, pen, brush, x1, y1, x2, y2):
        ellipse = Ellipse(pen, brush, x1, y1, x2, y2)
        self.parent.scene.addItem(ellipse)

    def clear(self):
        self.parent.scene.clear()
