from dataclasses import dataclass
from dataclasses import field  # more flexibility provided
import random


# used for field(default_factory=price_func)
def price_func():
    return float(random.randrange(20, 40))


@dataclass
class Book:
    # you can define default values when attributes are declared
    title: str  # attributes without default values must come first
    author: str = "nemo"
    pages: int = field(default=0)
    price: float = field(default_factory=price_func)


if __name__ == "__main__":
    b1 = Book("The Cat in the Hat", "Dr Seuss", 23)
    b2 = Book("Green Eggs and Ham", "Dr Seuss", 27)
    print(b1)
    print(b2)
