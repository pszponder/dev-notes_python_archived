# Error and Exception Handling

Handling errors and exceptions is an essential aspect of writing robust programs. In Python, errors can be managed using a combination of `try`, `except`, `else`, and `finally` blocks.

## try / except / else / finally

```python
try:
    # Code that might raise an exception
except SomeExceptionType as e:
    # Handle the exception
else:
    # Code to run if there's no exception (optional)
finally:
    # Code to run no matter what, exception or not (optional)
```

### 1. **The `try` Block**:

You place the code that might raise an exception inside the `try` block. If an exception is raised, Python will stop executing the `try` block and jump to the corresponding `except` block.

### 2. **The `except` Block**:

This block contains code that will run if an exception is raised in the `try` block. You can specify the type of exceptions you want to catch, and you can have multiple `except` blocks to handle different types of exceptions.

```python
try:
    x = 1 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
```

```python
try:
    age = int(input('what is your age? '))
    print(age)
except:
    print('please enter a number')
```

You can catch multiple exceptions in one block:

```python
try:
    # some code...
except (TypeError, ValueError) as e:
    print(f"Caught an error: {e}")
```

If you want to catch all exceptions (not recommended generally, unless you have a good reason):

```python
try:
    # some code...
except Exception as e:
    print(f"Caught an error: {e}")
```

### 3. **The `else` Block**:

This block, if present, will run after the `try` block completes without any exceptions.

```python
try:
    print("Everything is fine.")
except Exception as e:
    print(f"Caught an error: {e}")
else:
    print("No errors encountered.")
```

### 4. **The `finally` Block**:

Code within the `finally` block will always be executed, whether an exception was raised or not. This is typically used for cleanup actions, like closing files.

```python
try:
    f = open("somefile.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("File not found.")
finally:
    f.close()
```

## Catching Specific Errors / Exceptions

By default, the `except:` block catches any errors / exceptions which are thrown when trying to execute code in the `try:` block.

You can specify an error / exception type in the `except:` block so that it only triggers on that specific error / exception.

To handle multiple specific errors / exceptions, we can add multiple `except:` blocks

Refer [here for a list of built-in exceptions](https://docs.python.org/3/library/exceptions.html)

```python
while True:
    try:
        age = int(input('what is your age? '))
        print(age)
    except ValueError:
        # This block runs if a ValueError exception is thrown
        # by the logic in the try block
        print('please enter a number')
    except ZeroDivisionError:
        # This block runs if ZeroDivisionError exception is thrown
        # by the logic in the try block
        print('please enter age higher than 0')
    except:
        # This block runs if an error is thrown by the try block
        # which isn't handled by the above 2 except blocks
        print('handled generic error')
    else:
        # This block runs if logic in try block executes 
        #  without any errors being thrown
        print('thank you!')
        break
```

## Aliasing Specific Errors During Error Handling

When specifying specific error to handle by the `except` block, we can give them a name alias by using the `as` keyword

```python
def sum(num1, num2):
    try:
        return num1 + num2
    # Alias the TypeError object as err
    except TypeError as err:
        print(f'please enter numbers: {err}')
        print(err) # just prints the error as a string

print(sum(1, '2'))
# please etner numbers: unsupported operand type(s) for + 'int' and 'str'
```

## Catching Multiple Error / Exception Types at the Same Time

You can also specify an `except:` block to handle multiple types of errors / exceptions. 

Simply pass in a comma-separated list of errors / exceptions and wrap in parenthesis after `except`

> `except (<errorType1>, <errorType2>, ...):`

```python
def divide(num1, num2):
    try:
        return num1 / num2
    # This except block triggers if either 
    # TypeError or ZeroDivisionError trigger in the try block
    except (TypeError, ZeroDivisionError) as err:
        print(err)

print(divide(1, "2")) # unsupported operand type(s) for /: ...
print(divide(1, 0))   # division by zero
```

## Throwing / Raising Errors

Use the `raise` keyword in conjunction with an error / exception function to throw an error

```python
# This will throw an error in Python and cause the program
#  to stop executing
raise ValueError('I am raising a ValueError')
```

```python
x = -1
if x < 0:
    raise ValueError("Negative values are not allowed!")
```

## Creating Custom Exceptions

You can define your own exception types by creating new classes derived from the base class `Exception` or any derived exception class.

```python
class CustomError(Exception):
    pass

raise CustomError("This is a custom error.")
```

## Scope in try / except

The scope of the variables declared within the `try` block are considered global scope. (Only functions have local scope in Python). 

```python
# Extract Arguments from the CL
try:
    SOURCE_DIR = sys.argv[1]
    DEST_DIR = sys.argv[2]
except IndexError as exc:
    raise SystemExit(f"Usage: {sys.argv[0]} <source_dir> <dest_dir>") from exc

# Assuming try block is executed SOURCE_DIR and DEST_DIR
#  are defined and available here
print(SOURCE_DIR)
print(DEST_DIR)
```

## Resources / References

- [Python Docs - Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)
- [Real Python - Python's raise: Effectively Raising Exceptions in Your Code](https://realpython.com/python-raise-exception/)
- [Real Python - Exceptions](https://realpython.com/python-exceptions/)