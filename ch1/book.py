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
        self.__secret = "SECRET ATTRIBUTE"
    
    def get_price(self):
        """return price of book. instance method (not class method)"""
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price
    
    def set_discount(self, amount):
        """modifies discount on book object. (A mutator)"""
        self._discount = amount
        # note: _discount underscore serves as hint to devs that this attribute is internal to the class
        # and should not be accessed from outside the class's logic
        # note: Python doesn't formally enforce this encapsulation.

    
if __name__ == "__main__":
    b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
    b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)
    
    print(b1.get_price())
    b2.set_discount(0.10)
    print(b2.get_price())

    # note: dunder properties are hidden by the interpreter
    try:
        print(b1.__secret)
    except AttributeError as e:
        print("note: successful demonstration of dunder attribute.")
    # The error is because that property can't be seen outside the class. 

    
    # However, this is not a perfect mechanism. So the way that Python does this is by prefixing the name of the attribute with the class name. This is called name mangling. 
    # The reason for this feature is to prevent sub classes, which we'll learn about later, from inadvertently overriding the attribute, 
    # but other classes can subvert this simply by using the class name. So if I go back to the code and just simply put _book in front of this... 
    print(b1._Book__secret)
    # It says now this is a secret attribute. You can see now that I can access the property. So it's not a perfect solution.
    # Nevertheless, you can use this approach to make sure that subclasses don't use the same name for an attribute that you've already used. Now in some cases that's exactly what you want. You do want subclasses to overwrite things sometimes. But if you need to make sure that they don't, then the double underscore can prevent that.
    