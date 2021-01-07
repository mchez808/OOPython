class Book(object):
    """
    [from PEP 257] The docstring for a class should summarize its behavior and list the public methods and instance variables. If the class is intended to be subclassed, and has an additional interface for subclasses, this interface should be listed separately (in the docstring). The class constructor should be documented in the docstring for its __init__ method. Individual methods should be documented by their own docstring.
    """
    def __init__(self, title, author, pages, price):
        """Inits Book with parameters"""
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
    
    
if __name__ == "__main__":
    bk1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
    bk2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)