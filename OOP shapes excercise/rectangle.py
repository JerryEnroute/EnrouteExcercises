from shape import Shape

class Rectangle(Shape):

  def __init__(self, _color, _filled, _width: float = 1.0, _length: float = 1.0):
    super().__init__(_color, _filled)
    self._width = _width
    self._length = _length

  def getWidth(self):
    return self._width

  def setWidth(self):
    self._width

  def getLength(self):
    return self._length

  def setLength(self):
    self._length

  def getArea(self):
    area = self._width * self._length
    return area
  
  def getPerimeter(self):
    perimeter = 2 * (self._width + self._length)
    return perimeter

  def __str__(self):
    return f'rectangle[shape[color = {self._color}, filled = {self._filled}, width = {self._width}, length = {self._length}]]'