from Figure import Figure


class Line(Figure):

    def __init__(self, color, th):

        super().__init__()
        self.color = color
        self.thick = th

    def draw_geometry(self, painter):
        painter.line()
