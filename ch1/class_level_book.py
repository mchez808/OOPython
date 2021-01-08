# class methods and attributes
class Book:
    # TODO: properties defined at the class level are shared by all instances

    # TODO: dunder properties are hidden from other classes

    # TODO: create a class method

    # TODO: create a static method

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def set_title(self, new_title):
        self.title = new_title

    def __init__(self, title):
        self.title = title
    
    