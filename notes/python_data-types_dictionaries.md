# Python Dictionaries

A `dictionary` in Python is an ordered collection of key-value pairs.

## Defining a Dictionary

- A dictionary is defined by enclosing a comma-separated list of key-value pairs in curly braces `{}`
- A colon `:` separates each key from its associated value
- Key-value pairs are separated by commas `,`
- A dictionary's key can be one of the following types:
  - `integer`
  - `float`
  - `string`
  - `boolean`
  - `tuple`
  - `frozenset`

```python
d = {
    <key>: <value>,
    <key>: <value>,
      .
      .
      .
    <key>: <value>
}
```

```python
character = {
    "name": "Aragorn",
    "race": "Human",
    "class": "Ranger",
    "level": 5
    "inventory": ["sword", "potion"]
}
```

You can also construct a dictionary with the built-in `dict()` function.

The argument to `dict()` should be a sequence of key-value pairs. A list of tuples works well for this:

```txt
d = dict([
    (<key>, <value>),
    (<key>, <value),
      .
      .
      .
    (<key>, <value>)
])
```

```python
character = dict([
    ("name", "Aragorn"),
    ("race", "Human"),
    ("class", "Ranger"),
    ("level", 5),
    ("inventory", ["sword", "potion"])
])
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

Can also use the `update()` method to add or update properties of a dictionary with values passed into the `update()` method.

- The `update()` method accepts a dictionary whose key-value pairs are used to update the dictionary invoked by the `update()` method.

```python
# Add a new "spells" property & update the "level" property
character.update({"spells": ["inspire", "rally"], "level": 6})
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

## Checking if a Key or Value Exists

### Checking if a Key Exists

Use `in` and `not in` keywords to check if a key exists (or not)

```python
if <key> in <dictionary>.keys():
    # Do something if the key exists

# You can actually omit the `keys()` method
if <key> in <dictionary>:
    # Do something if the key exists
```

```python
if "weapon" in character.keys():
    print("Weapon is equipped!")

if "weapon" in character:
    print("Weapon is equipped!")

if "birthday" not in character:
    print("You don't have a birthday!")
```

### Checking if a Value Exists

Use `in` and `not in` keywords to check if a value exists (or not)

```python
if <key> in <dictionary>.values():
    # Do something if the value exists
```

```python
if "sword" in character.values():
    print("I have a sword!")
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

[Dictionary Comprehensions](python_comprehensions.md#dictionary-comprehensions)

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

Can also merge the dictionaries in place by using the update operator (`|=`)

```python
dict_d = {'a': 1, 'b': 2}

# Merge the RHS dictionary into the LHS dictionary
dict_d |= {'c': 3, 'd': 4}

print(dict_d) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
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

- [Python Cheatsheet - Dictionaries](https://www.pythoncheatsheet.org/cheatsheet/dictionaries)
- [RealPython - Dictionaries in Python](https://realpython.com/python-dicts/)
- [Real Python - How to Iterate Through a Dictionary in Python](https://realpython.com/iterate-through-dictionary-python/#using-some-of-pythons-built-in-functions)
