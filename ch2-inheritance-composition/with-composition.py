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


class Chapter:
    def __init__(self, name, page_ct):
        self.name = name
        self.page_ct = page_ct


class Book:
    def __init__(self, title, price, author=None):
        self.title = title
        self.price = price
        self.author = author
        self.chapter_list = []

    def addchapter(self, chapter=None):
        self.chapter_list.append(chapter)

    def get_page_ct(self):
        # get sum of chapters: 
            # Chapter : Book.chapter_list
            # Chapter.page_ct
            # Book.chapter_list.page_ct
        summ = 0
        for chap in self.chapter_list:
            summ += chap.page_ct
        return summ

    def __str__(self):
        return f"\"{self.title}\" by {self.author} at ${self.price}"



b1 = Book("War and Peace", 39.0, Author("Leo", "Tolstoy"))

b1.addchapter(Chapter("Chapter 1", 125))
b1.addchapter(Chapter("Chapter 2", 97))
b1.addchapter(Chapter("Chapter 3", 143))

print(b1)
print(b1.get_page_ct(), "pages")