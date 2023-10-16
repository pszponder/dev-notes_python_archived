# Python Data Types

## Numbers

```python
# Integers
x0 = -10
x1 = 0
x2 = 10

# Floating-Point Numbers
y0 = -3.14
y1 = 0
y2 = 3.14
```

## Strings

```python
# Can use either single or double quotes when creating strings
single = 'hello'
double = "world"
```

## Booleans

```python
is_true = True
is_false = False
```

## Lists

[`Lists`](python_data-types_lists.md) are an ordered collection of items which can be of any type and are _mutable_.

```python
fruits = ["apple", "banana", "cherry"]
```

## Tuples

`Tuples` are ordered collections of items, which can be of any type but are _immutable_.

```python
coordinates = (4.0, 5.0)
```

## Sets

`Sets` are an _unordered_ collection of _unique_ items

```python
# Any duplicate numbers passed into the set are removed
unique_numbers = {1, 2, 2, 3, 3, 3}

print(unique_numbers)  # {1, 2, 3}
```

## Dictionaries

`Dictionaries` are _unordered_ collections of key-value pairs

```python
person = {"name": "John", "age": 30}
```

## None

`None` represents the absence of a value or a null value

```python
x = None
```

## Mutable vs Immutable Types

**NOTE:**

- All data types in Python are objects.
- When you create a variable in Python, you're creating a reference to an object
- All variables in Python store references to object
- The key distinction to remember is whether the object being referenced is mutable or immutable

### Immutable

`Immutable` types in Python are types which after being created, cannot be modified.

- `int`
- `float`
- `str`
- `tuple`
- `frozenset`

When you "change" an immutable object, you're actually creating a new object with the new value and changing the reference to point to this new object

```python
x = "hello"
print(id(x))  # This gives the memory address of the object x references

x = "world"
print(id(x))  # This will typically be a different address because
              # x now references a new object
```

### Mutable

`Mutable` objects can have their content modified after they are created.

- `list`
- `dict`
- `set`
- Instances of user-defined classes

```python
lst = [1, 2, 3]
print(id(lst))  # This gives the memory address of the object lst references

lst.append(4)   # Modifies the original list object
print(id(lst))  # The memory address remains the same

```
