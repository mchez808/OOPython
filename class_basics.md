source: [Real Python](https://realpython.com/python3-object-oriented-programming/)

Object Oriented Programming is an excellent way to take full advantage of the capabilities Python 3 has to offer.

Let's begin by creating a basic class. A class about dogs.

<img src="./img/dags_pancake.jpg" alt="dogs" width="400" title="Zelda and Leeloo like pancakes!" />

These are my family's dogs. Zelda is the black [Yorkshire Terrier and Miniature Poodle mix](https://dogtime.com/dog-breeds/yorkipoo), and Leeloo is a [West Highland White Terrier](https://en.wikipedia.org/wiki/West_Highland_White_Terrier). They will be pivotal in describing Object Oriented Design... well, maybe.

##### Naming conventions

*Note that the [Python naming convention for classes](https://www.python.org/dev/peps/pep-0008/#class-names) is to write them in CapitalizedWords notation. So a class for Leeloo's specific breed would be written as* `WestHighlandWhiteTerrier`.

Let's give all `Dog` instances the properties of name and age.

If you're using the Atom text editor, here's a [handy tip for building a class](https://github.com/mchez808/OOPython/blob/main/editors_and_interfaces.md) there. (Of course, it's quite hard to beat the PyCharm IDE).

#### Attributes

Instances Attributes belong to class instances, or objects. So a dog born in 2009 can have the name *Zelda* with the age of 11, while another born in 2012 named *Leeloo* can have a separate age of 8. We use instance attributes to keep these separate.

```Py
lee = Dog(name='Leeloo', age=8)
zel = Dog(name='Zelda', age=11)
```

Class Attributes are common to all instances (objects). All dogs belong to the same species. Declare it outside the `.__init__()`, and it's a class attribute.

It's helpful for me to [run Python interactively](https://github.com/mchez808/OOPython/blob/main/editors_and_interfaces.md) on the fly.

#### Instance Methods

**Instance methods** can only be called from a class object. Just like `.__init__()`, the first parameter of an instance method should always be `self`. This is not a reserved keyword, but rather a Python convention that will improve readability.

It is okay to have an instance method `describe()`; it is far better to write the special instance method `__str__()`. Here's why: if I type `print(zel)`, I'll display the memory address, like `<__main__.Dog object at 0x0000024A21FA42B0>`. By using the **dunder method** `__str__()`, Python will know that by typing `print(zel)`, I really want to view a string representation of the object. (Java developers, think of it as the `toString()` method.)

To clarify, the *dunder method* `__str__()` will alter `print(zel)`, but it will not affect the output when typing `zel` into the CLI. The memory address will appear, unless `print()` is used.
