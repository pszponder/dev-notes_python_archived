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

You can also have multiple except blocks

```python
try:
    # some code...
except(TypeError) as e:
    print(f"Caught a Type Error: {e}")
except(ValueError) as e:
    print(f"Caught a Value Error: {e}")
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

```python
# When invoking this function, it will raise the NotImplementedError
# This reminds us to update the function logic
def my_func():
    raise NotImplementedError("Update function logic")
```

### Bubbling Up / Re-Raising Exceptions

If you wish to bubble up an exception, simply use the `raise` keyword inside an `except` block

Re-raising exceptions is useful in scenarios where you want to log the exception, perform some cleanup operations, or add additional context before letting the exception propagate further up

```python
"""
1. The "risky_operation" function tries to convert a string to an int
which raises a ValueError
1. The exception is caught by the except block inside "risky_operation".
After printing a message, it re-raises the exception using the "raise" keyword
1. The re-raised exception is then caught by the "except" block
inside the "main" function
"""

def risky_operation():
    try:
        # some code that might raise an exception
        x = int("not_a_number")
    except ValueError:
        print("A value error occurred in risky_operation!")
        raise  # re-raises the caught exception

def main():
    try:
        risky_operation()
    except ValueError:
        print("A value error was caught in main!")

main()
# A value error occurred in risky_operation!
# A value error was caught in main!
```

## Creating Custom Exceptions

You can define your own exception types by creating new classes [derived](python_oop.md#inheritance) from the base class `Exception` or any derived exception class.

```python
class CustomError(Exception):
    pass

raise CustomError("This is a custom error.")
```

```python
# Notice that the custom error can inherit from any built-in exception class
class CustomError(TypeError):
    pass

raise CustomError("This is a custom TypeError")
```

```python
class CustomRequestError(TypeError):
    """
    Exception raised when a specific error code is needed
    """
    def __init__(self, message, code):
        super().__init__(f"Error Code {code}: {message}")
        self.code = code

err = raise CustomRequestError("This is a custom TypeError", 500)
print(err.__doc__) # Prints the doc-string
```

```python
"""
1. Define a custom exception InsufficientManaError to indicate
when a spell fails due to a lack of mana.

2. The Wizard class has a method cast_spell that attempts to cast a spell.
If there's not enough mana, it raises the InsufficientManaError exception.

3. Within the cast_spell method, we catch this exception to print a user-friendly
message but then re-raise it to indicate a failure.

4. In the main function, we try to cast two spells.
The first one succeeds, but the second fails.
The re-raised exception is caught in main,
and we print another message indicating the interruption.
"""

class InsufficientManaError(Exception):
    """Exception raised for errors in the input."""
    def __init__(self, mana_required, mana_available):
        self.mana_required = mana_required
        self.mana_available = mana_available
        self.message = f"Insufficient mana! Required {mana_required}, but only {mana_available} available."
        super().__init__(self.message)


class Wizard:
    def __init__(self, name, mana):
        self.name = name
        self.mana = mana

    def cast_spell(self, spell, mana_required):
        try:
            if self.mana < mana_required:
                raise InsufficientManaError(mana_required, self.mana)
            self.mana -= mana_required
            print(f"{self.name} successfully cast {spell}!")
        except InsufficientManaError as e:
            print(f"{self.name} tried to cast {spell}, but {e.message}")
            raise  # re-raises the caught exception


def main():
    gandalf = Wizard("Gandalf", 50)

    try:
        gandalf.cast_spell("Light", 10)  # This should succeed
        gandalf.cast_spell("Teleport", 100)  # This should fail
    except InsufficientManaError:
        print("Spell casting was interrupted due to an error!")

main()
# Gandalf successfully cast Light!
# Gandalf tried to cast Teleport, but Insufficient mana! Required 100, but only 40 available.
# Spell casting was interrupted due to an error!
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
- [Ask forgiveness not permission - explained](https://stackoverflow.com/questions/12265451/ask-forgiveness-not-permission-explain)
- [Is it a good practice to use try-except-else in Python](https://stackoverflow.com/questions/16138232/is-it-a-good-practice-to-use-try-except-else-in-python/16138864#16138864)
- [Jeff Knupp - Write Cleaner Python: Use Exceptions](https://web.archive.org/web/20160313053014/http://jeffknupp.com/blog/2013/02/06/write-cleaner-python-use-exceptions/)
