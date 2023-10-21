# Functions

## Defining a Function

Use the `def` keyword to define a function

```python
def function_name(param1, param2, param3, ...):
    # function body

# Invoke the Function
function_name(arg1, arg2, arg3, ...)
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

### Default Parameter Values

Can provide default values to function parameters

```python
def greet(name="User"):
    print("Hello, " + name + "!")

greet()           # Outputs: Hello, User!
greet("Charlie")  # Outputs: Hello, Charlie!
```

### Keyword Arguments

Can send function arguments as key=value pairs

```python
def describe_pet(animal, pet_name):
    print(pet_name + " is a " + animal)

# Define which parameter the argument corresponds to
describe_pet(animal="cat", pet_name="Whiskers")
```

### Accepting Unknown Number of Arguments w/ \*args

If the number of arguments is unknown, add an `*` before the parameter name

- `*args` uses the `unpacking operator (*)` to accept a list of comma-separated positional arguments to a function invocation and return a [tuple](python_data-types_tuples.md)
- This tuple can then be iterated over using a for loop inside the function

```python
# Define a function with the *args keyword
def my_sum(*args):
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result

# Pass in as many arguments into the function
print(my_sum(1, 2, 3))
```

**NOTE:** `*args` is just a naming convention

- Instead of using `*args`, you can use any name, as long as it is prepended with a single asterisk `*` (the `unpacking operator`)

### Accepting Unknown Number of Keyword Arguments w/ \*\*kwargs

If you don't know how many [keyword arguments](python_functions.md#keyword-arguments) will be passed, add `**` before the parameter name

- `**` is the `Dictionary Unpacking Operator`
- `**kwargs` uses a `Dictionary Unpacking Operator` (`**`) which accepts a comma-separated list of key-value pairs (in format of `key=value`) and returns a dictionary of those key-value pairs
- This dictionary can then be [iterated over](python_data-types_dictionaries.md#iterate-over-keys--values-of-a-dictionary)

```python
def print_data(**data):
    for key, value in data.items():
        print(key + ": " + value)

print_data(firstname="John", lastname="Doe")
```

### Ordering Parameters in a Function

Correct order of function parameters:

1. Standard parameters
2. `*args`
3. Default parameters
4. `**kwargs`

```python
# Example of function with correct parameter order
# (standard args, *args, default parameters, **kwargs)
def my_function(a, b, *args, name="toby", **kwargs):
    pass
```

### Return Values

Use the `return` keyword to return values from a function

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Outputs: 8
```

## Local and Global Scope

- Code in the global scope cannot use any local variables.
- However, a local scope can access global variables.
- Code in a function’s local scope cannot use variables in any other local scope.
- You can use the same name for different variables if they are in different scopes. That is, there can be a local variable named spam and a global variable also named spam.

**NOTE:** Scope Rules

1. Start with local scope
2. If not found, go up to the next level-scope
3. Keep going up scope levels, until you get to Global Scope

```python
global_variable = 'I am available everywhere'

def some_function():
    print(global_variable)  # because is global
    local_variable = "only available within this function"
    print(local_variable)

# the following code will throw error because
# 'local_variable' only exists inside 'some_function'
print(local_variable)
# Traceback (most recent call last):
#   File "<stdin>", line 10, in <module>
# NameError: name 'local_variable' is not defined
```

### nonlocal keyword

Use the `nonlocal` keyword to reference a parent function's local scope

```python
def outer():
    x = "local"
    def inner():
        # ref parent function's x variable
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    inner()
    print("outer:", x)

outer()
# inner: nonlocal
# outer: nonlocal
```

### The global keyword

If you need to modify a global variable from within a function, use the `global` keyword:

```python
def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs) # spam
```

```python
total = 0

def count():
    # Reference the "total" variable from the global scope variable
    global total
    total += 1
    return total

count()
count()
print(count()) # 3
```

There are four rules to tell whether a variable is in a local scope or global scope:

1. If a variable is being used in the global scope (that is, outside all functions), then it is always a global variable.
2. If there is a global statement for that variable in a function, it is a global variable.
3. Otherwise, if the variable is used in an assignment statement in the function, it is a local variable.
4. But if the variable is not used in an assignment statement, it is a global variable.

## Anonymous Functions (Lambda Functions)

Lambda functions allow you to create small, anonymous functions without the need for a full `def` block

- Lambda functions are anonymous, meaning they do not need to be named.
- Lambda functions can be assigned to variables
- Lambda function can only contain one expressions, which is also the return value.
  - No statements are allowed
- Lambda functions can accept multiple arguments

```python
# Lambda function Syntax
lambda param1, param2, param3, ...: expression
```

```python
# Function which returns the input
def identity(x):
    return x

# Lambda function version of above identity function
lambda x: x
```

```python
f = lambda x: x + 1
print(f(2))  # Outputs: 3

f2 = lambda x, y, z: x + y + z
print(f2(1, 2, 3))  # Outputs: 6
```

```python
# Function to add two values together
def add(x, y):
    return x + y
add(5, 3) # 8

# lambda function to add two values together
# Store the lambda function as a variable
# You can then call that variable as it were a function
add = lambda x, y: x + y
add(5, 3) # 8
```

```python
# Assign the lambda function to a variable "full_name"
full_name = lambda first, last: f'{first.title()} {last.title()}'

# Invoke the lambda function assigned to the "full_name" variable
full_name('guido', 'van rossum') # 'Guido Van Rossum'
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

### Immediately Invoked Function Expression (IIFE)

An `IIFE` (`Immediately Invoked Function Expression`) allows us to immediately execute a Python Lambda Function via use of parenthesis.

```python
# In this example, the value 2 is passed as an argument
# to the lambda function definition which adds 1 to the argument
# This expression is invoked immediately
(lambda x: x + 1)(2) # 3
```

```python
# Another example of IIFE using Lambda Function and 2 arguments
(lambda x, y: x + y)(2, 3) # 5
```

### Lambda Function Arguments

Like a normal function object defined with `def`, Python lambda expressions support all the different ways of passing arguments. This includes:

- Positional arguments
- Named arguments (sometimes called keyword arguments)
- Variable list of arguments (often referred to as **varargs**)
- Variable list of keyword arguments
- Keyword-only arguments

```python
# Pass in multiple positional arguments to the lambda func
(lambda x, y, z: x + y + z)(1, 2, 3) # 6

# Define lambda func with keyword / named parameter
(lambda x, y, z=3: x + y + z)(1, 2) # 6

# Pass keyword argument to the lambda function
(lambda x, y, z=3: x + y + z)(1, y=2) # 6

# Define lambda func with args
(lambda *args: sum(args))(1,2,3) # 6

# Define lambda func with kwargs
(lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3) # 6

# Putting it all together
(lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3) # 6
```

### Higher-Order Functions w/ Lambda

Lambda functions are frequently used with [higher-order functions](https://en.wikipedia.org/wiki/Higher-order_function), which take one or more functions as arguments or return one or more functions.

A lambda function can be a higher-order function by taking a function (normal or lambda) as an argument like in the following contrived example:

```python
# Accept a function as an argument
high_ord_func = lambda x, func: x + func(x)

# Pass in lambda functions as arguments to the HOF
high_ord_func(2, lambda x: x * x) # 6
high_ord_func(2, lambda x: x + 3) # 7
```

```python
# Create a function which returns another function
# the return function is a higher order function
def make_adder(n):
    return lambda x: x + n

# Create new functions using the HOF make_adder
plus_3 = make_adder(3)
plus_5 = make_adder(5)

# Invoke the newly created functions
plus_3(4) # 7
plus_5(4) # 9
```

### Uses for Lambda Functions

Lambda functions are regularly used with the built-in functions [`map()`](https://docs.python.org/3/library/functions.html#map) and [`filter()`](https://docs.python.org/3/library/functions.html#filter), as well as [`functools.reduce()`](https://docs.python.org/3/library/functools.html?highlight=reduce#functools.reduce), exposed in the module [`functools`](https://docs.python.org/3/library/functools.html).

The following three examples are respective illustrations of using those functions with lambda expressions as companions:

```python
list(map(lambda x: x.upper(), ['cat', 'dog', 'cow']))
# ['CAT', 'DOG', 'COW']

list(filter(lambda x: 'o' in x, ['cat', 'dog', 'cow']))
# ['dog', 'cow']

from functools import reduce
reduce(lambda acc, x: f'{acc} | {x}', ['cat', 'dog', 'cow'])
# 'cat | dog | cow'
```

## Annotating Functions using Docstrings

A `Docstring` is a multi-line string that is placed as the 1st part of function used to describe what the function does.

`Docstring`s are defined with two sets of three single quotes, or two sets of three double quotes.

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

## Decorators

### What is a decorator?

A decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.

**NOTE:** `decorators` wrap a function, modifying its behavior

### Higher Order Functions

A `Higher Order Function` (HOF) satisfies one or more of the below conditions:

- `HOF` is a function which accepts another function as an argument
- `HOF` is a function which returns another functions

```python
# HOF which accepts a function as an argument
def hof1(func):
    func() # Execute the passed in function

# Define a standard function
def say_hello():
    print("hello")

# Assign a variable the output of the HOF
my_func = hof1(say_hello)
my_func() # Prints "hello"
```

```python
# HOF which returns a function
def hof2():
    def inner():
        return 5
    return func

# Assign a variable the output of the HOF (which is a function)
my_func = hof2()
my_func() # returns 5
```

### Defining and Invoking a Decorator

A `decorator` is a `HOF` which:

- Accepts a function as a parameter
- Defines and returns an inner wrapper function
- This inner wrapper function invokes the function parameter passed into the `decorator HOF`
- The inner wrapper function can add additional functionality to the
- Once you define the decorator, you can "decorate" and function with that decorator using the `@<decorator_name>`

```python
# Define a decorator function
def my_decorator(func):
    # Define the inner wrapper function
    #  which invokes the passed-in function parameter
    def wrap_func():
        print('***')
        func()
        print('***')
    return wrap_func

# "Decorate" the "hello" function with my_decorator
#  "hello" func is passed into my_decorator
# The "hello" function is actually now the returned wrap_func

@my_decorator
def hello():
    print('hello')

hello() # invoke the decorated function
# ***
# hello
# ***

# "Decorate" the "bye" function with my_decorator
#  "bye" function is passed into my_decorator
# The "bye" function is actually now the returned wrap_func

@my_decorator
def bye():
    print('see you later!')

bye() # Invoke the decorated function
# ***
# see you later!
# ***
```

Declaring a decorator function which can accept parameters

```python
# Define a decorator function
def my_decorator(func):
    # Define the inner wrapper function
    #  which invokes the passed-in function parameter
    # The wrap_func accepts any number of args / keyword args
    def wrap_func(*args, **kwargs):
        print('***')
        func(*args, **kwargs)
        print('***')
    return wrap_func

# "Decorate" the "hello" function with my_decorator
#  "hello" func is passed into my_decorator
# The "hello" function is actually now the returned wrap_func

@my_decorator
def hello(greeting):
    print(greeting)

hello("hello") # invoke the decorated function
# ***
# hello
# ***
```

Example of Decorator Function

```python
from time import time

# Define the performance decorator
# This decorator prints the time it takes to execute the
#   decorated function
def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f"took { t2 - t1} s")
        return result
    return wrapper

@performance
def long_time():
    for i in range(10000000):
        i*5

long_time() # "took 0.20406579971313477 s"
```

```python
# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True
}

# Define the decorator
def authenticated(fn):
  def wrapper(*args, **kwargs):
    if args[0]['valid']:
        return fn(*args, **kwargs)
  return wrapper

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)
```

## Resources / References

- [Real Python - Python args and kwargs: Demystified](https://realpython.com/python-kwargs-and-args/)
- [Python Cheatsheet - Functions](https://www.pythoncheatsheet.org/cheatsheet/functions)
- [Real Python - Lambda Functions](https://realpython.com/python-lambda/)
- [Real Python - Functional Programming in Python](https://realpython.com/courses/functional-programming-python/)
- [Real Python - Write Pythonic and Clean Code with namedtuple](https://realpython.com/python-namedtuple/)
- [Real Python - Primer on Python Decorators](https://realpython.com/primer-on-python-decorators/)
- [ArjanCodes - Python Decorators: The Complete Guide](https://www.youtube.com/watch?v=QH5fw9kxDQA)
