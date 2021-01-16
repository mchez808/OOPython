# class methods and attributes
class Book:
    # TODO: properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    # TODO: dunder properties are hidden from other classes
    __booklist = None   # essentially a private variable

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

    # TODO: create a class method
    @classmethod
    def get_book_types(cls):
        """Returns the BOOK_TYPES constant.
        operates on a class instance, not an object instance.
        """
        return cls.BOOK_TYPES

    # TODO: create a static method
    @staticmethod
    def get_book_list(cls):
        if Book.__booklist is None:
            Book.__booklist = []
        return Book.__booklist

    # by definition, it neither modifies the state of the class nor of objects
    # useful when it makes sense for the method to belong to the class,
    # i.e. good way of namespacing certain kinds of methods.


if __name__ == "__main__":
    b1 = Book("The Giver", "eBook")
    try:
        b2 = Book("The Alchemist", "Post-it notes")
    except ValueError as e:
        print("Expected fail case: success")
        b2 = Book("The Alchemist", "paperback")

    # access the class attribute through class method
    print("Book types:", Book.get_book_types())

    # use the static method to access a singleton object
    books = Book.get_book_list(Book)
    books.append(b1)
    books.append(b2)
    print(books)