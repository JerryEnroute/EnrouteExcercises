from abc import ABC, abstractmethod

class Shape(ABC):

    def __init__(self, _color: str = 'red', _filled: bool = True):
      self._color = _color
      self._filled = _filled
        
    def getColor(self):
      return self._color

    def setColor(self):
      self._color

    def isFilled(self):
      return self._filled

    def setFilled(self):
      self._filled

    @abstractmethod
    def getArea(self, area: float):
      pass

    @abstractmethod
    def getPerimeter(self, perimeter: float):
      pass

    def __str__(self):
        f'shape[color = {self._color}, filled = {self._filled}]'