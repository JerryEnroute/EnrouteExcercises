from shape import Shape

class Rectangle(Shape):

  def __init__(self, _color: str, _filled: bool, _width: float = 1.0, _length: float = 1.0):
    super().__init__(_color, _filled)
    self._width = _width
    self._length = _length

  def getWidth(self) -> float:
    return self._width

  def setWidth(self, width: float):
    self._width = width

  def getLength(self) -> float:
    return self._length

  def setLength(self, length: float):
    self._length = length

  def getArea(self) -> float:
    area = self._width * self._length
    return area
  
  def getPerimeter(self) -> float:
    perimeter = 2 * (self._width + self._length)
    return perimeter

  def __str__(self) -> str:
    return f'Rectangle[Shape[color = {self._color}, filled = {self._filled}, width = {self._width}, length = {self._length}]]'

print(Rectangle('red', True, 2.0, 3.0))