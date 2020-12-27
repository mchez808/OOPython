class Dog(object):
    """Dog class to demonstrate OOP concepts: inheritance"""

    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        super(Dog, self).__init__()
        self.name = name
        self.age = age


if __name__ == '__main__':
    lee = Dog(name='Leeloo', age=8)
    zel = Dog(name='Zelda', age=11)
