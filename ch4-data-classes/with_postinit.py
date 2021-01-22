# @dataclass provides a special function __post_init__ 
#  that you can override
#  to add additional attributes
#  that might depend on the values of the initial attributes.

from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    # TODO: the __post_init__ function lets us customize additional properties
    # after the object has been initialized via built-in __init__
    def __post_init__(self):
        self.description = f"{self.title} by {self.author}, {self.pages} pages"


if __name__ == "__main__":
    # create some Book objects
    b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
    b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

    # TODO: use the description attribute
    print(b1.description)
    print(b1.description)