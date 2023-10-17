# Python Dictionaries

A `dictionary` in Python is an unordered collection of key-value pairs.

## Defining a Dictionary

- A dictionary is defined by enclosing a comma-separated list of key-value pairs in curly braces `{}`
- A colon `:` separates each key from its associated value
- Key-value pairs are separated by commas `,`
- A dictionary's key can be one of the following types:
  - `int`
  - `float`
  - `boolean`
  - `string`
  - `tuple`
  - `frozenset`

```python
character = {
    "name": "Aragorn",
    "race": "Human",
    "class": "Ranger",
    "level": 5
}

print(character)  # Outputs: {'name': 'Aragorn', 'race': 'Human', 'class': 'Ranger', 'level': 5}
```

## Accessing Dictionary Values

### Accessing Value for Specific Key

Use bracket notation to access the value associated with a specific key

```python
my_dict[<value>]
```

```python
value = character["race"]
print(value)  # Outputs: 'Human'
```

### Retrieve Value for Specific Key or Return Default Value

- Use the `get()` method to retrieve a value for a specific key.
- If the key is not found, return `None`
- Alternatively, specify a default value to return if the key does not exist

```python
# returns `None` if key is not found
my_dict.get(<key>)

# OR

# Return default value if key is not found
my_dict.get(<key>, <default_value>)
```

```python
value = character.get("alignment", "Neutral")
print(value)  # Neutral
```

## Add New / Modify Existing Key-Value Pairs

You can also use bracket notation to add a new key-value pair, or modify an existing key-value pair

```python
# Add a new key-value pair to the character dictionary
character["background"] = "Isildur's Heir"

# Update value of existing key-value pair
character["level"] = 6
```

## Removing Key-Value Pairs

### del Keyword

Use the `del` keyword to remove a key and its corresponding value from a dictionary

```python
del my_dict[<key_to_remove>]
```

```python
del character["background"]  # Removes key-value pair
```

### Popping Off a Key-Value Pair

- Use the `pop()` method to remove a key from a dictionary, if it is present, return its value
- If the key does not exist, a `KeyError exception` is raised
- By specifying a default value to return, if the key does not exist, an error is not raised, and the default value is returned

```python
my_dict.pop(<key>[, <default>])
```

```python
d = {'a',: 10, 'b': 20, 'c': 30}

value = d.pop('z', -1)

print(value)  # -1
```

### Removing Last Key-Value Pair Added to a Dictionary

- Use the `popitem()` method to remove the last key-value pair added to a dictionary
- Returns the key-value pair as a tuple
- **CAUTION**: If `popitem()` is invoked on an empty dictionary, a `KeyError` exception is raised

```python
my_dict.popitem()
```

```python
d = {'a': 10, 'b': 20, 'c': 30}

t1 = d.popitem()
print(t1)  # ('c', 30)

t2 = d.popitem()
print(t2)  # ('b', 20)

print(d)  # ('a', 10)
```

## Checking if a Key Exists

```python
if <key> in <dictionary>:
    # Do something if the key exists
```

```python
if "weapon" in character:
    print("Weapon is equipped!")
```

## Iterate over Keys & Values of a Dictionary

Use the following methods to [loop](python_loops.md#iterate-over-dictionaries) through data in a dictionary:

- `keys()`: Returns a list of dictionary keys
- `values()`: Returns a list of dictionary values
- `items()`: Returns a list of tuples containing the dictionary key-value pairs

```python
# Keys
for key in my_dict:
    print(key, my_dict[key])

# Values
for val in my_dict.values():
    print(val)

# Key-Value Pairs
for key, val in my_dict.items():
    print(key, val)
```

## Empty / Clear Data in a Dictionary

Use the `clear()` method to clear the contents of a dictionary

```python
my_dictionary.clear()
print(my_dictionary)  # {}
```

## Dictionary Comprehensions

Dictionary comprehension is a concise way to create dictionaries using a single line of Python code.

```python
my_dict = {key_expr: value_expr for item in iterable}
```

```python
# Create a dictionary where keys are numbers between 1 and 5
# values are squares of their respective keys
squared = {x: x**2 for x in range(1, 6)}

print(squared)  # Outputs: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

```python
# Conditional Dictionary Comprehension
# Create a dictionary with numbers between 1 and 5 as keys
# but only if the number is even
squared_even = {x: x**2 for x in range(1, 6) if x % 2 == 0}

print(squared_even)  # Outputs: {2: 4, 4: 16}
```

```python
# Using Two Iterables
# Use the zip() function to iterate over two iterables in parallel
# Enabling you to create a dictionary from two separate lists
characters = ["Frodo", "Gandalf", "Legolas"]
roles = ["Hobbit", "Wizard", "Elf"]

character_roles = {character: role for character, role in zip(characters, roles)}

print(character_roles)  # Outputs: {'Frodo': 'Hobbit', 'Gandalf': 'Wizard', 'Legolas': 'Elf'}
```

```python
# Nested Dictionary Comprehension
# Can also nest dictionary comprehensions
matrix = {(i, j): i*j for i in range(3) for j in range(3)}

print(matrix)
# Outputs: {(0, 0): 0, (0, 1): 0, (0, 2): 0, (1, 0): 0, (1, 1): 1, (1, 2): 2, (2, 0): 0, (2, 1): 2, (2, 2): 4}
```

## Merging Dictionaries

### Merging using the update() method

- Use the `update()` method to accept another dictionary and update the calling dictionary with entries from the provided dictionary.
- If the keys in the dictionary being updated already exist in the calling dictionary, their values get overwritten

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

dict1.update(dict2)
print(dict1)  # Outputs: {'a': 1, 'b': 3, 'c': 4}
```

### Merging using Unpacking Operator

- Use `**` to unpack the key-value pairs of a dictionary and then combine them together
- In the case of overlapping keys, the key-value pairs from the 2nd dictionary will overwrite those from the 1st

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

merged_dict = {**dict1, **dict2}

print(merged_dict)  # Outputs: {'a': 1, 'b': 3, 'c': 4}
```

### Merging using the Merge Operator

The merge operator `|` can be also used to merge two dictionaries together

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

merged_dict = dict1 | dict2
print(merged_dict)  # Outputs: {'a': 1, 'b': 3, 'c': 4}
```

## Nested Dictionaries

```python
party = {
    "Mage": {"name": "Gandalf", "race": "Maia", "level": 10},
    "Thief": {"name": "Bilbo", "race": "Hobbit", "level": 4}
}

print(party["Mage"]["name"])  # Outputs: 'Gandalf'
```

## Resources / References

- [RealPython - Dictionaries in Python](https://realpython.com/python-dicts/)
