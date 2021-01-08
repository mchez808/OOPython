# class methods and attributes
class Book:
    # TODO: properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    # TODO: dunder properties are hidden from other classes

    # TODO: create a class method

    # TODO: create a static method

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def set_title(self, new_title):
        self.title = new_title

    def __init__(self, title, booktype):
        self.title = title
        if booktype.upper() not in Book.BOOK_TYPES:
            raise TypeError
        self.booktype = booktype


if __name__ == "__main__":
    b1 = Book("The Giver", "eBook")
    b2 = Book("The Alchemist", "Post-it notes")
