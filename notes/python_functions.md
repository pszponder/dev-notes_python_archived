# Functions

A function is a block of organized, reusable code that is used to perform a single, related actions.

Functions provide better modularity for your application and allow for code reusability.

## Defining a Function

Use the `def` keyword to define a function

```python
def function_name(parameters):
    # function body

# Invoke the Function
function_name(arguments)
```

```python
# Function w/o parameters
def greet():
    print("Hello!")

greet()  # Outputs: Hello!
```

```python
# Function w/ parameters
def greet(name):
    print("Hello, " + name + "!")

greet("Alice")  # Outputs: Hello, Alice!
```

## Return Values

Use the `return` keyword to return values from a function

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Outputs: 8
```

## Default Parameter Values

Can provide default values to function parameters

```python
def greet(name="User"):
    print("Hello, " + name + "!")

greet()           # Outputs: Hello, User!
greet("Charlie")  # Outputs: Hello, Charlie!
```

## Keyword Arguments

Can send function arguments as key=value pairs

```python
def describe_pet(animal, pet_name):
    print(pet_name + " is a " + animal)

# Define which parameter the argument corresponds to
describe_pet(animal="cat", pet_name="Whiskers")
```

## \*args (Arbitrary Arguments)

If the number of arguments is unknown, add an `*` before the parameter name

```python
def print_names(*names):
    for name in names:
        print(name)

print_names("Alice", "Bob", "Charlie")  # Outputs: Alice, Bob, Charlie
```

## \*\*kwargs (Arbitrary Keyword Arguments)

If you don't know how many keyword arguments will be passed, add `**` before the parameter name

```python
def print_data(**data):
    for key, value in data.items():
        print(key + ": " + value)

print_data(firstname="John", lastname="Doe")
```

## Recursion

```python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  # Outputs: 120
```

## Anonymous Functions (Lambda Functions)

Lambda functions allow you to create small, anonymous functions without the need for a full `def` block

- Lambda functions are anonymous, meaning they do not need to be named.
- Lambda functions can be assigned to variables
- Lambda function can only contain one expressions, which is also the return value.
  - No statements are allowed
- Lambda functions can accept multiple arguments

```python
# Lambda function Syntax
lambda arguments: expression
```

```python
f = lambda x: x + 1
print(f(2))  # Outputs: 3

f2 = lambda x, y, z: x + y + z
print(f2(1, 2, 3))  # Outputs: 6
```

```python
# Sorting: Lambda functions are often used as the key function for sorting
data = [('apple', 3), ('banana', 2), ('cherry', 5)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)  # Outputs: [('banana', 2), ('apple', 3), ('cherry', 5)]

# Functional Programming tools: Lambda functions are commonly used
# with functions like map(), filter(), and reduce()
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, nums))
print(squares)  # Outputs: [1, 4, 9, 16]
```

## Documenting Functions using Docstrings

Use `"""<documentation>"""` docstrings to document a function

```python
def simple_function():
    """This is a simple docstring."""
    pass
```

```python
def complex_function(arg1, arg2):
    """
    This is a function that does something complex.

    Parameters:
    - arg1: The first argument. It does this.
    - arg2: The second argument. It does that.

    Returns:
    - It returns something useful.

    """
    pass
```
