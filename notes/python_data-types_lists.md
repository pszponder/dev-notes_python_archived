# Python Lists

A `list` is an ordered collection of items, which can be of any type

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

## Get the length of a list

Use the `len(<list>)` function to get the length of a passed in list

```python
fruits = ["apple", "banana", "cherry"]

length = len(fruits)
print(length)  # 3
```

## Concatenating lists

```python
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]

combined = list1 + list2
print(combined)  # [1, 2, 3, 'a', 'b', 'c']
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

## Common List Methods

**NOTE:** Assume each example below starts with the following list:

```python
fruits = ["apple", "banana", "cherry"]
```

### Add elements to the end of the list w/ append()

```python
fruits.append("grape")
print(fruits)  # ['apple', 'banana', 'cherry', 'grape']
```

### Add elements from another list or iterable w/ extend()

```python
fruits.extend(["kiwi", "orange"])
print(fruits)  # ['apple', 'banana', 'cherry', 'kiwi', 'orange']
```

### Add an element to a specific index position w/ insert()

```python
fruits.insert(1, "blueberry")  # Inserts "blueberry" at position 1
print(fruits)  # ['apple', 'blueberry', 'banana', 'cherry']
```

### Remove the first item with the specified value w/ remove()

```python
fruits.remove("banana")
print(fruits)  # ['apple', 'cherry']
```

### Remove element at specified position, or last item of the index w/ pop()

```python
fruits.pop()         # Removes the last item
fruits.pop(1)        # Removes the item at position 1
```

### Remove all items from the list w/ clear()

```python
fruits.clear()
print(fruits)  # []
```

### Return the index of the 1st item w/ specified value w/ index()

```python
idx = fruits.index("cherry")
print(idx)  # 2
```

### Return the number of times a value appears in a list w/ count()

```python
count = fruits.count("apple")
print(count)  # 1
```

### Sort a list in place w/ sort()

```python
numbers.sort()        # Ascending order
numbers.sort(reverse=True)  # Descending order
```

### Reverse a list w/ reverse()

```python
fruits.reverse()
print(fruits)  # ['cherry', 'banana', 'apple']

# NOTE: Can also use list slicing to reverse a list
# This actually creates a new list
reversed = fruits[::-1]
```

### Shallow Copy w/ copy()

```python
new_fruits = fruits.copy()
print(fruits)  # ['apple', 'banana', 'cherry']
```

### Deep Copy w/ copy.deepcopy

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

## List Unpacking

You can unpack sequences (such as lists or tuples) into variables using a similar syntax to JavaScript's array unpacking.

```python
x, y, z = [4, 5, 6]
print(x)  # Outputs: 4
print(y)  # Outputs: 5
print(z)  # Outputs: 6
```

You can also use the `*` syntax to capture multiple items.

```python
first, *middle, last = [1, 2, 3, 4, 5]
print(first)   # Outputs: 1
print(middle)  # Outputs: [2, 3, 4]
print(last)    # Outputs: 5
```

## List Comprehensions

List comprehensions are a concise and readable way to create lists in Python. They are often used to transform one list (or any iterable) into another list by applying an expression to each element in the sequence or by filtering elements based on some condition.

The basic syntax for a list comprehension is:

```python
[expression for item in iterable if condition]
```

- `expression` is the current item in the iteration, but it can be transformed or changed.
- `item` represents the member elements in the iterable.
- `iterable` is a sequence, collection, or any other object that can return its elements one at a time.
- `condition` is like a filter that only accepts the items that evaluate to `True`.

### List Comprehension Examples:

1. **Simple Transformation**:
   Create a list of squares for numbers from 0 to 9:

   ```python
   squares = [x**2 for x in range(10)]
   print(squares)  # Outputs: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
   ```

2. **Using a Condition**:
   Create a list of squares for even numbers from 0 to 9:

   ```python
   even_squares = [x**2 for x in range(10) if x % 2 == 0]
   print(even_squares)  # Outputs: [0, 4, 16, 36, 64]
   ```

3. **Nested List Comprehension**:
   Flatten a matrix into a single list:

   ```python
   matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
   flat_list = [num for row in matrix for num in row]
   print(flat_list)  # Outputs: [1, 2, 3, 4, 5, 6, 7, 8, 9]
   ```

4. **Using Multiple Conditions**:
   Create a list of numbers between 0 to 20 that are both divisible by 2 and 3:

   ```python
   multiples = [x for x in range(21) if x % 2 == 0 if x % 3 == 0]
   print(multiples)  # Outputs: [0, 6, 12, 18]
   ```

5. **Using `if-else` within the Expression**:
   Create a list that labels numbers as "even" or "odd":

   ```python
   labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
   print(labels)  # Outputs: ['even', 'odd', 'even', 'odd', 'even']
   ```

## Resources / References

- [RealPython - Python's list Data Type: A Deep Dive w/ Examples](https://realpython.com/python-list/)
- [RealPython - Lists and Tuples in Python](https://realpython.com/python-lists-tuples/)
