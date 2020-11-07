class Painter:
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def line(self, x1, y1, x2, y2):

        self.parent.scene.addLine(x1, y1, x2, y2, self.parent.pen)

    def rect(self, x1, y1, x2, y2):

        x0 = x1 if x1 < x2 else x2

        y0 = y1 if y1 < y2 else y1

        w = x2 - x1 if x1 < x2 else x1 - x2

        h = y2 - y1 if y1 < y2 else y1 - y2

        self.parent.scene.addRect(x0, y0, w, h, self.parent.pen, self.parent.brush)

    def ellipse(self, x1, y1, x2, y2):
        self.parent.scene.addEllipse(x1, y1, x2-x1, y2-y1, self.parent.pen, self.parent.brush)

    def clear(self):
        self.parent.scene.clear()
