# A combination of multiple inheritance and abstract base classes can be used to implement an interface.
# Python doesn't have explicit language support for this as a built-in part of the language.
# An interface is a contract a particular class is making to provide certain behavior.
from abc import ABC, abstractmethod
from math import pi

class GraphicShape(ABC):
    """
    abstract base class, with @abstractmethod
    """
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass


class Circle(GraphicShape):
    """
    Circle class, inheriting from abstract base class
    """
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return pi * self.radius ** 2