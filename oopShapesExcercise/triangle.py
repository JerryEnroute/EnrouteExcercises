from shape import Shape

class Triangle(Shape):

  def __init__(self, _color, _filled, _sideLength: float = 1.0):
    super().__init__(_color, _filled)
    self._sideLength = _sideLength

  def setSideLength(self, _sideLength: float):
    self._sideLength = _sideLength

  def getArea(self, area: float):
    area = self._sideLength * self._sideLength * 0.5
    return area

  def getPerimeter(self, perimeter: float):
    perimeter = 3 * self._sideLength
    return perimeter

  def __str__(self):
    return f'triangle[shape[color = {self._color}, filled = {self._filled}, sideLength = {self._sideLength}]]'