class XYZ:
    def __init__(self):
        self.xyz = 'XYZ'

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

    def __eq__(self, other):
        # must be of same class
        if not isinstance(other, type(self)):
            raise ValueError("Can't compare Node to non-Node type")
        return self.data == other.data

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
    # print(xyz == a)
    print(a == xyz)