
class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price


class Book(Publication):
    def __init__(self, author, pages, title, print):
        super(Book, self).__init__(title, print)
        self.author = author
        self.pages = pages


if __name__ == "__main__":
    b1 = Book("Brave New World", "Aldous Huxley", 311, 29.0)

    print(b1.author)
