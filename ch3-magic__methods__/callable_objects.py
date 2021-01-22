class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    def __call__(self, title, author, price):
        # The __call__ method can be used to call the object like a function
        # This method will be invoked when I call my object. So it gets a copy of the object
        self.title = title
        self.author = author
        self.price = price
    # HOW THIS IS HELPFUL:
    #  that's one of the benefits of this technique is if you have objects whose attributes change frequently, 
    # or are often modified together, this can result in more compact code that's also easier to read.


if __name__ == "__main__":    
    b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
    b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

    # call the object as if it were a function
    # to change the values of the object's attributes
    print(b1)
    b1("Anna Karenina", "Leo Tolstoy", 49.95)       # <------- CALLABLE OBJECT example
    print(b1)
