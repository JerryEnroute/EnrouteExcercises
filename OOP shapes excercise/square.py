from rectangle import Rectangle

class Square(Rectangle):
    
    def __init__(self, _color: str, _filled: bool, side: float):
      super().__init__(_color, _filled)
      self._width = self._length = side
    
    def getSide(self) -> float:
      return self._width

    def setSide(self, side: float):
      self.setWidth(side)
      self.setLength(side)

    def setWidth(self, side: float):
      self._width = self._length = side

    def setLength(self, side: float):
      self._width = self._length = side
    
    def __str__(self) -> str:
      return f'Square[Rectangle[Shape[color = {self._color}, filled = {self._filled}, width = {self._width}, length = {self._length}]]]'

print(Square('red', True, 2.0))