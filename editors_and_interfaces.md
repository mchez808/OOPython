# Atom

Autocomplete in Atom is excellent. Just type `class` (or really just `c`) and the `New class` option appears. Another helpful one is `ifmain` because, honestly, `if __name__ == '__main__':` can be a mouthful to memorize :)

# Python in the Command Line Interface

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
