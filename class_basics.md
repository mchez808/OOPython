source: [Real Python](https://realpython.com/python3-object-oriented-programming/)

Object Oriented Programming is an excellent way to take full advantage of the capabilities Python 3 has to offer.

Let's begin by creating a basic class.

##### Naming conventions

*Note: Python class names are written in CapitalizedWords notation by convention. For example, a class for a specific breed of dog like the Jack Russell Terrier would be written as JackRussellTerrier.*

some properties that all `Dog` objects should have: name, age

Autocomplete in Atom is excellent. Just type `class` (or really just `c`) and the `New class` option appears.

If you're using the Atom text editor, here's a [handy tip for building a class](https://github.com/mchez808/OOPython/blob/main/editors_and_interfaces.md) there. (Of course, it's quite hard to beat the PyCharm IDE).

#### Attributes

Instances Attributes belong to class instances, or objects. So a dog born in 2009 can have the name *Zelda* with the age of 11, while another born in 2012 named *Leeloo* can have a separate age of 8. We use instance attributes to keep these separate.

```Py
lee = Dog(name='Leeloo', age=8)
zel = Dog(name='Zelda', age=11)
```

Class Attributes are common to all instances (objects). All dogs belong to the same species. Declare it outside the `.__init__()`, and it's a class attribute.

Let's run Python interactively in the *Bash* command line, using the `-i` option, to view this. Go to the same directory. (Not Windows -- all bets are off with Windows!)

```
cd animals
python -i dogs.py
```

```Py
>>> zel.name
'Zelda'
>>> lee.age
8
>>> zel.species
'Canis familiaris'
```

A handy Python command for clearing the CLI when running Python there

```Py
from os import system
def cls():
    system('cls')
```
