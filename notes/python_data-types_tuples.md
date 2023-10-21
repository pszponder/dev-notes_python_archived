# Tuples

Tuples are identical to [lists](python_data-types_lists.md) in all respects, except for the following properties:

- Tuples are defined by enclosing the elements in parentheses (`()`) instead of square brackets (`[]`).
- Tuples are immutable.

## Defining a Tuple

A `tuple` is defined using parenthesis `()` instead of square brackets

**NOTE:** Accessing and Slicing Tuples

- Even though tuples are defined using parentheses, you still index and slice tuples using square brackets, just as for strings and lists.

```python
# Declare a tuple using parenthesis
furniture = ('table', 'chair', 'rack', 'shelf')

# Inspect the tuple
print(furniture[0]) # 'table'
print(furniture[1:3]) # ('chair', 'rack')
len(furniture) # 4

t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')
print(t)       # ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')
print(t[0])    # 'foo'
print(t[-1])   # 'corge'
print(t[1::2]) # ('bar', 'qux', 'corge')
```

```python
my_tuple = (1, 2, 3, 4, 5)

# You can perform any operation on a tuple that does not change the data
print(my_typle[0])   # 1
print(5 in my_tuple) # true

# Create a new tuple which is a slice of the original
new_tuple = my_tuple[1:2]
print(new_tuple) # (2, )

new_tuple2 = my_tuple[1:4]
print(new_tuple2) # (2, 3, 4)

# Assign mulitple variables based on value (and position) in tuple
# Note, if other contains 2 or more values, it will be a list
x, y, z, *other = (1, 2, 3, 4, 5)

print(x)     # 1
print(y)     # 2
print(z)     # 3
print(other) # [4, 5]
```

### Defining a tuple with a single value

To tell Python that you really want to define a singleton tuple, include a trailing comma (,) just before the closing parenthesis:

```python
t = (2,)
print(type(t)) # <class 'tuple>'
print(t[0])    # 2
print(t[-1])   # 2
```

## Tuple Unpacking

In Python, you can unpack sequences (like lists or tuples) into variables using a similar syntax to JavaScript's array unpacking

```python
# A literal tuple containing several items can be assigned to a single object:
t = ('foo', 'bar', 'baz', 'quix')

# Unpacking the tuple and assigning values to seperate variables
# NOTE: When unpacking, the number of variables on the left must match the number of values in the tuple:
(s1, s2, s3, s4) = t

print(s1) # 'foo'
print(s2) # 'bar'
print(s3) # 'baz'
print(s4) # 'qux'
```

```python
a, b, c = (1, 2, 3)
print(a)  # Outputs: 1
print(b)  # Outputs: 2
print(c)  # Outputs: 3
```

You can also use the `*` syntax to capture multiple items.

```python
first, *middle, last = (1, 2, 3, 4, 5)
print(first)   # Outputs: 1
print(middle)  # Outputs: [2, 3, 4]
print(last)    # Outputs: 5
```

**NOTE:** In the case of a tuple, the unpacked item ends up as an array, and not another tuple.

## Tuples vs Lists

The main way that tuples are different from lists is that tuples, like strings, are immutable.

- `tuples` are `immutable` (they cannot be changed)
- `lists` are `mutable` (they can be modified)
- `tuples` are more memory efficient than `lists`

**NOTE:** Use tuples if you data doesn't change

- If your data doesn't change once it is created, it is more performant to use tuples over lists
- A good example of when a Tuple would be a good data structure would be when storing Latitude and Longitude pairs, these points don't change.

**NOTE:** Why use a tuple instead of a list?

- Program execution is faster when manipulating a tuple than it is for the equivalent list. (This is probably not going to be noticeable when the list or tuple is small.)
- Sometimes you don’t want data to be modified. If the values in the collection are meant to remain constant for the life of the program, using a tuple instead of a list guards against accidental modification.
- There is another Python data type that you will encounter shortly called a dictionary, which requires as one of its components a value that is of an immutable type. A tuple can be used for this purpose, whereas a list can’t be.

## Tuple Functions & Methods

### Len

Use the `len()` function to determine the number of items inside the tuple

```python
my_tuple(1, 2, 3, 4, 5)

# Obtain the length of the tuple
print(len(my_tuple)) # 5
```

### Count

`count()` returns the number of times a specified value occurs in a tuple

```python
my_tuple1(1, 2, 3, 4, 5)
my_tuple2(1, 2, 3, 4, 3)

# Determine how many times specified value occurs in the tuple
print(my_tuple1.count(5)) # 1
print(my_tuple2.count(3)) # 2
```

### Index

`index()` searches the tuple for a specific value and returns the position of where it was found

```python
my_tuple(1, 2, 3, 4, 5)

# Determine the index of the specified value in the tuple
print(my_tuple[2]) # 3
print(my_tuple[len(my_tuple) - 1]) # 5
```

## Using tuples to swap variable values

```python
a = "foo"
b = "bar"

# Swap values of a and b
(a, b) = (b, a) # Can also just do this: a, b, = b, a

print(a) # "bar"
print(b) # "foo"
```

## Converting between list() and tuple()

```python
# Convert a list into a tuple
tuple(['cat', 'dog', 5]) # ('cat', 'dog', 5)

# Convert a tuple into a list
list(('cat', 'dog', 5)) # ['cat', 'dog', 5]

# Convert the characters of a string to a list
list('hello') # ['h', 'e', 'l', 'l', 'o']
```

## Resources / References

- [Python Cheatsheet - Lists and Tuples](https://www.pythoncheatsheet.org/cheatsheet/lists-and-tuples)
- [RealPython - Lists and Tuples in Python](https://realpython.com/python-lists-tuples/)
