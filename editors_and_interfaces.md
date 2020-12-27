# Atom

Autocomplete in Atom is excellent. Just type `class` (or really just `c`) and the `New class` option appears.

Another helpful one is `ifmain` because, honestly, `if __name__ == '__main__':` can be a mouthful to memorize :) What does `__main__` do? In this case, it sits in a Python class module (a file). Thus it executes when the module is run directly. However, if I import the module (`from dog import Dog`), then the `__main__` function does not execute.

# Python in the Command Line Interface

Let's run Python interactively in the *Bash* command line, using the `-i` option, to view this. Go to the same directory. (Not Windows -- all bets are off with Windows!)

```
cd animals
python -i dog.py
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

>>> cls()

# clears Bash CLI
```
