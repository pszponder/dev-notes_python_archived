# Python Lists

A `list` is an ordered collection of items, which can be of any type

Characteristics of Python Lists:

- Lists are ordered
- Lists can contain arbitrary objects
- List elements can be accessed by index
- List elements can be nested to arbitrary depth
- Lists are mutable
- Lists are dynamic

**NOTE:** If you don't plan to modify your list (add or remove elements), it is better to use a [tuple](python_data-types_tuples.md) instead

```python
a = ["foo", "bar", "baz", "qux"]

# Lists can store any combination of values / objects
li0 = [21.42, 'foobar', 3, 4, 'bark', False, 3.14159]

li1 = [1, 2, 3, 4, 5]

li2 = ['a', 'b', 'c']

li3 = [1, 2, 'a', True]

li4 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
] # nested array
```

## Defining Lists

```python
# Empty List
empty = []

# String List
fruits = ["apple", "banana", "cherry"]

# Number List
numbers = [1, 2, 3, 4, 5]

# Mixed List (multiple types)
mixed = ["apple", 2, 3.5]

# 2D List
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
```

## Accessing Values from a List

```python
fruits = ["apple", "banana", "cherry"]

print(fruits[0])  # apple
print(fruits[1])  # banana
print(fruits[2])  # cherry

# Use negative indexes to access values from a list starting from the last element
print(fruits[-1]) # cherry
print(fruits[-2]) # banana
print(fruits[-3]) # apple
```

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

value1 = matrix[0][0]  # 1
value2 = matrix[0][1]  # 2
value3 = matrix[0][2]  # 3
value4 = matrix[1][0]  # 4
value5 = matrix[1][1]  # 5
value6 = matrix[1][2]  # 6
```

## Iterate Over Elements in a List

[Iterating over Lists](python_loops.md#iterate-over-iterables-lists-tuples-strings-etc)

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

## List Slices

Slicing is a versatile operation in Python that can be used to extract a portion of a list (or any other sequence type like strings or tuples)

```python
list[start:stop:step]

# start -- The starting index (inclusive)
# stop  -- The stopping index (exclusive)
# step  -- The step size or increment value. Defaults to 1
```

```python
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Extract elements from index 2 up to (but not including) index 5
subset1 = lst[2:5]  # [2, 3, 4]

# Extract elements from the beginning up to index 5
subset2 = lst[:5]  # [0, 1, 2, 3, 4]

# Extract elements from index 5 to the end
subset3 = lst[5:]  # [5, 6, 7, 8, 9]

# Extract every 2nd element from the list
subset4 = lst[::2]  # [0, 2, 4, 6, 8]

# Extract every 2nd element from index 2 up to index 8
subset5 = lst[2:8:2]  # [2, 4, 6]

# Extract the last 3 elements
subset6 = lst[-3:]  # [7, 8, 9]

# Extract elements from the third-last to the fifth last
subset7 = lst[-5:-2]  # [5, 6, 7]

# Use slicing to reverse a list
subset8 = lst[::-1] # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# NOTE: If start >= stop and step > 0, slice is empty
subset9 = lst[99:2]  # []
```

## Get the length of a list

Use the `len(<list>)` function to get the length of a passed in list

```python
fruits = ["apple", "banana", "cherry"]

length = len(fruits)
print(length)  # 3
```

## Merge / Concatenate and Replicate lists

```python
# Merge two ore more lists together using the "+" operator
print([1, 2, 3] + ['A', 'B', 'C']) # [1, 2, 3, 'A', 'B', 'C']

# Replicate lists using the "*" operator and an integer value
print(['X', 'Y', 'Z'] * 3)
# ['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']

# Update the value of my_list by appending onto it another list
my_list = [1, 2, 3]
my_list = my_list + ['A', 'B', 'C']
print(my_list) # [1, 2, 3, 'A', 'B', 'C']
```

```python
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

# For each item in list2, append it to list1
for x in list2:
    list1.append(x)

print(list1) # ["a", "b", "c", 1, 2, 3]
```

```python
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

# Add the contents of list2 to list1
list1.extend(list2)

print(list1) # ["a", "b", "c", 1, 2, 3]
```

## Repeating a list

```python
repeated = ["a"] * 3
print(repeated)  # ['a', 'a', 'a']
```

## Check if an item exists in the list (Membership)

```python
if "apple" in fruits:
    print("Apple is in the list!")
```

## Common List Methods / Manipulations

### Modify individual list values with indexes

```python
furniture = ['table', 'chair', 'rack', 'shelf']

furniture[0] = 'desk'
print(furniture) # ['desk', 'chair', 'rack', 'shelf']

furniture[2] = furniture[1]
print(furniture) # ['desk', 'chair', 'chair', 'shelf']

furniture[-1] = 'bed'
print(furniture) # ['desk', 'chair', 'chair', 'bed']

cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]

cart[0] = "laptop" # change the 1st value of the list
print(cart) # ["laptop", "sunglasses", "toys", "grapes"]
```

### Modify multiple list values simultaneously with slice assignment

You can also modify multiple list values at the same time using [slice assignment](https://realpython.com/python-assignment-operator/#updating-lists-through-indices-and-slices)

```python
# Syntax for slice assignment
a[m:n] = <iterable>
```

The number of elements inserted need not be equal to the number replaced. Python just grows or shrinks the list as needed.

```python
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']

print(a[1:4]) # ['bar', 'baz', 'qux']

# Replace items at index 1 through 3 with values in specified array
a[1:4] = [1.1, 2.2, 3.3, 4.4, 5.5]

print(a) # ['foo', 1.1, 2.2, 3.3, 4.4, 5.5, 'quux', 'corge']

print(a[1:6]) # [1.1, 2.2, 3.3, 4.4, 5.5]

# Replace items from index 1 through 5 with value in specified array
a[1:6] = ['Bark!']

print(a) # ['foo', 'Bark!', 'quux', 'corge']
```

You can insert multiple elements in place of a single element—just use a slice that denotes only one element:

```python
a = [1, 2, 3]

# Replace item at index 1 with values in specified array
a[1:2] = [2.1, 2.2, 2.3]

print(a) # [1, 2.1, 2.2, 2.3, 3]

#=======================================================================
# NOTE! this isn't the same as replacing the single element with a list:
#=======================================================================
b = [1, 2, 3]

# Insert a nested array in the place of the value at index 1
b[1] = [2.1, 2.2, 2.3]

print(b) # [1, [2.1, 2.2, 2.3], 3]
```

You can also insert elements into a list without removing anything. Simply specify a slice of the form `[n:n]` (a zero-length slice) at the desired index:

```python
a = [1, 2, 7, 8]

a[2:2] = [3, 4, 5, 6]

print(a) # [1, 2, 3, 4, 5, 6, 7, 8]
```

### Add Elements to a List

**CAUTION:** The `append()` and `insert()` methods change the list they are invoked on in place

#### Add elements to the end of the list w/ append()

`append` adds an element to the end of a `list`. This is analogous to the `push()` method for arrays in JavaScript

```python
fruits = ["apple", "banana", "cherry"]
fruits.append("grape")
print(fruits)  # ['apple', 'banana', 'cherry', 'grape']

furniture = ['table', 'chair', 'rack', 'shelf']
furniture.append('bed')
print(furniture) # ['table', 'chair', 'rack', 'shelf', 'bed']
```

#### Add elements from another list or iterable w/ extend()

```python
fruits = ["apple", "banana", "cherry"]
fruits.extend(["kiwi", "orange"])
print(fruits)  # ['apple', 'banana', 'cherry', 'kiwi', 'orange']
```

#### Add an element to a specific index position w/ insert()

`insert` adds an element to a `list` at a given position:

```python
<list>.insert(idx, value)
```

```python
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "blueberry")  # Inserts "blueberry" at position 1
print(fruits)  # ['apple', 'blueberry', 'banana', 'cherry']

furniture = ['table', 'chair', 'rack', 'shelf']
furniture.insert(1, 'bed')
print(furniture) # ['table', 'bed', 'chair', 'rack', 'shelf']

basket = [1, 2, 3, 4, 5]
basket.insert(len(basket), 6)
print(basket) # [1, 2, 3, 4, 5, 6]
```

#### Prepending / Appending Items to a List

Additional items can be added to the start or end of a list using the + concatenation operator or the `+=` [augmented assignment operator](https://realpython.com/python-assignment-operator/#augmented-assignment-operators-in-python):

```python
# Append elements to list a
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
a += ['grault', 'garply']
print(a) # ['foo', 'bar', 'baz', 'qux', 'quux', 'corge', 'grault', 'garply']

# Prepend elements to list b
b = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
b = [10, 20] + b
print(b) # [10, 20, 'foo', 'bar', 'baz', 'qux', 'quux', 'corge']
```

Note that a list must be concatenated with another list, so if you want to add only one element, you need to specify it as a singleton list:

```python
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
a += 20
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    a += 20
TypeError: 'int' object is not iterable

a += [20]
print(a)  # ['foo', 'bar', 'baz', 'qux', 'quux', 'corge', 20]
```

#### Extend an existing list

Use the `extend()` method to append a list of values to an existing list. `extend()` accepts an iterable object

```python
li = [1, 2, 3, 4, 5]
li.extend([100, 101])
print(li) # [1, 2, 3, 4, 5, 100, 101]
```

### Removing Elements from a List

#### Remove value from specified index of list using del keyword

`del` keyword removes an item using the index:

```python
furniture = ['table', 'chair', 'rack', 'shelf']
del furniture[2]
print(furniture) # ['table', 'chair', 'shelf']

del furniture[2]
print(furniture) # ['table', 'chair']
```

#### Remove the first item with the specified value w/ remove()

`remove()` removes an item with using actual value of it:

```python
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)  # ['apple', 'cherry']

furniture = ['table', 'chair', 'rack', 'shelf']
furniture.remove('chair')
print(furniture) # ['table', 'rack', 'shelf']
```

**CAUTION:** Removing repeated items

- If the value appears multiple times in the list, only the 1st instance of the value will be removed.
- To remove multiple instances of the value, will have to loop through the list.

#### Remove element at specified position, or last item of the index w/ pop()

By default, `pop` will remove and return the last item of the list.

**NOTE:** `pop()` can also remove a value from specified index

- You can also pass the index of the element as an optional parameter:
- The `pop()` method returns the item which was removed from the list

```python
animals = ['cat', 'bat', 'rat', 'elephant']

# Remove the last element of the list
animals.pop()  # returns 'elephant'
print(animals) # ['cat', 'bat', 'rat']

# Remove the 0th element in the list
animals.pop(0) # returns 'cat'
print(animals) # ['bat', 'rat']

fruits = ["apple", "banana", "cherry"]
fruits.pop()         # Removes the last item
fruits.pop(1)        # Removes the item at position 1
```

#### Remove all items from the list w/ clear()

Use the `clear()` method to remove all existing elements from a list

```python
li = [1, 2, 3, 4, 5]
li.clear()
print(li) # []

fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)  # []
```

#### Remove multiple elements using slice assignment

You can remove multiple elements out of the middle of a list by assigning the appropriate slice to an empty list.

You can also use the `del` statement with the same slice:

```python
# Remove values from index 1 through 4 by replacing with empty array
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
a[1:5] = []
print(a) # ['foo', 'corge']

# Delete values from index 1 through 4 via the del keyword
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
del a[1:5]
print(a) # ['foo', 'corge']
```

### Creating a copy of a list

Since Lists are reference types in Python, it is a good idea to create a clone / copy of the list you are modifying.

Slicing a complete list will create a copy of the list

```python
spam = ['cat', 'bat', 'rat', 'elephant']

# Create a copy of the list
spam2 = spam[:] # ['cat', 'bat', 'rat', 'elephant']

spam.append('dog')
print(spam)  # ['cat', 'bat', 'rat', 'elephant', 'dog']
print(spam2) # ['cat', 'bat', 'rat', 'elephant']
```

You can also use the `.copy()` method to create a copy of a list

- **CAUTION:** Using `.copy()` only creates a Shallow Copy

```python
spam = ['cat', 'bat', 'rat', 'elephant']

# Create a copy / clone of the "spam" list
spam_copy = spam.copy()

print(spam)      # ['cat', 'bat', 'rat', 'elephant']
print(spam_copy) # ['cat', 'bat', 'rat', 'elephant']
```

#### Deep Copy w/ copy.deepcopy

To create a deep copy of a list, you need to import the `copy` module

```python
import copy

original_list = [[1, 2, 3], [4, 5, 6]]
copied_list = copy.deepcopy(original_list)

# Modifying the copied list
copied_list[0][0] = 99

print(original_list)  # Outputs: [[1, 2, 3], [4, 5, 6]]
print(copied_list)    # Outputs: [[99, 2, 3], [4, 5, 6]]
```

### Find index of a value using **index()**

The `index()` method allows you to find the index of a value by passing its name:

The `index()` method returns the index position of the 1st occurrence of the specified value

```python
furniture = ['table', 'chair', 'rack', 'shelf']

furniture.index('chair') # 1
```

```python
# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# index of 'e' in vowels
index = vowels.index('e')
print('The index of e:', index) # The index of e: 1

# element 'i' is searched
# index of the first 'i' is returned
index = vowels.index('i')
print('The index of i:', index) # The index of i: 2
```

**CAUTION:** If the value does not exist in the list, Python will throw a `ValueError` exception

```python
# vowels list
vowels = ['a', 'e', 'i', 'o', 'u']

# index of 'p' is vowels
index = vowels.index('p')
print('The index of p:', index) # ValueError: 'p' is not in list
```

The list `index()` method can take a maximum of three arguments:

- **element** - the element to be searched
- **start** (optional) - start searching from this index
- **end** (optional) - search the element up to this index

```python
# alphabets list
alphabets = ['a', 'e', 'i', 'o', 'g', 'l', 'i', 'u']

# index of 'i' in alphabets
index = alphabets.index('e')   # 1
print('The index of e:', index) # The index of e: 1

# 'i' after the 4th index is searched
index = alphabets.index('i', 4)   # 6
print('The index of i:', index) # The index of i: 6

# 'i' between 3rd and 5th index is searched
index = alphabets.index('i', 3, 5)   # Error!
print('The index of i:', index) # ValueError: 'i' is not in list
```

### Return the number of times a value appears in a list w/ count()

```python
fruits = ["apple", "banana", "cherry"]
count = fruits.count("apple")
print(count)  # 1
```

### Sorting Lists

#### Sort a list in place w/ sort()

```python
fruits = ["apple", "banana", "cherry"]
numbers.sort()        # Ascending order
numbers.sort(reverse=True)  # Descending order
```

```python
numbers = [2, 5, 3.14, 1, -7]
numbers.sort()
print(numbers) # [-7, 1, 2, 3.14, 5]

furniture = ['table', 'chair', 'rack', 'shelf']
furniture.sort()
print(furniture) # ['chair', 'rack', 'shelf', 'table']
```

You can also pass `True` for the `reverse` keyword argument to have `sort()` sort the values in reverse order:

```python
furniture.sort(reverse=True)
print(furniture) # ['table', 'shelf', 'rack', 'chair']
```

If you need to sort the values in regular alphabetical order, pass `str.lower` for the key keyword argument in the sort() method call:

```python
letters = ['a', 'z', 'A', 'Z']
letters.sort(key=str.lower)
print(letters) # ['a', 'A', 'z', 'Z']
```

#### Create a new sorted array with the `sorted()` function

[Real Python - How to use sorted() and sort() in Python](https://realpython.com/python-sort/)

You can use the built-in function `sorted` to return a new sorted list:

```python
li = ['a', 'x', 'b', 'c', 'd', 'e', 'd']

# create a new sorted list based on "li"
li2_sorted = sorted(li)
print(li)         # ['a', 'x', 'b', 'c', 'd', 'e', 'd']
print(li2_sorted) # ['a', 'b', 'c', 'd', 'd', 'e', 'x']

furniture = ['table', 'chair', 'rack', 'shelf']
sorted(furniture) # ['chair', 'rack', 'shelf', 'table']
```

One of the most powerful components of `sorted()` is the keyword argument called `key`.

The `key` argument expects a function to be passed to it, and that function will be used on each value in the list being sorted to determine the resulting order.

```python
# Sort the list based on string length
words = ['banana', 'pie', 'Washington', 'book']
sorted(words, key=len) # ['pie', 'book', 'banana', 'Washington']

names_with_case = ['harry', 'Suzy', 'al', 'Mark']
sorted(names_with_case) # ['Mark', 'Suzy', 'al', 'harry']

# Sort based on string and whether they are all lower case
sorted(names_with_case, key=str.lower)
# ['al', 'harry', 'Mark', 'Suzy']

# List Sorting (based on 2nd value of each tuple)
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1])
print(a)
```

### Reverse a list w/ reverse()

Either use slices w/ a negative step or the `.reverse()` method to reverse a list

```python
fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits)  # ['cherry', 'banana', 'apple']

# NOTE: Can also use list slicing to reverse a list
# This actually creates a new list
reversed = fruits[::-1]
```

```python
li = [1, 2, 3]

# Create new list which is the reverse of the original via slices
li_reversed = li[::-1]
print(li_reversed) # [3, 2, 1]
```

**CAUTION:** `reverse()` acts on the original list!

- The `reverse()` method acts on the original list it was called against.

```python
li = [1, 2, 3]

# Since the reverse method is invoked on "li"
# What actually happense here is that we reverse "li"
# AND we create a new variable which also points to the reversed "li" list
li_reversed = li.reverse()
print(li_reversed) # [3, 2, 1]
print(li) # [3, 2, 1]
```

### Check how many times a value occurs in the list w/ count()

```python
li = ["a", "b", "c", "d", "e", "a"]

print(li.count("a")) # 2
print(li.count("c")) # 1
print(li.count("z")) # 0
```

### Checking if a value is in a list with _in_ and _not in_ keywords

```python
# Use the `in` keywords to evaluate if specified value is in the list
'rack' in ['table', 'chair', 'rack', 'shelf'] # True
'bed' in ['table', 'chair', 'rack', 'shelf'] # False

# Use the `not in` keywords to evaluate if specified value is not in the list
'bed' not in furniture # True
'rack' not in furniture # False
```

### Find min and max values of a list

```python
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(min(a)) # "bar"
print(max(a)) # "qux"

b = [5, 2, 1, 3, 4]
print(min(b)) # 1
print(max(b)) # 5
```

### De-duplicating a list

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

### Create a new list using the `range()` and `list()` functions

`range(start, stop)` creates a comma-separated range of values starting at `start` and ending right before `stop` (`stop - 1`)

```python
li = list(range(1, 5))
print(li) # [1, 2, 3, 4]
```

### Join values in a list together into a string

```python
# Take the values inside the array and join them together
# via the string which is invoking join (empty space in this ex.)
new_sentence = " ".join(['hi', 'my', 'name', 'is', 'Bilbo'])

print(new_sentence) # 'hi my name is JOJO'
```

## List Unpacking

- `List unpacking` is a shortcut that lets you assign multiple variables with the values in a list in one line of code.
- `List unpacking` in Python is similar to array destructuring in JavaScript

```python
# Use list unpacking to assign new variables to specific values in the list
a, b, c = [1, 2, 3]

print(a) # 1
print(b) # 2
print(c) # 3
```

```python
# Traditional way of assigning values from a list
furniture = ['table', 'chair', 'rack', 'shelf']
table = furniture[0]
chair = furniture[1]
rack = furniture[2]
shelf = furniture[3]

# List Unpacking
furniture = ['table', 'chair', 'rack', 'shelf']
table, chair, rack, shelf = furniture

print(table) # 'table'
print(chair) # 'chair'
print(rack)  # 'rack'
print(shelf) # 'shelf'
```

We can also use `list unpacking` to assign a sub-list to the remainder of values

```python
# Ex 1
a, b, c, *other = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)     # 1
print(b)     # 2
print(c)     # 3
print(other) # [4, 5, 6, 7, 8, 9]

# Ex 2
a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)     # 1
print(b)     # 2
print(c)     # 3
print(other) # [4, 5, 6, 7, 8]
print(d)     # 9

# Ex 3
first, *middle, last = [1, 2, 3, 4, 5]
print(first)   # Outputs: 1
print(middle)  # Outputs: [2, 3, 4]
print(last)    # Outputs: 5
```

`list unpacking` can also be used to swap the values in two variables:

```python
# Initialize a and b variables
a, b = 'table', 'chair'

print(a) # table
print(b) # chair

# Swap values of a and b
a, b = b, a

print(a) # chair
print(b) # table
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

## List Comprehensions

[List Comprehensions](python_comprehensions.md#basic-list-comprehension-steps)

## Resources / References

- [RealPython - Python's list Data Type: A Deep Dive w/ Examples](https://realpython.com/python-list/)
- [Python Cheatsheet - Lists and Tuples](https://www.pythoncheatsheet.org/cheatsheet/lists-and-tuples)
- [Real Python - Lists and Tuples in Python](https://realpython.com/python-lists-tuples/#defining-and-using-tuples)
- [Real Python - Slice assignment](https://realpython.com/python-assignment-operator/#updating-lists-through-indices-and-slices)
- [Real Python - How to use sorted() and sort() in Python](https://realpython.com/python-sort/)
- [Programiz - Python List index](https://www.programiz.com/python-programming/methods/list/index)
