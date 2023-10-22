# Testing in Python

## Using the unittest library

[Real Python - Getting Started with Testing in Python](https://realpython.com/python-testing/)

Python has a built-in library called `unittest` that can be used to write and run unit tests

```python
# main.py

def do_stuff(num=0):
    try:
        if num:
            return int(num) + 5
        else:
            return "please enter a number"
    except ValueError as err:
        return err
```

```python
# test.py

import unittest
import main  # Import the Python module we are testing


# Create a test class
# This class inherits from the unittest.TestCase class class TestMain(unittest.TestCase):
    # Special setup method
    # runs before each test is executed
    def setUp(self) -> None:
        print("setting up for test...")
        return super().setUp()

    # Special teardown method
    # runs after each test is executed
    def tearDown(self) -> None:
        print("cleaning up...")
        return super().tearDown()

    # Test the function works as expected
    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    # Test that the method throws an error if passed in values are incorrect
    def test_do_stuff2(self):
        test_param = "asdf"
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    # Check what happens when None is passed in
    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, "please enter a number")


# Run the entire test file
# (only if it is the file being executed by the Python Interpreter)
if __name__ == "__main__":
    unittest.main()
```

### assertions -- unittest

[assertion methods in unittest](https://docs.python.org/3/library/unittest.html#assert-methods)

| Assert Method               | Checks That            |
| --------------------------- | ---------------------- |
| `assertEqual(a, b)`         | `a == b`               |
| `assertNotEqual(a, b`       | `a != b`               |
| `assertTrue(x)`             | `bool(x) is True`      |
| `assertFalse(x)`            | `bool(x) is False`     |
| `assertIs(a, b)`            | `a is b`               |
| `assertIsNot(a, b)`         | `a is not b`           |
| `assertIsNone(x)`           | `x is not None`        |
| `assertIn(a, b)`            | `a in b`               |
| `assertNotIn(a, b)`         | `a not in b`           |
| `assertIsInstance(a, b)`    | `isinstance(a, b)`     |
| `assertNotIsInstance(a, b)` | `not isinstance(a, b)` |

### Running all of the project unit tests

Execute the below script to run all of the unit tests in the current directory

```bash
python -m unittest
```

To run in verbose mode, add the `-v` option

```bash
python -m unittest -v
```

### Examples

```python
# main.py

import random

def run_guess(guess, answer):
    if  0 < guess < 11:
        if guess == answer:
            print('you are a genius!')
            return True
    else:
        print('hey bozo, I said 1~10')
        return False

if __name__ == '__main__':
    answer = random.randint(1, 10)
    while True:
        try:
            guess = int(input('guess a number 1~10:  '))
            if (run_guess(guess, answer)):
                break
        except ValueError:
            print('please enter a number')
            continue
```

```python
# test.py

import unittest
import main

class TestGame(unittest.TestCase):
    def test_input(self):
        # please note in the video, I had the parameters flipped it should be the "guess" parameter 1st and "answer" parameter 2nd
        result = main.run_guess(5, 5)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = main.run_guess(0, 5)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = main.run_guess(11, 5)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        result = main.run_guess('11', 5)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
```

## Pytest

- [Real Python - Effective Python Testing with Pytest](https://realpython.com/pytest-python-testing/)

## References

- [Python Docs - unittest](https://docs.python.org/3/library/unittest.html)
- [Real Python - Getting Started with Testing in Python](https://realpython.com/python-testing/)
- [Real Python - Effective Python Testing with Pytest](https://realpython.com/pytest-python-testing/)
