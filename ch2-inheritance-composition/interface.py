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


# TODO: add another ABC called JSONify
class JSONify(ABC):
    """
    abstract base class, with 1 single @abstractmethod to_json
    """
    @abstractmethod
    def to_json(self):
        pass
    


class Circle(GraphicShape):
    """
    Circle class, inheriting from abstract base class
    """
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return pi * self.radius ** 2


if __name__ == "__main__":
    c = Circle(10)
    print(c.calcArea())

    # TODO: add behavior for JSON-representation of concrete class
    # Why not add it to the GraphicShape ABC (abstract base class)?
    # Because, if we had other concrete child classes and we wanted them all to have the same behavior,
    # we wouldn't want to necessitate the implementation of it in every subclass. (DRY: Don't Repeat Yourself)