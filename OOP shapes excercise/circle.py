from shape import Shape

class Circle(Shape):
  def __init__(self, _color, _filled, _radius: float = 1.0):
    super().__init__(_color, _filled)
    self._radius = _radius
    
  def getRadius(self):
    return self._radius
    
  def setRadius(self):
    self._radius
    
  def getArea(self):
    area = self._radius * self._radius * 3.14
    return area
    
  def getPerimeter(self):
    perimeter = 2 * self._radius * 3.14
    return perimeter
    
  def __str__(self):
    return f'circle[shape[color = {self._color}, filled = {self._filled}, radius = {self._radius}]]'