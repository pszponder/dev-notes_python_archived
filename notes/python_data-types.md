# Python Data Types

Python supports the following Data Types:

- Strings
- Integers
- Booleans
- Floats
- Bytes
- Dictionary
- List
- Tuple
- Set
- Complex
- Frozenset
- Range
- Binary

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

## [Strings](python_data-types_strings.md)

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

## [Lists](python_data-types_lists.md)

[`Lists`](python_data-types_lists.md) are an ordered collection of items which can be of any type and are _mutable_.

```python
fruits = ["apple", "banana", "cherry"]
```

## [Tuples](python_data-types_tuples.md)

[`Tuples`](python_data-types_tuples.md) are ordered collections of items, which can be of any type but are _immutable_.

```python
coordinates = (4.0, 5.0)
```

## [Sets](python_data-types_sets.md)

[`Sets`](python_data-types_sets.md) are an _unordered_ collection of _unique_ items

```python
# Any duplicate numbers passed into the set are removed
unique_numbers = {1, 2, 2, 3, 3, 3}

print(unique_numbers)  # {1, 2, 3}
```

## Dictionaries

[`Dictionaries`](python_data-types_dictionaries.md) are _unordered_ collections of key-value pairs

```python
person = {"name": "John", "age": 30}
```

## None

`None` represents the lack / absence of a value. Think of this as the equivalent to `null` in other languages like JavaScript.

`None` is often used when initializing a variable which will have its value changed in later in the code.

```python
# Initialize the user variable with a value of None
user = None

# Update the value of user
user = "bob"
```

## Mutable vs Immutable Types

**NOTE:**

- All data types in Python are objects.
- When you create a variable in Python, you're creating a reference to an object
- All variables in Python store references to object
- The key distinction to remember is whether the object being referenced is mutable or immutable

### Immutable

`Immutable` types in Python are types which after being created, cannot be modified.

- Numbers (`int`, `float`, `binary`)
- Booleans
- `str`
- Bytes
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

## Python Iterables

> [! NOTE] Python `Iterable`s
> An `iterable` is a collection which can be iterated over in a loop
>
> In Python, iterable types are:
>
> - `string`
> - `list`
> - `tuple`
> - `dictionary`
> - `set`

## Type Casting / Type Conversion

We can use type casting in Python to convert a value from one type to another

```python
# Convert string "12" into an integer
int("12") # 12

# Convert string "3.3" into a float
float("3.3") # 3.3

# Convert float into string
str(44.5) # "44.5"

# Convert number into a boolean
bool(0) # False
bool(1) # True

# Convert a binary to an integer
int("0b101", 2) # 5

# Convert an integer to binary using the bin() function
bin_val = bin(5) # "0b101"

# Convert a list into a tuple
tup = tuple(['cat', 'dog', 5]) # ('cat', 'dog', 5)

# Convert a tuple into a list
li1 = list(('cat', 'dog', 5)) # ['cat', 'dog', 5]

# Convert the characters of a string to a list
li2 = list('hello') # ['h', 'e', 'l', 'l', 'o']

# Convert a list into a set
s2 = set([1, 2, 3]) # {1, 2, 3}

# convert a tuple into a set
s3 = set((1, 2, 3)) # {1, 2, 3}

# convert a string into a set
s4 = set("hello") # {'e', 'l', 'o', 'h'}
```

## References

- [Real Python - Python's Mutable vs Immutable Types: What's the Difference?](https://realpython.com/python-mutable-vs-immutable-types/#:~:text=types%20in%20Python.-,Mutability%20vs%20Immutability,its%20internal%20state%20after%20creation.)
