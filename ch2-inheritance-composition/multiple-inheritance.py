# Unlike other languages, Python lets you define classes that can inherit from more than one base class. 
# multiple inheritance: while it can be a useful tool, it can also cause a lot of problems if you don't use it carefully.

class A:
    def __init__(self):
        super().__init__()
        self.abc = "abc"


class B:
    def __init__(self):
        super().__init__()
        self.xyz = "xyz"


# inherit from multiple classes
class C(A, B):  # both A and B defined as base classes
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    c = C()
