class XYZ:
    def __init__(self):
        self.xyz = 'XYZ'

    def __eq__(self, other):
        # must be of same class
        if not isinstance(other, type(self)):
            raise ValueError("Can't compare Node to non-Node type")
        return self.xyz == other.xyz


err = "Can't compare Node to non-Node type"

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

    def __eq__(self, other):
        # must be of same class
        if not isinstance(other, Node):
            raise ValueError(err)

        return (self.data == other.data) and (self.next == other.next)

    # greater than
    def __gt__(self, other):
        if not isinstance(other, Node):
            raise ValueError(err)
        return self.data > other.data

    # greater than or equal to
    def __ge__(self, other):
        if not isinstance(other, Node):
            raise ValueError(err)
        return self.data >= other.data

    # less than
    def __lt__(self, other):
        if not isinstance(other, Node):
            raise ValueError(err)
        return self.data < other.data

    # less than or equal to
    def __le__(self, other):
        if not isinstance(other, Node):
            raise ValueError(err)
        return self.data <= other.data


# TODO
# class LinkedList:
#     def __init__(self, node=None):
#         self.head = node
#         self.length = 0 if node is None else 1


if __name__ == "__main__":
    c = Node('c')
    c2 = Node('c')
    print(c == c2)

    b = Node('b', c)
    print(c == b)

    a = Node('a', b)
    print(a, end=' '); print(b, end=' '); print(c)

    xyz = XYZ()
    xyz2 = XYZ()
    print(xyz == xyz2)
    try:
        print(a == xyz)  # same as: >>> print(xyz == a)
    except ValueError as e:
        print("An error was expected; an error has occurred.")
    
    print("node equality:")
    a2 = Node('a', b)
    print(a == a2)

    print("comparisons")
    print(a > b, end=', '); print(b > a)
    print(a >= b, end=', '); print(b >= a)
    print(a < b, end=', '); print(b < a)
    print(a <= b, end=', '); print(b <= a)
