
class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price


class Book(Publication):
    def __init__(self, title, price, author, pages):
        super(Book, self).__init__(title, price)
        self.author = author
        self.pages = pages


class Magazine(Publication):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher


if __name__ == "__main__":
    b1 = Book("Brave New World", 29.0, "Aldous Huxley", 311)
    print(b1.title, b1.price, b1.author, b1.pages, sep=', ')

    m1 = Magazine("Scientific American", 5.99, "Monthly", "Springer Nature")
    print(m1.title, m1.price, m1.period, m1.publisher, sep=', ')
