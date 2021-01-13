# composition: "has-a" relationship, to build more complex classes
    # Book has-a price, title, and Author -- which has-a first and last name
    # (by contrast, inheritance: "is-a" relationship)
        # (e.g., magazine is-a periodical, which is-a publication)

class Author:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __str__(self):
        return f"{self.first} {self.last}"


class Book:
    # modify this to take in an Author class argument
    def __init__(self, title, price, author : Author):
        self.title = title
        self.price = price
        self.author = author
        self.chapters = []

    def addchapter(self, name, pages):
        self.chapters.append((name, pages))



b1 = Book("War and Peace", 39.0, Author("Leo", "Tolstoy"))

b1.addchapter("Chapter 1", 125)
b1.addchapter("Chapter 2", 97)
b1.addchapter("Chapter 3", 143)

print(b1.title)
