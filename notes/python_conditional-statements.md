# Conditional Statements in Python

## Logical and Comparison Operators

### Conditional Operators

Python supports the usual logical conditions from mathematics:

| Operator | Meaning                  |
| -------- | ------------------------ |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `<`      | Less than                |
| `>`      | Greater Than             |
| `<=`     | Less than or Equal to    |
| `>=`     | Greater than or Equal to |

### Boolean Operators

There are three Boolean operators: `and`, `or`, and `not`.

The `and` Operator’s _Truth_ Table:

| Expression        | Evaluates to |
| ----------------- | ------------ |
| `True and True`   | `True`       |
| `True and False`  | `False`      |
| `False and True`  | `False`      |
| `False and False` | `False`      |

The `or` Operator’s _Truth_ Table:

| Expression       | Evaluates to |
| ---------------- | ------------ |
| `True or True`   | `True`       |
| `True or False`  | `True`       |
| `False or True`  | `True`       |
| `False or False` | `False`      |

The `not` Operator’s _Truth_ Table:

| Expression  | Evaluates to |
| ----------- | ------------ |
| `not True`  | `False`      |
| `not False` | `True`       |

### Mixing Operators

You can mix boolean and comparison operators:

```python
(4 < 5) and (5 < 6) # True

(4 < 5) and (9 < 6) # False

(1 == 2) or (2 == 2) # True
```

Also, you can mix use multiple Boolean operators in an expression, along with the comparison operators:

```python
2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2 # True
```

### is vs ==

In Python `a == b`:

- Checks for equality of `a` and `b` are the same
- Types of `a` and `b` can be converted
- `==` is equivalent to `==` in JavaScript

In Python `is`:

- Checks for equality of `a` and `b`
- Checks if `a` and `b` are the same type
- If comparing two objects, then `a` and `b` must point to the same object in memory
- `is` is equivalent to `===` in JavaScript

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b) # True
print(a == c) # True
print(b == c) # True

print(a is b) # False
print(a is c) # True
print(b is c) # False
```

## Truthy vs Falsy Values in Python

All values in python are considered "truthy" except for the following, which are "falsy"

- `None`
- `False`
- `0`
- `0.0`
- `0j`
- `Decimal(0)`
- `Fraction(0, 1`
- `[]` - an empty `list`
- `{}` - an empty `dict`
- `()` - an empty `tuple`
- `set()` - an empty set
- `""` or `''` - an empty string
- `b''` or `b""` - an empty `bytes`
- an empty `range`, like `range(0)`
- objects for which
  - `obj.__bool__()` returns `False`
  - `obj.__len__()` returns `0`

## Conditional Statements

### if, elif, else

```python
if condition_1:
    # Code for condition 1
elif condition_2:
    # Code for condition 2
else:
    # Code if nothing else above triggered
```

```python
age = 18

if age < 20:
    print("You're a teenager!")
elif age == 20:
    print("You just hit 20!")
else:
    print("You're above 20!")
```

### Ternary Operator / Conditional Expression

Many programming languages have a ternary operator, which define a conditional expression.

The most common usage is to make a terse, simple conditional assignment statement.

In other words, it offers one-line code to evaluate the first expression if the condition is true, and otherwise it evaluates the second expression.

```python
condition_if_true if condition else condition_if_false
```

Example:

```python
age = 15

# this if statement:
if age < 18:
   print('kid')
else:
   print('adult')

# output: kid

# is equivalent to this ternary operator:
print('kid' if age < 18 else 'adult') # kid
```

Ternary operators can be chained:

```python
age = 15

# this ternary operator:
print('kid' if age < 13 else 'teen' if age < 18 else 'adult')

# is equivalent to this if statement:
if age < 18:
    if age < 13:
        print('kid')
    else:
        print('teen')
else:
    print('adult')

# output: teen
```

### Switch-Case Statement

In computer programming languages, a switch statement is a type of selection control mechanism used to allow the value of a variable or expression to change the control flow of program execution via search and map.

The _Switch-Case statements_, or **Structural Pattern Matching**, was firstly introduced in 2020 via [PEP 622](https://peps.python.org/pep-0622/), and then officially released with **Python 3.10** in September 2022.

The <a href="https://peps.python.org/pep-0636/" target="_blank">PEP 636</a> provides an official tutorial for the Python Pattern matching or Switch-Case statements.

#### Matching single values

```python
response_code = 201
match response_code:
    case 200:
        print("OK")
    case 201:
        print("Created")
    case 300:
        print("Multiple Choices")
    case 307:
        print("Temporary Redirect")
    case 404:
        print("404 Not Found")
    case 500:
        print("Internal Server Error")
    case 502:
        print("502 Bad Gateway")

# Created
```

#### Matching with the or Pattern

In this example, the pipe character (`|` or `or`) allows python to return the same response for two or more cases.

```python
response_code = 502
match response_code:
    case 200 | 201:
        print("OK")
    case 300 | 307:
        print("Redirect")
    case 400 | 401:
        print("Bad Request")
    case 500 | 502:
        print("Internal Server Error")

# Internal Server Error
```

#### Matching by the length of an Iterable

```python
today_responses = [200, 300, 404, 500]
match today_responses:
    case [a]:
            print(f"One response today: {a}")
    case [a, b]:
            print(f"Two responses today: {a} and {b}")
    case [a, b, *rest]:
            print(f"All responses: {a}, {b}, {rest}")

# All responses: 200, 300, [404, 500]
```

#### Default value

The underscore symbol (`_`) is used to define a default case:

```python
response_code = 800
match response_code:
    case 200 | 201:
        print("OK")
    case 300 | 307:
        print("Redirect")
    case 400 | 401:
        print("Bad Request")
    case 500 | 502:
        print("Internal Server Error")
    case _:
        print("Invalid Code")

# Invalid Code
```

#### Matching Builtin Classes

```python
response_code = "300"
match response_code:
    case int():
            print('Code is a number')
    case str():
            print('Code is a string')
    case _:
            print('Code is neither a string nor a number')

# Code is a string
```

#### Guarding Match-Case Statements

```python
response_code = 300
match response_code:
    case int():
            if response_code > 99 and response_code < 500:
                print('Code is a valid number')
    case _:
            print('Code is an invalid number')

# Code is a valid number
```

## Resources / References

- [Python Cheat Sheet - Control Flow](https://www.pythoncheatsheet.org/cheatsheet/control-flow)
