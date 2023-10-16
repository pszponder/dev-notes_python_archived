# Loops in Python

## For Loop

```python
"""
For Loop with range()

- The range() function returns a sequence of numbers,
and is commonly used to repeat a loop a specific number of times

range([start], stop, [step])
- start -- Value of the start parameter (inclusive). Defaults to 0
- stop -- Value of the stop parameter (exclusive)
- step -- The step size or increment value. Defaults to 1
"""

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

## While Loop

The `while` loop repeats a block of code as long as its condition is `True`

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

## Loop Control Statements

- `break` -- exists the loop prematurely
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

`list comprehensions` provide a way to create lists based on existing iterables.

```python
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]
print(squares)  # [1, 4, 9, 16, 25]
```

`set comprehensions` and `dictionary comprehensions` can also be used to create sets and dictionaries

```python
numbers = [1, 2, 3, 4, 5]
squares_set = {n**2 for n in numbers}

mapping = {n: n**2 for n in numbers}
```

## Enumerate

Use the `enumerate()` function when you need both the index and the value from an iterable.

```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
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

You can use a for loop to iterate over keys, values, or key-value pairs in dictionaries

```python
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
