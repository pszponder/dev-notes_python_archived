# Python Sets

A `set` is an unordered collection of _unique_ values

- Sets are unordered
- Set elements are unique. Duplicate elements are not allowed.
- A set itself may not be modified, but the elements contained in the set must be of an immutable type.

## Creating a Set

There are two ways to create sets:

1. using curly braces `{}`
2. using the built-in function `set()`

`set()` syntax

- To define a set using the `set()` function, pass in an iterable (list, tuple, or even a string)

```python
x = set(<iterable>)
```

```python
# Define a set using curly braces
s = {1, 2, 3}

# Convert a list or tuple into a set
s2 = set([1, 2, 3]) # {1, 2, 3}

x = set(['foo', 'bar', 'baz', 'foo', 'qux'])
print(x) # {'qux', 'foo', 'bar', 'baz'}

# convert a tuple into a set
s3 = set((1, 2, 3)) # {1, 2, 3}

y = set(('foo', 'bar', 'baz', 'foo', 'qux'))
print(y) # {'qux', 'foo', 'bar', 'baz'}

# convert a string into a set
# NOTE: order of string characters may or may not be preserved
s4 = set("hello") # {'e', 'l', 'o', 'h'}
```

### Automatically Remove Duplicate Values

A set automatically removes all the duplicate values.

```python
# Any duplicate items passed into a set are removed automatically
s = {1, 2, 3, 2, 3, 4}
print(s) # {1, 2, 3, 4}
```

### Creating an Empty Set

**CAUTION:** Creating empty sets

- When creating an empty set, be sure to not use empty curly braces `{}` or you will end up creating an empty dictionary instead
- To create an empty set, you **MUST** use the `set()` function

```python
# NOTE: THIS IS NOT HOW YOU DECLARE A SET!
# A set of empty curly braces actually defines an empty dictionary
s = {}  # this will create a dictionary instead of a set
type(s)
# <class 'dict'>
```

### Restrictions on Set Creation

**CAUTION:** Can't pass lists or dictionaries into sets as values

- Since set elements must be immutable, neither lists nor dictionaries can be set as elements in a set

```python
# Define a list
a = [1, 2, 3]

# Attempt to create a set using a set literal and the list
# NOTE: This will throw an error
set_a = {a}
"""
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    {a}
TypeError: unhashable type: 'list'
"""

# NOTE: We can however, pass list "a" into the set() method
#  this is because, each element of list a is an immutable type
set_b = set(a) # {1, 2, 3}

# NOTE 2: However, if we try to use the set() function
#  on a nested array, we will again get an error since
#  the elements of the lists are lists themselves and are mutable
c = [[1, 2], [3, 4], [5, 6]]
set_c = set(c)
"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
"""

# Define a dictionary
d = {'a': 1, 'b': 2}

# Attempt to create a set using a set literal and the dictionary
# NOTE: This will throw an error
set_d = {d}
"""
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    {d}
TypeError: unhashable type: 'dict'
"""
```

## Manipulating Sets

### Adding items to a set

Using the `add()` method we can add a single element to the set.

```python
# Define a set
s = {1, 2, 3}

# Add an item to the set
s.add(4)

print(s) # {1, 2, 3, 4}
```

### Modifying / Updating a Set

#### Modify a set by union

By passing in a list, set, or tuple into a set via the `update()` method, add all items (that are not duplicates) to the set:

```python
x1.update(x2[, x3 ...])

#OR

x1 |= x2 [| x3 ...]
```

```python
# Define a set
s = {1, 2, 3}

# Add multiple items to the set via a list
# duplicate values are not stored in the set
# You can also pass in another set, a tuple, or a string (iterables)
s.update([2, 3, 4, 5, 6])
print(s) # {1, 2, 3, 4, 5, 6}

# Can also pass in a single element to the update method to add it to the set
s.update(7)
print(s) # {}
```

You can also use an argument assignment `|=` to update the set

```python
# Define two sets
x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'baz', 'qux'}
x3 = {'foo', 'corge', 'garply'}

# Add the contents of set x2 and x3 to the contents of set x1
# Only unique values are added to the set
x1 |= x2 | x3
print(x1) # {'qux', 'corge', 'garply', 'foo', 'bar', 'baz'}
```

#### Modify a set by intersection

`x1.intersection_update(x2)` and `x1 &= x2` update `x1`, retaining only elements found in both `x1` and `x2`:

```python
x1.intersection_update(x2[, x3 ...])

# OR

x1 &= x2 [& x3 ...]
```

```python
x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'baz', 'qux'}

# Update x1 to contain only values shared in both x1 and x2
x1 &= x2
x1 # {'foo', 'baz'}

# update x1 to contain only values shared with values in passed in array
x1.intersection_update(['baz', 'qux'])
x1 # {'baz'}
```

#### Modify a set by difference

`x1.difference_update(x2)` and `x1 -= x2` update `x1`, removing elements found in `x2`:

```python
x1.difference_update(x2[, x3 ...])

# OR

x1 -= x2 [| x3 ...]
```

```python
# Define two sets
x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'baz', 'qux'}

# Remove any values from x1 that are also in x2
x1 -= x2
x1 # {'bar'}

# Remove any values in x1 that are also in the passed in list
x1.difference_update(['foo', 'bar', 'qux'])
x1 # set()
```

#### Modify a set by symmetric difference

`x1.symmetric_difference_update(x2)` and `x1 ^= x2` update `x1`, retaining elements found in either `x1` or `x2`, but not both:

```python
x1.symmetric_difference_update(x2)

# OR

x1 ^= x2
```

```python
# Define two sets
x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'baz', 'qux'}

# Update x1 to contain values which are not shared between x1 & x2
# "bar" is in x1 but not x2, "qux" is in x2, but not in x1
x1 ^= x2
x1 # {'bar', 'qux'}

# Update x1 to contain values not shared between x1 and the list
x1.symmetric_difference_update(['qux', 'corge'])
x1 # {'bar', 'corge'}
```

### Removing items from a set

#### remove()

Both the `remove()` and `discard()` methods will remove an element from the set.

`remove()` will raise a `key error` if the value doesn't exist.

`x.remove(<elem>)` removes `<elem>` from `x`. Python raises an exception if `<elem>` is not in `x`:

```python
# Define a set
s = {1, 2, 3}

# Remove the value 3 from the set
s.remove(3)
print(s) # {1, 2}

# Attempt to remove a non-existent value from the set
# remove() will raise an error if the value does not exist in the set
s.remove(3)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 3
```

#### discard()

`discard()` will remove a value in the set if it exists. If the value does not exist, nothing will happen (unlike `remove()`, it won't raise any errors).

```python
# Define a set
s = {1, 2, 3}

# Remove a value from the set
s.discard(3)
print(s) # {1, 2}

# Attempt to remove a non-existant value from the set
s.discard(3)
```

#### pop()

`x.pop()` removes and returns a random chosen element from the set. If `x` is empty, `x.pop()` raises an exception

```python
# Define a set
x = {'foo', 'bar', 'baz'}

# Remove a random element from the set
x.pop() # 'bar'
x       # {'baz', 'foo'}

# Remove another random element from the set
x.pop() # 'baz'
x       # {'foo'}

# Remove another random element from the set
x.pop() # 'foo'
x       # set()

# Attempt to remove another random element from the set
# this time, since there aren't any elements left in the set
#  (the set is empty), an error will be raised
x.pop()
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    x.pop()
KeyError: 'pop from an empty set'
```

### Check if value exists in a set (set membership)

Use the `in` and `not in` keywords to check if a value is or is not in a set

```python
# Define a set
my_set = {1, 2, 3, 4, 5}

# Determine if 1 is in the set
print(1 in my_set) # True

# Determine if 1 is NOT in the set
print(1 not in my_set) # False

# Determine if 6 is in the set
print(6 in my_set) # False

# Determine if 6 is NOT in the set
print(6 not in my_set) # True
```

### Finding the length of a set

Use the `len()` function to find the length of a set

```python
# Define a set
my_set = {1, 2, 3, 4, 5}

# find the length of the set
set_length = len(my_set) # 5
```

### Convert a set into a list

Use the `list()` function to convert a set into a list

```python
# Define a set
my_set = {1, 2, 3, 4, 5}

# Convert the set into a list
my_list = list(my_set)
print(my_list) # [1, 2, 3, 4, 5]
```

### De-duplicating a list using sets

A useful trick to de-duplicate a list (removing duplicate values), is to convert the list into a set, and then convert that set back into a list

```python
list_with_duplicates = [1, 1, 2, 2, 3, 4, 4, 5]

# Convert the list into a set
# This step removes duplicates list values
s = set(list_with_duplicates)
print(s) # {1, 2, 3, 4, 5}

# Convert the set back into a list
list_unique = list(s)
print(list_unique) # [1, 2, 3, 4, 5]
```

### Copy a set w/ `copy()`

Use the `copy()` method to create a copy of a set

```python
my_set = {1, 2, 3, 4, 5}

# Create a copy of my_set and store in variable called new_set
new_set = my_set.copy()
print(new_set) # {1, 2, 3, 4, 5}
```

### Clear a set w/ `clear()`

Use the `clear()` method to clear out the contents of a set

```python
s = {1, 2, 3, 4, 5}
print(s) # {1, 2, 3, 4, 5}

# Clear the contents of the set
s.clear()
print(s) # set()
```

## Set Operations

### set union() and |

The `union()` method & `|` operator creates a new set with all elements from the associated sets.

```python
x1.union(x2[, x3 ...])

# OR

x1 | x2 [| x3 ...]
```

```python
# Define two or more sets
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = {4, 5, 6}

# Use either the union method or "|" operator to create a set union
union1 = s1.union(s2, s3)  # {1, 2, 3, 4, 5, 6}
union2 = s1 | s2 | s3      # {1, 2, 3, 4, 5, 6}
```

```python
a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {3, 4, 5, 6}
d = {4, 5, 6, 7}

# Find the union of all sets using either union() or |
a.union(b, c, d) # {1, 2, 3, 4, 5, 6, 7}
a | b | c | d    # {1, 2, 3, 4, 5, 6, 7}
```

**NOTE:** `union()` vs `|`

- When you use the `|` operator, both operands must be sets.
- The `.union()` method, on the other hand, will take any iterable as an argument, convert it to a set, and then perform the union.

```python
>>> x1 | ('baz', 'qux', 'quux')
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    x1 | ('baz', 'qux', 'quux')
TypeError: unsupported operand type(s) for |: 'set' and 'tuple'

>>> x1.union(('baz', 'qux', 'quux'))
{'baz', 'quux', 'qux', 'bar', 'foo'}
```

### set intersection() and &

`intersection` or `&` will return a new set with only the elements that are common to all sets.

```python
x1.intersection(x2[, x3 ...])

# OR

x1 & x2 [& x3 ...]
```

```python
# Define two or more different sets
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}

# Use either intersection method or "&" operator to create
# an intersection union
intersection1 = s1.intersection(s2, s3) # {3}
intersection2 = s1 & s2 & s3            # {3}
```

```python
a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {3, 4, 5, 6}
d = {4, 5, 6, 7}

# The resulting set contains only elements that are present in all of the specified sets
a.intersection(b, c, d) # {4}
a & b & c & d           # {4}
```

This is opposite of `symmetric_difference`

### set difference

`difference` or `-` will return a set with only the elements that are unique to the first set (invoked set).

```python
x1.difference(x2[, x3 ...])

# OR

x1 - x2 [- x3 ...]
```

**NOTE:** How to think about `set difference`?

- Another way to think about this the `set difference` is the set which results from taking all values in `x2`, `x3`, ... and subtracting them from `x1`

```python
# Define two sets
s1 = {1, 2, 3}
s2 = {2, 3, 4}

# Define the set difference between s1 and s2
# Of all values in two sets, s1 has value of 1 which is unique
diff1 = s1.difference(s2) # {1}
diff2 = s1 - s2           # {1}

# Define the set difference between s2 and s1
# Of all values in two sets, s2 has value of 4 which is unique
diff3 = s2.difference(s1) # {4}
diff4 = s2 - s1           # {4}
```

```python
a = {1, 2, 3, 30, 300}
b = {10, 20, 30, 40}
c = {100, 200, 300, 400}

"""
When multiple sets are specified,
the operation is performed from left to right.

In this example,
a - b is computed first, resulting in {1, 2, 3, 300}.
Then c is subtracted from that set, leaving {1, 2, 3}:
"""
a.difference(b, c) # {1, 2, 3}
a - b - c          # {1, 2, 3}
```

### set symmetric_difference

`symetric_difference` or `^` will return all the elements that are not common between the sets:

```python
# NOTE: symmetric_difference() can only accept a single argument
x1.symmetric_difference(x2)

# OR

# NOTE: ^ can be used to compute symmetric_difference on two or more sets
x1 ^ x2 [^ x3 ...]
```

```python
# Define sets
s1 = {1, 2, 3}
s2 = {2, 3, 4}

# Generate symmetric difference between the sets
# Returns items not common to two sets
sym_diff1 = s1.symmetric_difference(s2) # {1, 4}
sym_diff2 = s1 ^ s2                     # {1, 4}
```

```python
a = {1, 2, 3, 4, 5}
b = {10, 2, 3, 4, 50}
c = {1, 50, 100}

# Compute symmetric difference on all three sets
# NOTE: Can't do this with the symmetric_difference() method
a ^ b ^ c # {100, 5, 10}
```

This is opposite of `intersection`

### Determine if two sets have any elements in common

Use the `isdisjoint()` method to determine if two sets have any elements in common.

`isdisjoint()` returns a boolean value:

- `True` if there aren't any values in common between the sets
- `False` if at least one value is common between the sets

```python
x1.isdisjoint(x2)
```

```python
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}

x1.isdisjoint(x2) # False

x2 - {'baz'} # {'quux', 'qux'}

x1.isdisjoint(x2 - {'baz'}) # True
```

**NOTE:**

- The intersection of two disjoint sets is an empty set
- If `x1.isdisjoint(x2)` is `True`, then `x1 & x2` (or `x1.intersection(x2)`) is an empty set (`set()`)

```python
x1 = {1, 3, 5}
x2 = {2, 4, 6}

# Verify that the two sets are disjoint
x1.isdisjoint(x2) # True

# If x1 and x2 are disjoint,
#  then their intersection is an empty set
x1 & x2 # set()
```

### Determine whether one set is a subset of the other w/ issubset()

In set theory, a set `x1` is considered a subset of another set `x2` if every element of `x1` is in `x2`.

```python
# Returns True if x1 is a subset of x2
# Returns False otherwise
x1.issubset(x2)

# OR

# Returns True if x1 is a subset of x2
# Returns False otherwise
x1 <= x2
```

```python
x1 = {'foo', 'bar', 'baz'}
print(x1.issubset({'foo', 'bar', 'baz', 'qux', 'quux'})) # True

x2 = {'baz', 'qux', 'quux'}
print(x1 <= x2) # False
```

### Determine whether one set is a proper subset of another w/ <

A proper subset is the same as a subset, except that the sets can’t be identical.

A set `x1` is considered a proper subset of another set `x2` if every element of `x1` is in `x2`, and `x1` and `x2` are not equal.

```python
x1 = {'foo', 'bar'}
x2 = {'foo', 'bar', 'baz'}
print(x1 < x2) # True

x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'bar', 'baz'}
print(x1 < x2) # False
```

### Determine whether one set is a superset of the other w/ issuperset

A superset is the reverse of a subset. A set `x1` is considered a superset of another set `x2` if `x1` contains every element of `x2`.

`x1.issuperset(x2)` and `x1 >= x2` return `True` if `x1` is a superset of `x2`:

```python
x1 = {'foo', 'bar', 'baz'}

x1.issuperset({'foo', 'bar'}) # True

x2 = {'baz', 'qux', 'quux'}
x1 >= x2 # False
```

### Determine whether one set is a proper superset of the other

A proper superset is the same as a superset, except that the sets can’t be identical. A set `x1` is considered a proper superset of another set `x2` if `x1` contains every element of `x2`, and `x1` and `x2` are not equal.

`x1 > x2` returns `True` if `x1` is a proper superset of `x2`:

```python
x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'bar'}
x1 > x2 # True

x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'bar', 'baz'}
x1 > x2 # False
```

## References

- [Python Cheat Sheet - Sets](https://www.pythoncheatsheet.org/cheatsheet/sets)
- [Real Python - Sets](https://realpython.com/python-sets/)
