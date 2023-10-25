# Python Comprehensions

Comprehension allows us to create powerful functionality within a single line of code.

## Using List Comprehensions to create a list

List comprehensions are a concise and readable way to create lists in Python. They are often used to transform one list (or any iterable) into another list by applying an expression to each element in the sequence or by filtering elements based on some condition.

The basic syntax for a list comprehension is:

```python
[expression for member in iterable if condition]
```

- `expression` is the current item in the iteration, but it can be transformed or changed.
- `member` represents the member elements in the iterable.
- `iterable` is a sequence, collection, or any other object that can return its elements one at a time.
- `condition` is like a filter that only accepts the items that evaluate to `True`.
  - **NOTE:** `if <condition>` is optional, you don't need to use it if you don't want to filter the data

## Basic List Comprehension Steps:

```txt
new_list = [<expression> for <member> in <iterable>]
```

Every list comprehension in Python includes three elements:

1. **`expression`** is the member itself, a call to a method, or any other valid expression that returns a value.
2. **`member`** is the object or value in the list or iterable.
3. **`iterable`** is a list, [set](https://realpython.com/python-sets/), sequence, [generator](https://realpython.com/introduction-to-python-generators/), or any other object that can return its elements one at a time.

```python
# Use list comprehension to turn string into a list of characters
chars = [char for char in 'hello']
print(chars) # ['h', 'e', 'l', 'l', 'o']

# =========================
# Above is equivalent to...
# =========================

# Instantiate an empty list
chars2 = []

for char in 'hello':
    chars2.append(char)

print(chars2) # ['h', 'e', 'l', 'l', 'o']
```

```python
# Create a list of numbers using list comprehension
nums = [num for num in range(0, 5)]
print(nums) # [0, 1, 2, 3, 4]
```

```python
# Using list comprehension to create a list of squares
squares = [i * i for i in range(10)]
squares # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# =========================
# Above is equivalent to...
# =========================

# Instantiate an empty list
squares = []

for i in range(10):
    squares.append(i * i)

print(squares) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

Because the **expression** requirement is so flexible, a list comprehension in Python works well in many places where you would use `map()`.

```python
tax_nums = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = .08

# Define a function which perform a computation on a single item
def get_price_with_tax(txn):
    return txn * (1 + TAX_RATE)

final_prices = [get_price_with_tax(i) for i in tax_nums]
print(final_prices)
# [1.1772000000000002, 25.4448, 62.467200000000005, 4.9248, 7.322400000000001]
```

**NOTE:** Other ways to create lists in python

- [Using Loops](python_comprehensions.md#creating-python-lists-using-for-loops)
- [Using the map() function](python_comprehensions.md#creating-python-lists-using-map-objects)

## Convert for loop to a list comprehension

```python
# =======================================
# EXAMPLE 1: Print all elements in a list
# =======================================
fruits = ["apples", "bananas", "strawberries"]

# using for loop
for fruit in fruits:
    print(fruit)

# using list comprehension
[ print(fruit) for fruit in fruits ]

# ===========================================
# EXAMPLE 2: Uppercase all values of the list
# ===========================================

fruits = ["apples", "bananas", "strawberries"]

# using for loop
new_fruits = []
for fruit in fruits:
    fruit.upper()
    new_fruits.append(fruit)
furit = new_fruits # reassign original fruit to new_fruits

# using list comprehension
fruits = [ fruit.upper() for fruit in fruits ]
```

## Adding Conditional Logic to List Comprehensions

### Filtering

The most common way to add [conditional logic](https://realpython.com/python-conditional-statements/) to a list comprehension is to add a conditional to the end of the expression:

```txt
new_list = [
    <expression> for <member> in <iterable>
    (if <conditional>)
]
```

By adding conditional logic to the list comprehension, we can use list comprehension to filter a list

```python
# create a list of only even numbers
evens = [num for num in range(0, 5) if num % 2 == 0]
print(evens) # [0, 2, 4]
```

```python
# Create a list of squares for even numbers from 0 to 9:
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # Outputs: [0, 4, 16, 36, 64]
```

```python
sentence = 'the rocket came back from mars'

# Create a new list with each character in the string
#  but only add the character if it is a vowel
vowels = [i for i in sentence if i in 'aeiou']

print(vowels) # ['e', 'o', 'e', 'a', 'e', 'a', 'o', 'a']
```

```python
# More complicated example of using list comprehension to filter

sentence = 'The rocket, who was named Ted, came back from Mars because he missed his friends.'

# method used to return boolean based on logic
def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels

consonants = [i for i in sentence if is_consonant(i)]
# ['T', 'h', 'r', 'c', 'k', 't', 'w', 'h', 'w', 's', 'n', 'm', 'd', 'T', 'd', 'c', 'm', 'b', 'c', 'k', 'f', 'r', 'm', 'M', 'r', 's', 'b', 'c', 's', 'h', 'm', 's', 's', 'd', 'h', 's', 'f', 'r', 'n', 'd', 's']
```

### Using if / else if / else

You can place the conditional at the end of the statement for simple filtering, but what if you want to *change* a member value instead of filtering it out? In this case, it’s useful to place the conditional near the *beginning* of the expression:

```txt
new_list = [
    <expression> if <conditional>  # if statement
    (else <action> <condition>)    # else if statement
    (else <expression>)            # else statement
    for <member> in <iterable>     # iteration
]
```

With this formula, you can use conditional logic to select from multiple possible output options.

```python
# in new_bits list, replace every instance of False to 0
#  and every instance of True to 1

# ============================================================
# Using standard for + if/else statement:
# ============================================================
bits = [False, True, False, False, True, False, False, True]
new_bits = []

for b in bits:
    if b == True:
        new_bits.append(1)
    else:
        new_bits.append(0)

# =========================
# Using list comprehensions
# =========================
new_bits = [ 1 if b == True else 0 for b in bits ]

# Breaking down into multiple lines (for readability)
new_bits = [
    1 if b == True
    else 0
    for b in bits
]
```

```python
original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]

# Use list comprehension to output i if its value is > 0
#  otherwise, output 0 in the new list
prices = [i if i > 0 else 0 for i in original_prices]

print(prices) # [1.25, 0, 10.22, 3.78, 0, 1.16]
```

```python
# Alternative to above example
def get_price(price):
    return price if price > 0 else 0

prices = [get_price(i) for i in original_prices]

print(prices) # [1.25, 0, 10.22, 3.78, 0, 1.16]
```

```python
# USING MULTIPLE CONDITIONS:

# Create a list of numbers between 0 to 20 that are both divisible by 2 and 3:
multiples = [x for x in range(21) if x % 2 == 0 if x % 3 == 0]
print(multiples)  # Outputs: [0, 6, 12, 18]
```

```python
# Create a list that labels numbers as "even" or "odd":
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(labels)  # Outputs: ['even', 'odd', 'even', 'odd', 'even']
```

## String manipulation using Comprehension

```python
# ======================================================
# Break the Pascal-case string into its individual words
# ======================================================
my_string = "HelloMyNameIsBob"

# 1. Join together all characters (unless there is space)
# 2. If the current char is lowercase, add it to the new array
# 3. If current char is uppercase, prepend space in front of it
#    then add it to the new array
# 4. Slice the array to avoid capturing 1st empty space in array
my_arr = "".join(
    [
        i if i.islower()
        else " " + i
        for i in my_string
    ][1:] # slice my_arr so 1st char (empty space) isn't included
)
```

## Nested List Comprehension

```python
# Flatten a matrix into a single list:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [num for row in matrix for num in row]
print(flat_list)  # Outputs: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Set Comprehensions

A **set comprehension** is almost exactly the same as a list comprehension in Python. The difference is that set comprehensions make sure the output contains no duplicates.

You can create a set comprehension by using curly braces instead of brackets:

```python
quote = "life, uh, finds a way"

# Create a new set which contains characters from string
#  which are vowels (and are not already in the set)
unique_vowels = {i for i in quote if i in 'aeiou'}

print(unique_vowels) # {'a', 'e', 'u', 'i'}
```

## Dictionary Comprehensions

Dictionary comprehensions are also very similar to list and set comprehensions, except they also require a key

```python
# Syntax for Dictionary Comprehensions
my_dict = {key_expr: value_expr for item in iterable}
```

```python
squares = {i: i * i for i in range(10)}

print(squares)
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
```

```python
simple_dict = {
    'a': 1,
    'b': 2
}

my_dict = { key: value ** 2 for key, value in simple_dict.items()}

print(my_dict) # { 'a': 1, 'b': 4}
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

## References

- [Real Python - When to use a List Comprehension in Python](https://realpython.com/list-comprehension-python/)

## Appendix

### Creating Python Lists Using for loops

The most common type of loop is the [`for`](https://realpython.com/courses/python-for-loop/) loop. You can use a `for` loop to create a list of elements in three steps:

1. Instantiate an empty list.
2. Loop over an iterable or [range](https://realpython.com/python-range/) of elements.
3. [Append](https://realpython.com/python-append/) each element to the end of the list.

```python
# Instantiate an empty list
squares = []

# Iterate over an iterable,
#  perform a computation,
#  & push result into the empty list
for i in range(10):
    squares.append(i * i)

print(squares) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### Creating Python Lists Using map() Objects

[`map()`](https://realpython.com/python-map-function/) provides an alternative approach that’s based in [functional programming](https://realpython.com/python-functional-programming/). You pass in a function and an iterable, and `map()` will create an object. This object contains the output you would get from running each iterable element through the supplied function.

```python
txns = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = .08

# Define a function which perform a computation on a single item
def get_price_with_tax(txn):
    return txn * (1 + TAX_RATE)

# Apply the function to each item in the list via the map function
# this returns an iterator (think of it as a map object)
final_prices = map(get_price_with_tax, txns)

# Convert the map object / iterator to a list
list(final_prices)
# [1.1772000000000002, 25.4448, 62.467200000000005, 4.9248, 7.322400000000001]
```
