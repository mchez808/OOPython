# Unlike other languages, Python lets you define classes that can inherit from more than one base class. 
# multiple inheritance: while it can be a useful tool, it can also cause a lot of problems if you don't use it carefully.

# For self.name, the Method Resolution Order (MRO) starts in current class, 
# in this case, in class C, which has no definition of name.
# Python then goes to the superclasses of the line (after ~20):
# 
#    C(A, B)        in order, from left to right.
#    
#    D(B, A)        <-- this would alter the MRO.

# this added complexity is one of the main reasons why you don't see a whole lot of multiple inheritance in real world projects, 
# but there is a place where they actually are very useful and that is in implementing a programming construct called an interface.

class A:
    def __init__(self):
        super().__init__()
        self.abc = "abc"
        self.name = "AAA"


class B:
    def __init__(self):
        super().__init__()
        self.xyz = "xyz"
        self.name = "BBB"


# inherit from multiple classes
class C(A, B):  # both A and B defined as base classes
    def __init__(self):
        super().__init__()

    def show_attr(self):
        print(self.abc, self.xyz)

    def show_name(self):
        print(self.name)


class D(B, A):
    def __init__(self):
        super().__init__()

    def show_name(self):
        print(self.name)
    

if __name__ == "__main__":
    c = C()
    c.show_attr()   # non-conflicting attributes print just fine

    c.show_name()   # conflict?  MRO: AAA prints out.

    # new MRO
    d = D()
    d.show_name()

    # print out MRO's
    print(C.__mro__)
    print(D.__mro__)