# Python Modules and Packages

Each file in Python can be considered a `module`

## Quick Syntax Summary

```python
# Import a package
import <package> [ as <alias-name> ]

# Import a module
import <module> [ as <alias-name> ]

# Import module, subpackage, or object from a package
# X, X, Z, etc. can be a module, sub-package or object
#  from the imported package
from <package> import <X [, Y, Z, ...]> [ as <alias-name> ]

# Import an object from a module
from <module> import <object_a [, object_b, object_c, ...]>
```

## Package vs Module

What is a `module`?

- A `module` is any `*.py` file.
- The name of the module is the name of the file.

What is a `package`?

- A `package` is any folder containing a file named `__init__.py` file inside of it.
- **NOTE:** In Python 3.3+, any folder (even without a `__init__.py` file) is considered a package.
- The name of the package is the name of the folder.

What is a `built-in module`?

- A `built-in module` is a "module" (written in C) that is compiled into the Python interpreter, and therefore does not have a `*.py` file

## import Keyword

The `import` keyword

- When a `module` is imported, Python runs all of the code in the module file.
- When a `package` is imported, Python runs all of the code in the package's `__init__.py` file, if such a file exists.
- All of the objects defined in the `module` or the `package's` `__init__.py` file are made available to the importer.

**CAUTION:** Avoid running code from imported modules

- Often, we want to ensure that we only run code if the code is executed (and not imported). To ensure this, use the following logic:

```python
# script.py
if __name__ == '__main__':
    # Run this logic only if
    # the containing module is executed
    # (via "python script.py")
```

## `__init__.py`

An `__init__.py` file has 2 functions:

- Convert a folder of scripts into an importable package of modules (before Python 3.3)
- Run package initialization code

**NOTE:** Don't need `__init__.py` anymore

- As of Python 3.3+, all folders are considered packages so it is no longer necessary to put `__init__.py` into your folder structure.

### Running Package Initialization Code

- The first time a package or one of its modules is imported, Python will execute the `__init__.py` file in the root folder of the package if the file exists.
- All objects and functions defined in `__init__.py` are considered part of the package namespace.

## Absolute vs. Relative Import

What is an `absolute import`?

- An `absolute import` uses the full path (starting from the project’s root folder) to the desired module to import.

What is a `relative import`?

- A `relative import` uses the relative path (starting from the path of the current module) to the desired module to import.

Best Practice - Use `absolute import`

- It is best practice to use absolute imports

Add the module absolute path as a comment to your file

- It is a good practice to add the absolute path to each module as a comment in the module file.

## Importing Modules (Files)

To import a module into a Python file, use the `import` keyword and then pass in the name of the module (the name of the file)

In the below example, `main.py` imports a module called `utility.py`. These files are located in the same directory.

```python
# main.py

# Import the utility module
import utility

# Run the imported functions from the utility module
divided = utility.divide(5, 10)
print(divided)  # 0.5

multiplied = utility.multiply(5, 10)
print(multiplied)  # 50
```

```python
# utility.py

def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2
```

**CAUTION:** Importing from same file path

- The example above assumes that the imported `utility.py` module is in the same directory path as the file which is importing it (`main.py`)
- Refer to the notes on `packages` to import modules from other directories (`packages`)

### Importing modules with aliased names

You can use the `as` keyword to alias the name of an imported module. You can then reference the module in your code with the aliased name instead of the module name.

```python
# main.py

# Import the utility module and reference it in the code with the "util" alias
import utility as util

# Run the imported functions from the utility module
divided = util.divide(5, 10)
print(divided)  # 0.5

multiplied = util.multiply(5, 10)
print(multiplied)  # 50
```

### Importing specific items from a module

We can use the `from..import` syntax to import specific items from a module

> `from <module> import <item1>, <item2>, ...`

```python
# Use from..import to import specific items from utility module
# In this case, import the "add" and "subtract" functions
from utility import add, subtract

# Run the imported functions from the utility module
# NOTE: Since we only imported add and subtract in this case
#       we don't have access to the other functions
added = add(1, 2)
print(added)  # 3

subtracted = subtract(1, 2)
print(subtracted)  # -1
```

### `__pycache__` directory

When you execute a file which uses imports, Python will cache a compiled version of the imported module in a directory called `__pycache__`
As long as nothing changes in the imported module by the time the importing code is executed again, the cached file in `__pychache__` is used instead for quicker executions.

`__pychache__` is automatically created if it does not exist.

## Python Packages

A `package` in Python is a directory containing Python `modules`.

A `package` can have one or more `modules` (files) inside of it.

### Importing modules from a Python Package

When importing a `module` from a `package`, use dot notation to drill down from one directory / `package` to another until you get to the desired `module` you wish to import.

File Structure for example below:

- `main.py`
- `utility.py`
- `shopping` (directory / package)
  - `__init__.py`
  - `shopping_cart.py`

```python
# Import the utility module and reference it in the code with the "util" alias
import utility as util
import shopping.shopping_cart as cart  # Import the shopping_cart module from the shopping package

# Run the imported functions from the utility module
divided = util.divide(5, 10)
print(divided)  # 0.5

multiplied = util.multiply(5, 10)
print(multiplied)  # 50

# Run the imported functions from the shopping_cart module in the shopping package
my_cart = cart.buy("apple")
print(my_cart)  # ['apple']
```

## `__name__` & `__main__`

When a `module` is read in by Python it is given a name which matches up to the file name.

This name of the module can be accessed within the module by accessing the `__name__` keyword

**NOTE:** `__name__` for the executed module is always `__main__`

- The module which is executed by the Python interpreter is always given the `__name__` of `__main__`

**NOTE:** `main.py`

- It is standard practice to have a `main.py` file as the root entry point of your project.
- `main.py` is responsible for importing all modules / packages and executing the main project code.

We often want to ensure that we only run code if the code is executed (and not imported). To ensure this, use the following logic:

```python
# script.py

if __name__ == '__main__':
    # Your logic here
    # Only run code here if the containing module is executed
    # via "python script.py"
```

```python
# main.py

# Import the utility module and reference it in the code with the "util" alias
import utility as util
from utility import add, subtract
import shopping.shopping_cart as cart  # Import the shopping_cart module from the shopping package

# Only run this code if the module is executed
#  (and not imported)
# This is common practice for main.py
if __name__ == "__main__":
    # Run the imported functions from the utility module
    divided = util.divide(5, 10)
    print(divided)  # 0.5

    multiplied = util.multiply(5, 10)
    print(multiplied)  # 50

    added = add(1, 2)
    print(added)  # 3

    subtracted = subtract(1, 2)
    print(subtracted)  # -1

    # Run the imported functions from the shopping_cart module in the shopping package
    my_cart = cart.buy("apple")
    print(my_cart)  # ['apple']
```

## Python's Built-In Modules

All Python Built-In Modules can be found under the [Python Module Index](https://docs.python.org/3/py-modindex.html)
Think of the `Python Module Index` as Python's Standard Library.

### Useful Modules -- collections

```python
from collections import Counter, defaultdict

"""
The collections library contains many useful modules including:
- Counter
- defaultdict

Counter can accept an iterable and return a counter object
which will contain the number of times each value in the iterable appears
"""

li = [1, 2, 2, 3, 4, 5, 5, 6, 7]
li_counter = Counter(li)
print(li_counter)  # Counter({2: 2, 5: 2, 1: 1, 3: 1, 4: 1, 6: 1, 7: 1})

sentence = "blah blah blah thinking about python"
sentence_counter = Counter(sentence)
print(
    sentence_counter
)  # Counter({'h': 5, ' ': 5, 'b': 4, 'a': 4, 'l': 3, 't': 3, 'n': 3, 'i': 2, 'o': 2, 'k': 1, 'g': 1, 'u': 1, 'p': 1, 'y': 1})

"""
When accessing a non-existent key in a Python dictionary, you will get a KeyError
Using defaultdict returns a default value if trying to access a value which does not exist
"""
dictionary = {"a": 1, "b": 2}
print(dictionary["c"])  # Throws a KeyError since "c" does not exist as a key

default_dict = defaultdict(lambda: "does not exist", {"a": 1, "b": 2})
print(default_dict["c"])  # "does not exist"
```

## 3rd Party Python Libraries w/ Python Package Index (pypi)

https://pypi.org/

`pypi` is an open-source 3rd party python package repository. It equivalent to `npm` in JavaScript.

### How to install packages from pypi

In order to install packages from `pypi`, you have to use `pip`

`pip install <pypi package name>`

**CAUTION:** Using `pip install` installs packages globally by default!

- When using `pip install` installs packages globally by default. In order to install packages locally, you have to also use `virtual environments`

### List out all packages installed by pip

```bash
pip freeze
```

### Export & Install Multiple Python Packages w/ requirements.txt

`requirements.txt` contains a list of all python packages installed in the current python environment.

Python's `requirements.txt` is analogous to `package.json` in JavaScript

**NOTE:** Use Virtual Environments when managing python packages

- Create a `requirements.txt` file
- Use `pip freeze` to generate the list of packages and store in a `requirements.txt` file.

```bash
pip freeze > requirements.txt
```

You will need to re-run this command whenever you add or remove a package

Use the following command to install all dependencies from `requirements.txt` file

```bash
pip install -r requirements.txt
```

## Virtual Environments

[python virtual environments](python_virtual-environments.md)

## References

- [Python Docs - Python Built-in Modules](https://docs.python.org/3/py-modindex.html)
- [Python Package Index (PyPi)](https://pypi.org/)
- [How to install pip](https://www.makeuseof.com/tag/install-pip-for-python/)
- [Real Python - Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/)
- [The Definitive Guide to Python import Statements](https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html)
- [NerualNine - Importing Your Own Python Modules Properly](https://www.youtube.com/watch?v=GxCXiSkm6no)
