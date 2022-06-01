from abc import ABC, abstractmethod

class Shape(ABC):

    def __init__(self, _color: str = 'red', _filled: bool = True):
      self._color = _color
      self._filled = _filled
        
    def getColor(self) -> str:
      return self._color

    def setColor(self, color: str):
      self._color = color

    def isFilled(self) -> bool:
      return self._filled

    def setFilled(self, filled: bool):
      self._filled = filled

    @abstractmethod
    def getArea(self, area: float):
      pass

    @abstractmethod
    def getPerimeter(self, perimeter: float):
      pass

    def __str__(self) -> str:
      f'Shape[color = {self._color}, filled = {self._filled}]'