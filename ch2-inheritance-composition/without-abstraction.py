# Without Using Abstract Base Classes to enforce class constraints

# This is a fairly common design pattern programming:
# you want to provide a base class that defines a template for other classes to inherit from.
# However: 
#   1) You don't want consumers of your base class to be able to create instances of the base class itself. 
#       It's merely intended to be a blueprint, just an idea. You want only subclasses to provide concrete implementations of that idea.
#   2) You want to enforce the constraint that there are certain methods in the base class that subclasses must implement.


class GraphicShape:
    def __init__(self):
        super().__init__()

    def calcArea(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side

if __name__ == "__main__":
    g = GraphicShape()

    c = Circle(10)
    print(c.calcArea())
    s = Square(12)
    print(s.calcArea())
