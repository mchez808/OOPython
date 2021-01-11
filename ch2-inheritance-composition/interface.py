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


# Interfaces are really useful for declaring that a class has a capability that it knows how to provide. 
# interface class
class JSONify(ABC):
    """
    abstract base class, serving the function of an interface
    """
    @abstractmethod
    def to_json(self):
        pass


# Python is flexible enough to be able to implement an interface with abstract base classes and multiple inheritance.
class Circle(GraphicShape, JSONify):
    """
    Circle class, performing multiple inheritance from abstract base classes
    """
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return pi * self.radius ** 2

    def to_json(self):
        return f"{{\"circle\" : {str(self.calcArea())} }}"


if __name__ == "__main__":
    c = Circle(10)
    print(c.calcArea())

    # TODO: add behavior for JSON-representation of concrete class
    # Why not add it to the GraphicShape ABC (abstract base class)?
    # Because, if we had other concrete child classes and we wanted them all to have the same behavior,
    # we wouldn't want to necessitate the implementation of it in every subclass. (DRY: Don't Repeat Yourself)
    print(c.to_json())