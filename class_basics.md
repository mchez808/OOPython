source: [Real Python](https://realpython.com/python3-object-oriented-programming/)

Object Oriented Programming is an excellent way to take full advantage of the capabilities Python 3 has to offer.

Let's begin by creating a basic class. A class about dogs.

<!-- insert pic here -->
<!-- ![dogs](./img/dags_pancake.jpg "Zelda and Leeloo like pancakes!") -->
<img src="./img/dags_pancake.jpg" alt="dogs" width="400"/>

##### Naming conventions

*Note that the [Python naming convention for classes](https://www.python.org/dev/peps/pep-0008/#class-names) is to write them in CapitalizedWords notation. So a class for Leeloo's specific breed would be written as* `[WestHighlandWhiteTerrier](https://en.wikipedia.org/wiki/West_Highland_White_Terrier)`.

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
