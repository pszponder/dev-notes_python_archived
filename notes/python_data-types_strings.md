# Strings in Python

## Strings Intro

In Python, strings can be defined using single or double quotes

```python
my_string1 = "hello world, this is a string"
my_string2 = 'this is also a string'
```

**CAUTION:** Python Strings are Immutable

- Once a string is defined, it cannot be changed (immutable)
- To change the string value assigned to a variable, you must reassign the value of the variable.

## Triple Quoted Strings

Triple quotes allow for multi-line strings

```python
'''
This multi-line string
uses a set of 3 single quotes
'''

"""
We can also create a multi-line string
using a set of 3 double quotes
"""
```

## String Concatenation

We can use the `+` operator to concatenate two or more strings together

```python
first_name = "john"
last_name = "doe"
full_name = first_name + " " + last_name # john doe
```

**NOTE:** Use `f-strings` over string concatenation

- Python3 introduced `f-strings` which are much better and easier to use than string concatenation

## Formatting Strings

### Converting a Value to a String

Use the `str()` function to convert a non-string value to a string

```python
age = 40
age_as_str = str(age)
```

### Formatted Strings (f-strings)

[Real Python: f-string guide](https://realpython.com/python-f-strings/)

What are `f-strings`?

- `f-strings` are an easy way to generate strings that contain interpolated expressions.
- Any code between curly braces `{}` will be evaluated and then the result will be turned into a string and inserted into the overall string.
- This is the same as JavaScript's String Literals

```python
# Below evaluates to "there are 85400 seconds in a day"
f"there are {24*60*60} seconds in a day"
```

```python
age = input("How old are you (in years)? ")
days = float(age) * 365
print(f"{age} years is {days} days old")
```

```python
first_name = "Legolas"
last_name = "Greenleaf"
print(f"Hello {first_name} {last_name}")
```

You can also use create an f-string out of triple quoted strings:

```python
f_string = f'''
This multi-line string
contains some math in it:
2 + 2 = { 2 + 2}
'''

print(f_string)
```

### The format() method

Use the `format()` method to replace a set of curly braces in a string with a value(s)

```python
age = 123
age_string = "You are {} years old".format(number)
print(number_string) # You are 123 years old
```

## String Multiplication

Can multiply a string by a number to create a longer repeating string

```python
"hello" * 3 # Results in "hellohellohello"
```

## String Indexing

Strings are ordered and indexed.

**NOTE:** Indices start at `0` in Python

```python
# Define a string
msg = "I <3 Cats"

# Access the character at index 0 of msg
msg[0] # 'I'

# Access the character at index 5 of msg
msg[5] # 'C'
```

**NOTE:** Python Indexing w/ Negative Indices

- Can use negative indices in Python to access characters of a string starting at the end of the string.
- The last character of a string is at index `-1`

```python
movie = "Chicken Run"

# Access the -2 index
movie[-2] # u
```

## String Slices (extract sub-strings)

What are slices?

- Slices allow you to access and extract a portion of a string/array (a sub-string / sub-array)
- `string[start_idx:end_idx:step]`
- The slice starts at `start_idx` and goes up to (but not including) `end_idx`
- `step` is optional

```python
msg = "I <3 Cats"

# Access a slice of a string starting from index 2
# and up to (but not including) the charachter at index 6
msg[2:6] # "<3 C"

animal = "catdog"
animal[2:4] # "td"
animal[3:6] # "dog"

# Select a sub-string starting at specified index,
# all the way to the end of the string
animal[3:] # "dog"

# Select a sub-string starting from the beginning of the string,
# up to specified index
animal[:3] # "cat"

phone1 = "(310) 448 8712"
phone2 = "(212) 696 9912"

area_code1 = phone1[1:4]
area_code2 = phone2[1:4]

# Slices with a Step
msg[2:8:2] # '< a'
```

Can use negative steps to go backwards / reverse the string

```python
numbers = "0123456789"

# Reverse the string
numbers[::-1] # "9876543210"
```

## Escape Characters / Escape Sequences

- Newline => `\n`
- Tab => `\t`
- Double Quote => `\"`
- Single Quote => `\'`
- Backslash => `\\`

## String Functions / Methods

[Python String Methods](https://www.w3schools.com/python/python_ref_string.asp)

### Find the length of a string using the len() function

`len()` evaluates to the integer value of the number of characters in a string, list, dictionary, etc.:

```python
>>> len('hello')
# 5

>>> len(['cat', 3, 'dog'])
# 3
```

### Test of Emptiness

Test of emptiness of strings, lists, dictionaries, etc., should not use `len`, but prefer direct boolean evaluation.

Test of emptiness example:

```python
>>> a = [1, 2, 3]

# bad
>>> if len(a) > 0:  # evaluates to True
...     print("the list is not empty!")
...
# the list is not empty!

# good
>>> if a: # evaluates to True
...     print("the list is not empty!")
...
# the list is not empty!
```

### Uppercase / Lowercase / Capitalize strings

- Use the `upper()` method to turn a string all uppercase
- Use the `lower()` method to turn an uppercase string to lowercase
- Use the `capitalize()` method to capitalize a string

```python
my_string = "hEllO WoRld"

my_string.upper() # "HELLO WORLD"
my_string.lower() # "hello world"
my_string.capitalize() # "Hello world"
```

### Find the index of the 1st occurrence of sub-string or character

- The `find()` method finds the first occurrence of the specified value.
- The `find()` method returns -1 if the value is not found.
- The `find()` method is almost the same as the `index()` method, the only difference is that the `index()` method raises an exception if the value is not found.

```python
quote = "to be or not to be"
quote.find("be") # 3
```

### Checking if a character or sub-string is in a string with `in` and `not in` keywords

```python
str1 = "hello goodbye"

print("hello" in str1) # True
print("o" in str1)     # True
print("bye" in str1)   # True
print("hi" in str1)    # False

print("hi" not in str1)    # True
print("hello" not in str1) # False
```

### Replace all occurrences of a sub-string or character

```python
quote = "to be or not to be"
quote.replace("be", "replace") # "to replace or not to replace"
```

### Join values in a list together into a string with `join()`

[Join values in a list together into a string](python_data-types_lists.md#join-values-in-a-list-together-into-a-string)

### Additional Common String Methods

- `join()`
- `lstrip()`
- `removeprefix()`
- `removesuffix()`
- `rfind()`
- `rindex()`
- `rjust()`
- `split()`
- `startswith()`
- `endswith()`
- `strip()`
- `swapcase()`
- `title()`

## References

- [Real Python: f-string guide](https://realpython.com/python-f-strings/)
- [Python String Methods](https://www.w3schools.com/python/python_ref_string.asp)
