# Loops in Python

## For Loop

```python
# For Loop Syntax
for <var> in <iterable>:
    <statement(s)>
```

The `for` loop can be used to iterate over any iterable type (`string`, `list`, `tuple`, `dictionary`, or `set`):

```python
# Print each character in the string
for item in 'Zero to Mastery':
    print(item)

# Print each element in the list
for item in [1, 2, 3, 4, 5]:
    print(item)

# Print each item in the tuple
for item in (1, 2, 3, 4, 5):
    print(item)

# Print each item in the set
for item in {1, 2, 3, 4, 5}:
    print(item)
```

### Using the range() function to create iterables

The `range()` function returns a sequence of numbers, and is commonly used to repeat a loop a specific number of times.

`range([start], stop, [step])`

- `start` -- Value of the start parameter (inclusive). Defaults to 0
- `stop` -- Value of the stop parameter (exclusive)
- `step` -- The step size or increment value. Defaults to 1

```python
for i in range(5):
    print(i)
# Outputs: 0 1 2 3 4

for i in range(2, 8):
    print(i)
# Outputs: 2 3 4 5 6 7

for i in range(0, 10, 2):
    print(i)
# Outputs: 0 2 4 6 8

# You can use negative values to loop in reverse
for i in range(5, -1, -1):
    print(i)
# Outputs: 5 4 3 2 1 0

```

```python
"""
For Loop with Iterables

The for loop can iterate over any iterable object,
lists, tuples, strings, etc.
"""

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

```python
"""
Can nest for loops inside one or another
"""

for i in range(3):      # Outer Loop
    for j in range(3):  # Inner Loop
        print(i, j)
```

### for-else

This allows to specify a statement to execute in case of the full loop has been executed. Only
useful when a `break` condition can occur in the loop:

```python
for i in [1, 2, 3, 4, 5]:
   if i == 3:
       break
else:
   print("only executed when no item is equal to 3")
```

### For Loop Examples

```python
# Exercise
# Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

# Iterate through each sub-list in picture
for i in range(0, len(picture)):
    row = "" # Initialize an empty string for each row of picture
    # Iterate through each element of the current sub-list
    for j in range(0, len(picture[i])):
        # Determine if current value should be " " or "*"
        if picture[i][j] == 0:
            row += " "
        else:
            row += "*"
    print(row)

#    *
#   ***
#  *****
# *******
#    *
#    *

# Alternative solution
for row in picture:
    for pixel in row:
        if pixel:
            print("*", end="")
        else:
            print(" ", end="")
    print("")
```

```python
# SOLUTION 1:
# Print out a list containing the duplicate values in the list
li= ["a", "b", "c", "b", "d", "m", "n", "n"]
dups = []

# Iterate through the list
for ptr1 in range(0, len(li)):
    # Iterate through the list again but start at ptr1 + 1
    for ptr2 in range(ptr1 + 1, len(li)):
        # If both pointers point to the same value,
        # append that value to dups list and break out of inner-loop
        # this will cause ptr1 and ptr2 to advance
        if (li[ptr1] == li[ptr2]):
            dups.append(li[ptr1])
            break
print(dups) # ["b", "n"]

# SOLUTION 2:
# Iterate through each value in the list
for value in li:
    # Check how many times the current value appears in the list
    if li.count(value) > 1:
        # If the value is not already in the list, append it to dups
        if value not in dups:
            dups.append(value)
print(dups) # ["b", "n"]
```

## While Loop

The `while` loop repeats a block of code as long as its condition is `True`

```python
while <condition>:
    # loop logic
```

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

```python
spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam + 1

# Hello, world.
# Hello, world.
# Hello, world.
# Hello, world.
# Hello, world.
```

```python
while True:
    response = input('say something: ')
    if (response == "bye"):
        break
```

### while-else

You can add an `else` clause to a while loop which will run once when the while loop's condition evaluates to `False`.

```python
i = 0

while i < 5:
    print(i)
    i += 1
else:
    print('done with all the work')

# 0
# 1
# 2
# 3
# 4
# "done with all the work"
```

## Loop Control Statements

- `break` -- immediately exits the enclosing loops
- `continue` -- skips the remainder of the current iteration and continues with the next one
- `pass` -- does nothing, acts as a placeholder

```python
for num in range(10):
    if num == 5:
        break
    elif num == 8:
        continue
    print(num)
```

## Comprehensions

[Comprehensions](python_comprehensions.md) provide a way to create lists based on existing iterables.

## Enumerate

When you use `enumerate()`, the function gives you back *two* loop variables:

1. The **count / index** of the current iteration
2. The **value** of the item at the current iteration

```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
```

```python
values = ["a", "b", "c"]

# Iterate over each value
for idx, value in enumerate(values):
    print(idx, value)

# 0 a
# 1 b
# 2 c
```

```python
# Use enumerate to iterate over a string
for i, char in enumerate("hello"):
    print(i, char)

# 0 h
# 1 e
# 2 l
# 3 l
# 4 o
```

## Iterate over Iterables (Lists, Tuples, Strings, etc.)

```python
"""
For Loop with Iterables

The for loop can iterate over any iterable object,
lists, tuples, strings, etc.
"""

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

## Iterate over Dictionaries

[Real Python - How to iterate through a dictionary in python](https://realpython.com/iterate-through-dictionary-python/)

You can use a for loop to iterate over keys, values, or key-value pairs in dictionaries

```python
"""
SUMMARY OF DICTIONARY ITERATION
"""
data = {"a": 1, "b": 2, "c": 3}

# Keys
for key in data:
    print(key)

# Values
for value in data.values():
    print(value)

# Key-Value pairs
for key, value in data.items():
    print(key, value)
```

### Return a list of keys in a dictionary with keys()

The `keys()` method returns a list of all **keys** in the dictionary:

```python
wizard_dict = {
    "name": "Gandalf",
    "age": 500,
    "inventory": ["staff", "pipe", "sword"]
}

print(wizard_dict.keys()) # ["name", "age", "inventory"]

# Iterate through the keys of the dictionary
for key in wizard_dict.keys():
    print(key)

# name
# age
# inventory
```

**NOTE:** There is actually no need to use **.keys()** since by default you will loop through keys:

```python
wizard_dict = {
    "name": "Gandalf",
    "age": 500,
    "inventory": ["staff", "pipe", "sword"]
}

# Iterate through the values of the dictionary
for key in wizard_dict:
    print(key)

# name
# age
# inventory
```

### Return a list of values in the dictionary with values()

The `values()` method returns a list of the **values** of the dictionary:

```python
wizard_dict = {
    "name": "Gandalf",
    "age": 500,
    "inventory": ["staff", "pipe", "sword"]
}

print(wizard_dict.values())
# ["Gandalf", 500, ["staff, "pipe", "sword"]]

# Iterate through the values of the dictionary
for value in wizard_dict.values():
    print(value)

# Gandalf
# 500
# ['staff', 'pipe', 'sword']
```

### Return a list of key-value pairs in a dictionary with items()

The `items()` method returns a list of tuples containing the key-value pairs in the dictionary.

The first item in each tuple is the key, and the second item is the key’s value:

```python
wizard_dict = {
    "name": "Gandalf",
    "age": 500,
    "inventory": ["staff", "pipe", "sword"]
}

print(wizard_dict.items())
"""
[
    ('name', 'Gandalf'),
    ('age', 500),
    ('inventory', ['staff', 'pipe', 'sword'])
]
"""

# Iterate through key-value pairs as tuples
for item in wizard_dict.items():
    print(item)

# ('name', 'Gandalf')
# ('age', 500)
# ('inventory', ['staff', 'pipe', 'sword'])
```

Using the `keys()`, `values()`, and `items()` methods, a for loop can iterate over the keys, values, or key-value pairs in a dictionary, respectively.

```python
wizard_dict = {
    "name": "Gandalf",
    "age": 500,
    "inventory": ["staff", "pipe", "sword"]
}

# Iterate through key-value pairs as individual values
for key, value in wizard_dict.items():
    print(f"Key: {key} => Value: {value}")

# Key: name => Value: Gandalf
# Key: age => Value: 500
# Key: inventory => Value: ['staff', 'pipe', 'sword']
```

## Iterating in Parallel w/ zip

Use the `zip()` function to iterate over two or more lists in parallel

```python
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

for name, score in zip(names, scores):
    print(name, score)
```

## Creating and Using Custom Iterators

- Manually create iterators using `iter()`
- Use `next()` to fetch the next item from the iterator

```python
numbers = [1, 2, 3]
iterator = iter(numbers)

print(next(iterator))  # 1
print(next(iterator))  # 2
```

## Resources / References

- [Real Python - Using the Python zip() function for Parallel Iteration](https://realpython.com/python-zip-function/)
- [Python Cheat Sheet - Control Flow](https://www.pythoncheatsheet.org/cheatsheet/control-flow)
- [Real Python - How to iterate through a dictionary in python](https://realpython.com/iterate-through-dictionary-python/)
- [Real Python - Python enumerate(): Simplify looping with counters](https://realpython.com/python-enumerate/)
- [Real Python - Python "for" Loops (Definite Iteration)](https://realpython.com/python-for-loop/)
