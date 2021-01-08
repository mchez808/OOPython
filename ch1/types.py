class Book(object):
    def __init__(self, title):
        self.title = title


class Film(object):
    def __init__(self, title):
        self.title = title


if __name__ == "__main__":
    b1 = Book("Life of Pi")
    f1 = Film("Life of Pi")

    print(type(b1))
    print(type(f1))

    print(type(b1) == type(f1))

    print("2nd book", end="... ")
    b2 = Book("Life of Pi")
    print("types equal?", type(b1) == type(b2))
    print("is equal?", b1 is b2)
    # print("values equal?", b1 == b2)  # not correctly implemented yet
