class Book(object):
    """
    [from PEP 257] The docstring for a class should summarize its behavior and list the public methods and instance variables. If the class is intended to be subclassed, and has an additional interface for subclasses, this interface should be listed separately (in the docstring). The class constructor should be documented in the docstring for its __init__ method. Individual methods should be documented by their own docstring.
    """
    def __init__(self, title):
        """Inits Book with parameters"""
        self.title = title


if __name__ == "__main__":
    bk1 = Book("Life of Pi")
    bk2 = Book("The Art of War")