from shape import Shape

class Circle(Shape):
  def __init__(self, _color: str, _filled: bool, _radius: float = 1.0):
    super().__init__(_color, _filled)
    self._radius = _radius
    
  def getRadius(self) -> float:
    return self._radius
    
  def setRadius(self) -> float:
    self._radius
    
  def getArea(self) -> float:
    area = self._radius * self._radius * 3.14
    return area
    
  def getPerimeter(self) -> float:
    perimeter = 2 * self._radius * 3.14
    return perimeter
    
  def __str__(self) -> str:
    return f'Circle[Shape[color = {self._color}, filled = {self._filled}, radius = {self._radius}]]'

print(Circle('red', True, 2.0))