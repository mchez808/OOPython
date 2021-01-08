# class methods and attributes
class Book:
    # TODO: properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    # TODO: dunder properties are hidden from other classes

    # TODO: create a class method
    @classmethod
    def get_book_types(cls):
        """Returns the BOOK_TYPES constant.
        operates on a class instance, not an object instance.
        """
        return cls.BOOK_TYPES

    # TODO: create a static method

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def set_title(self, new_title):
        self.title = new_title

    def __init__(self, title, booktype):
        self.title = title
        if booktype.upper() not in Book.BOOK_TYPES:
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype


if __name__ == "__main__":
    b1 = Book("The Giver", "eBook")
    try:
        b2 = Book("The Alchemist", "Post-it notes")
    except ValueError as e:
        print("Expected fail case: success")

    # access the class attribute through class method
    print("Book types:", Book.get_book_types())
