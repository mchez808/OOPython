class C(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return str(self.x) + " ^_^ " + str(self.y)

    def __repr__(self):
        # __repr__ method returns an object representation
        # it makes debugging easier
        return f"{{\"magic\":x={str(self.x)},y={str(self.y)}}}"

if __name__ == "__main__":
    a = C(3, 4)
    print(a.x, a.y)
    b = C(4, 3)
    print(b.x, b.y)

    print(a == b)

    d = C(3, 4)
    print(a == d)

    # these two: same output format
    print(a)
    print(str(b))
    print('=====')

    print(repr(a))
    print(repr(b))
    print(repr(d))
