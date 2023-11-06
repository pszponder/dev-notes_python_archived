# Python Logging

## Logging to Standard Output using print()

Use the `print()` function to log to standard output.

`print()` does not return anything.

```python
# Log "Hello World" to the Console
print("Hello World")

# You can pass multiple comma-separated strings to the function and they will be printed on the same line with spaces in between
print("hello", "world", "!") # hello world !
```

### end keyword

The keyword argument `end` can be used to avoid the newline after the output, or end the output with a different string:

```python
phrase = ['printed', 'with', 'a', 'dash', 'in', 'between']
>>> for word in phrase:
...     print(word, end='-')
...
# printed-with-a-dash-in-between-
```

### sep keyword

The keyword `sep` specify how to separate the objects, if there is more than one:

```python
print('cats', 'dogs', 'mice', sep=',')
# cats,dogs,mice
```

### Escape Characters

- Newline => `\n`
- Tab => `\t`
- Double Quote => `\"`
- Single Quote => `\'`
- Backslash => `\\`

## f-strings in Python

Python `f-strings` are the same as string literals in JavaScript

Put an `f` in front of a Python string. Then, inside the string, you can use Curly Braces to evaluate python code

```python
first_name = "Legolas"
last_name = "Greenleaf"
print(f"Hello {first_name} {last_name}")
```

## Obtaining user input with the input() function

The `input()` function takes the input from the user and converts it into a string:

```python
>>> print('What is your name? ')   # ask for their name
>>> my_name = input()
>>> print('Hi, {}'.format(my_name))
# What is your name?
# Martha
# Hi, Martha
```

`input()` can also set a default message without using `print()`:

```python
>>> my_name = input('What is your name? ')  # default message
>>> print('Hi, {}'.format(my_name))
# What is your name? Martha
# Hi, Martha
```

```python
user = input("What is your name? ")
pw = input("What is your password? ")
pw_length = len(pw)
pw_encoded = "*" * pw_length

print(f"Hi {user}, your password {pw_encoded} is {pw_length} characters long")
```

## The logging module

The `logging` module in Python is used to log messages that you want to see during the development or production phase.

It provides a flexible framework for emitting log messages from Python programs and can be configured to work with different logging destinations like console, file, or even remote logging servers.

### Logging Levels

Here are the different log levels, listed from highest priority to lowest:

- `CRITICAL` (50)
  - For very serious errors that prevent the program from continuing.
  - Errors that cause application failure, such as a crucial database being unavailable
- `ERROR` (40):
  - For serious problems that need to be logged.
  - Handling errors that affect the application's operation, such as an HTTP 500 error, but allow the application to continue working
- `WARNING` (30):
  - For warning messages that indicate something unexpected or a potential problem.
  - Non-critical issues that require attention, such as deprecated code usage or log disk space
- `INFO` (20):
  - For informational messages to track the flow of the program.
  - Could be user authentication message or version info
- `DEBUG` (10)
  - For detailed debugging information.
  - Debugging message, provides extra info for developers during development or testing

### Logger Basics

The logging module in Python contains 3 main items:

- `Logger`
  - Schedules log information for input
- `Handler`
  - Sends the log information to a destination
  - Each logger can have one or more handlers
  - Example, can have one handler for the console and another to log to files
- `Formatter`
  - Defines how the log will be displayed
    - Ex. current time + log message
  - Used by log handlers to format the log message
  - Each handler can have only one formatter

```python
# my_logger.py

import logging

# Create a logger and set its level
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)  # Set minimum log level to DEBUG

# Create a console handler and set its log level to INFO
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO) # Only logs if level is INFO or greater

# Create a file handler and sets its log level to DEBUG
# NOTE: Since the level is the same as what is configured in logger
#  this isn't necessary
file_handler = logging.FileHandler("file.log")
file_handler.setLevel(logging.DEBUG)  # Optional since same as logger

# Create a formatter & add it to the handlers
# (can also create separate formatters for each handler)
formatter = logging.Formatter(
    "%(asctime)s.%(msecs)03dZ %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S"  # Adding ISO data format
)
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)
```

```python
# quest.py
from my_logger import logger

def start_quest():
    # Log messages using the configured logger
    logger.debug("Gandalf starts his journey to Middle Earth.")
    logger.info("Frodo has the ring.")
    logger.warning("The ring wraiths are near.")
    logger.error("Boromir tries to take the ring.")
    logger.critical("Sauron has found Frodo.")

if __name__ == "__main__":
    start_quest()
```

## Resources / References

- [RealPython - Logging in Python](https://realpython.com/python-logging/)
- [Sematext - Python Logging Tutorial: How-To, Basic Examples & Best Practices](https://sematext.com/blog/python-logging/)
- [ArjanCodes - Python Logging: How to Write Logs Like a Pro!](https://www.youtube.com/watch?v=pxuXaaT1u3k)
- [teclado - Python logging tutorial: loggers, handlers, and formatters](https://www.youtube.com/watch?v=b4Ms4wxJuPg)
