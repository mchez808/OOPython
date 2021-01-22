# Python 3.7 introduces the start of Data Classes
# used mostly to hold information
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    # You can define methods in a dataclass like any other
    def bookinfo(self):
        return f"{self.title}, by {self.author}"


# ==========================================
# Data Classes
# ==========================================
# @dataclass decorator implements __init__
#  to initialize each attribute on the object instance.
#
# note: type hints required for this to work.
#  however, the types are not enforced.
#
# What else Data Classes do:
#   - __eq__ and __repr__ are automatically implemented

# create some instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)
b3 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

# access fields
print(b1.title)
print(b2.author)

# print the book itself - dataclasses implement __repr__
# implementation of the __repr__ function
print(b1)
repr(b1)

# comparing two dataclasses - they implement __eq__
print(b1 == b2)
print(b2 == b3)

# change some fields, call a regular class method
b1.title = "Anna Karenina"
b1.pages = 864
print(b1.bookinfo())