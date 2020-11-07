class Frame:

    def __init__(self, _x1, _y1, _x2, _y2):
        self.x1 = _x1
        self.y1 = _y1
        self.x2 = _x2
        self.y2 = _y2

    _x1, _x2, _y1, _y2 = property()

    @_x1.getter
    def _x1(self):
        return self.x1

    @_x1.setter
    def _x1(self, value):
        self.x1 = value

    @_x2.getter
    def _x2(self):
        return self.x2

    @_x2.setter
    def _x2(self, value):
        self.x2 = value

    @_y2.getter
    def _y2(self):
        return self.y2

    @_y2.setter
    def _y2(self, value):
        self.y2 = value

    @_y1.getter
    def _y1(self):
        return self.y1

    @_y1.setter
    def _y1(self, value):
        self.y1 = value
