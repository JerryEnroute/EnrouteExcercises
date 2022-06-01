from rectangle import Rectangle

class Square(Rectangle):
    
    def __init__(self, _color, _filled, _width, _length):
      super().__init__(_color, _filled, _width, _length)
    
    def getSide(self):
      return self._width

    def setSide(self, side: float):
      self.setWidth(side)
      self.setLength(side)

    def setWidth(self, side: float):
      self._width = self._length = side

    def setLength(self, side: float):
      self._width = self._length = side
    
    def __str__(self):
      return f'square[rectangle[shape[color = {self._color}, filled = {self._filled}, width = {self._width}, length = {self._length}]]]'
