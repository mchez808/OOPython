class Dog(object):
    """Dog class to demonstrate OOP Design"""

    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        super(Dog, self).__init__()
        self.name = name
        self.age = age

    # Class instances
    def describe(self):
        return f"{self.name} is {self.age} years old."

    def speak(self, sound):
        return f"{self.name} says {sound}"


if __name__ == '__main__':
    lee = Dog(name='Leeloo', age=8)
    zel = Dog(name='Zelda', age=11)

    print(zel.describe(), lee.describe())
