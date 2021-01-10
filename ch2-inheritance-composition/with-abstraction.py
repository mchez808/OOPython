# Without Using Abstract Base Classes to enforce class constraints

# This is a fairly common design pattern programming:
# you want to provide a base class that defines a template for other classes to inherit from.
# However: 
#   1) You don't want consumers of your base class to be able to create instances of the base class itself. 
#       It's merely intended to be a blueprint, just an idea. You want only subclasses to provide concrete implementations of that idea.
#   2) You want to enforce the constraint that there are certain methods in the base class that subclasses must implement.

# example here: program is flexible, so that new 2D shape classes can be added.

# TODO:
# the scenario here is that we want each shape to inherit from graphic shape. 
# We want to enforce that every shape implements the calcArea function, 
# and we want to prevent the graphic shape class itself from being instantiated on its own

from math import pi

class GraphicShape:
    def __init__(self):
        super().__init__()

    def calcArea(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return pi * self.radius ** 2


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side

    def calcArea(self):
        return self.side ** 2


if __name__ == "__main__":
    g = GraphicShape()

    c = Circle(10)
    print(c.calcArea())
    s = Square(12)
    print(s.calcArea())
