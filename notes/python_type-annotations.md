# Type Annotations / Hints in Python

Python has support for optional `type hints` / `type annotations`.

`Type Hints` / `Type Annotations` enable declaring the type of a variable (similar to TypeScript in JavaScript).

```python
# WITHOUT TYPE HINTS / ANNOTATIONS

def get_full_name(first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


print(get_full_name("john", "doe"))
```

```python
# WITH TYPE HINTS / ANNOTATIONS

def get_full_name(first_name: str, last_name: str) -> str:
    full_name = first_name.title() + " " + last_name.title()
    return full_name


print(get_full_name("john", "doe"))

```

## Variables

```python
# This is how you declare the type of a variable
age: int = 1

# You don't need to initialize a variable to annotate it
a: int  # Ok (no value at runtime until assigned)

# Doing so can be useful in conditional branches
child: bool
if age < 18:
    child = True
else:
    child = False
```

## Useful built-in types

### Simple Types

```python
# For most types, just use the name of the type in the annotation
x: int = 1
x: float = 1.0
x: bool = True
x: str = "test"
x: bytes = b"test"
```

```python
def get_items(
    item_a: str,
    item_b: int,
    item_c: float,
    item_d: bool,
    item_e: bytes
):
    return item_a, item_b, item_c, item_d, item_d, item_e
```

### Collections / (lists, sets, dictionaries, tuples)

You can use the same builtin types as generics (with square brackets and types inside):

- `list`
- `tuple`
- `set`
- `dict`

```python
# For collections on Python 3.9+, the type of the collection item is in brackets
x: list[int] = [1]
x: list[str] = ["hello", "world"]
x: list[list[int]] = [[1, 2, 3], [4, 5, 6]]
x: set[int] = {6, 7}

# For mappings, we need the types of both keys and values
x: dict[str, float] = {"field": 2.0}  # Python 3.9+
x: dict[str, list[str]] = {
    "MainServer": ["1.1.1.1", "80", "yes"],
    "OtherServer": ["2.2.2.2", "99", "no"]
}

# For tuples of fixed size, we specify the types of all the elements
x: tuple[int, str, float] = (3, "yes", 7.5)  # Python 3.9+

# For tuples of variable size, we use one type and ellipsis
x: tuple[int, ...] = (1, 2, 3)  # Python 3.9+
```

```python
# On Python 3.8 and earlier, the name of the collection type is
# capitalized, and the type is imported from the 'typing' module
from typing import List, Set, Dict, Tuple
x: List[int] = [1]
x: Set[int] = {6, 7}
x: Dict[str, float] = {"field": 2.0}
x: Tuple[int, str, float] = (3, "yes", 7.5)
x: Tuple[int, ...] = (1, 2, 3)
```

### Union (Specifying Multiple Types)

You can declare that a variable can be any of **several types**, for example, an `int` or a `str`.

In Python 3.6 and above (including Python 3.10) you can use the `Union` type from `typing` and put inside the square brackets the possible types to accept.

```python
from typing import Union

# On Python 3.10+, use the | operator when something could be one of a few types
x: list[int | str] = [3, 5, "test", "fun"]  # Python 3.10+
# On earlier versions, use Union
x: list[Union[int, str]] = [3, 5, "test", "fun"]

# Function which accepts union of either integer or string
def process_item(item: Union[int, str]):
    print(item)
```

In Python 3.10 there's also a **new syntax** where you can put the possible types separated by a vertical bar (`|`).

```python
def process_item(item: int | str):
    print(item)
```

### None and Possibly None

You can declare that a value could have a type, like `str`, but that it could also be `None`.

In Python 3.6 and above (including Python 3.10) you can declare it by importing and using `Optional` from the `typing` module.

Using `Optional[str]` instead of just `str` will let the editor help you detecting errors where you could be assuming that a value is always a `str`, when it could actually be `None` too.

`Optional[Something]` is actually a shortcut for `Union[Something, None]`, they are equivalent.

```python
from typing import Optional


def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")

# Use Optional[X] for a value that could be None
# Optional[X] is the same as X | None or Union[X, None]
x: Optional[str] = "something" if some_condition() else None
if x is not None:
    # Mypy understands x won't be None here because of the if-statement
    print(x.upper())

# If you know a value can never be None due to some logic that python doesn't
# understand, use an assert
assert x is not None
print(x.upper())
```

This also means that in Python 3.10, you can use `Something | None`:

```python
def say_hi(name: str | None = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")
```

### Custom Types

```python
# Declare a custom type called tcp_dict
tcp_dict = dict[str, list[str]]

# Use the custom type to annotate a variable
my_tcp_dict: tcp_dict = {
    "MainServer": ["1.1.1.1", "80", "yes"],
    "OtherServer": ["2.2.2.2", "99", "no"]
}

# Use tcp_dict custom type to specify type of function parameter
def print_tcp_dict(dt: tcp_dict):
    for key, value in dt.items():
        print(f"NAME: {key}")
        print(f"IP: {value[0]}")
        print(f"PORT: {value[1]}")
        print(f"ACTIVE: {value[2]}")


print_tcp_dict(my_tcp_dict)
```

## Specifying a type as optional

**NOTE:** `Optional[X]` is equivalent to `X | None`

**CAUTION:** Specify default value for `Optional[X]`

- When specifying a type as optional, you have to provide a default value.
- If you don't want to provide a specific value, use `None`

```python
from uuid import UUID, uuid4
from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    """
    Model to simulate a User
    Optional specifiese that the property is optional
    """

    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
```

```python
# As of Python 3.10, can use X | None instead of Optional[X]
class UserUpdateRequest(BaseModel):
    """
    Model used for PUT Request when Updating a User
    """

    first_name: str | None
    last_name: str | None
    middle_name: str | None
    roles: list[Role] | None
```

Note that this is not the same concept as an optional argument, which is one that has a default. An optional argument with a default does not require the `Optional` qualifier on its type annotation just because it is optional. For example:

```python
def foo(arg: int = 0) -> None:
    #...
```

On the other hand, if an explicit value of `None` is allowed, the use of `Optional` is appropriate, whether the argument is optional or not. For example:

```python
def foo(arg: Optional[int] = None) -> None:
    #...
```

## Functions

```python
# This is how you annotate a function definition
def stringify(num: int) -> str:
    return str(num)

# And here's how you specify multiple arguments
def plus(num1: int, num2: int) -> int:
    return num1 + num2

# If a function does not return a value, use None as the return type
# Default value for an argument goes after the type annotation
def show(value: str, excitement: int = 10) -> None:
    print(value + "!" * excitement)

# Here is an example with a list
def process_items(items: list[str]) -> None:
    for item in items:
        print(item)

# Here is an example of a tuple and set
def process_items(
    items_t: tuple[int, int, str],
    items_s: set[bytes]
) -> None:
    return items_t, items_s

# Here is an example with a dict
def process_items(prices: dict[str, float]) -> None:
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)

# Note that arguments without a type are dynamically typed (treated as Any)
# and that functions without any annotations not checked
def untyped(x):
    x.anything() + 1 + "string"  # no errors
```

```python
from typing import Callable, Iterator, Union, Optional

# This is how you annotate a callable (function) value
x: Callable[[int, float], float] = f
def register(callback: Callable[[str], int]) -> None: ...

# A generator function that yields ints is secretly just a function that
# returns an iterator of ints, so that's how we annotate it
def gen(n: int) -> Iterator[int]:
    i = 0
    while i < n:
        yield i
        i += 1

# You can of course split a function annotation over multiple lines
def send_email(address: Union[str, list[str]],
               sender: str,
               cc: Optional[list[str]],
               bcc: Optional[list[str]],
               subject: str = '',
               body: Optional[list[str]] = None
               ) -> bool:
    ...

# Mypy understands positional-only and keyword-only arguments
# Positional-only arguments can also be marked by using a name starting with
# two underscores
def quux(x: int, /, *, y: int) -> None:
    pass

quux(3, y=5)  # Ok
quux(3, 5)  # error: Too many positional arguments for "quux"
quux(x=3, y=5)  # error: Unexpected keyword argument "x" for "quux"

# This says each positional arg and each keyword arg is a "str"
def call(self, *args: str, **kwargs: str) -> str:
    reveal_type(args)  # Revealed type is "tuple[str, ...]"
    reveal_type(kwargs)  # Revealed type is "dict[str, str]"
    request = make_request(*args, **kwargs)
    return self.do_api_query(request)
```

## Classes

You can also declare a class as the type of a variable.

```python
# Let's say you have a class `Person`, with a name
class Person:
    def __init__(self, name: str):
        self.name = name


# Now you can declare a variable to be of type Person
# (refer to the function parameter)
def get_person_name(one_person: Person):
    return one_person.name

```

```python
class BankAccount:
    # The "__init__" method doesn't return anything,
    # so it gets return type "None"
    # just like any other method that doesn't return anything
    def __init__(self, account_name: str, initial_balance: int = 0) -> None:
        # mypy will infer the correct types for these instance variables
        # based on the types of the parameters.
        self.account_name = account_name
        self.balance = initial_balance

    # For instance methods, omit type for "self"
    def deposit(self, amount: int) -> None:
        self.balance += amount

    def withdraw(self, amount: int) -> None:
        self.balance -= amount

# User-defined classes are valid as types in annotations
account: BankAccount = BankAccount("Alice", 400)

def transfer(src: BankAccount, dst: BankAccount, amount: int) -> None:
    src.withdraw(amount)
    dst.deposit(amount)

# Functions that accept BankAccount also accept any subclass of BankAccount!
class AuditedBankAccount(BankAccount):
    # You can optionally declare instance variables in the class body
    audit_log: list[str]
    # This is an instance variable with a default value
    auditor_name: str = "The Spanish Inquisition"

    def __init__(self, account_name: str, initial_balance: int = 0) -> None:
        super().__init__(account_name, initial_balance)
        self.audit_log: list[str] = []

    def deposit(self, amount: int) -> None:
        self.audit_log.append(f"Deposited {amount}")
        self.balance += amount

    def withdraw(self, amount: int) -> None:
        self.audit_log.append(f"Withdrew {amount}")
        self.balance -= amount

audited = AuditedBankAccount("Bob", 300)
transfer(audited, account, 100)  # type checks!

# You can use the ClassVar annotation to declare a class variable
class Car:
    seats: ClassVar[int] = 4
    passengers: ClassVar[list[str]]

# If you want dynamic attributes on your class, have it
# override "__setattr__" or "__getattr__"
class A:
    # This will allow assignment to any A.x, if x is the same type as "value"
    # (use "value: Any" to allow arbitrary types)
    def __setattr__(self, name: str, value: int) -> None: ...

    # This will allow access to any A.x, if x is compatible with the return type
    def __getattr__(self, name: str) -> int: ...

a.foo = 42  # Works
a.bar = 'Ex-parrot'  # Fails type checking
```

## Standard "duck types"

In typical Python code, many functions that can take a list or a dict as an argument only need their argument to be somehow “list-like” or “dict-like”. A specific meaning of “list-like” or “dict-like” (or something-else-like) is called a “duck type”, and several duck types that are common in idiomatic Python are standardized.

```python
from typing import Mapping, MutableMapping, Sequence, Iterable

# Use Iterable for generic iterables (anything usable in "for"),
# and Sequence where a sequence (supporting "len" and "__getitem__") is
# required
def f(ints: Iterable[int]) -> list[str]:
    return [str(x) for x in ints]

f(range(1, 3))

# Mapping describes a dict-like object (with "__getitem__") that we won't
# mutate, and MutableMapping one (with "__setitem__") that we might
def f(my_mapping: Mapping[int, str]) -> list[int]:
    my_mapping[5] = 'maybe'  # mypy will complain about this line...
    return list(my_mapping.keys())

f({3: 'yes', 4: 'no'})

def f(my_mapping: MutableMapping[int, str]) -> set[str]:
    my_mapping[5] = 'maybe'  # ...but mypy is OK with this.
    return set(my_mapping.values())

f({3: 'yes', 4: 'no'})

import sys
from typing import IO

# Use IO[str] or IO[bytes] for functions that should accept or return
# objects that come from an open() call (note that IO does not
# distinguish between reading, writing or other modes)
def get_sys_IO(mode: str = 'w') -> IO[str]:
    if mode == 'w':
        return sys.stdout
    elif mode == 'r':
        return sys.stdin
    else:
        return sys.stdout
```

## Coroutines and asyncio

See [Typing async/await](https://mypy.readthedocs.io/en/stable/more_types.html#async-and-await) for the full detail on typing coroutines and asynchronous code.

```python
import asyncio

# A coroutine is typed like a normal function
async def countdown(tag: str, count: int) -> str:
    while count > 0:
        print(f'T-minus {count} ({tag})')
        await asyncio.sleep(0.1)
        count -= 1
    return "Blastoff!"
```

## References

- [Python Docs - typing](https://docs.python.org/3/library/typing.html)
- [mypy - Type hints cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
- [FastAPI - Python Type Hints Intro](https://fastapi.tiangolo.com/python-types/)
- [NerualNine - Type Hinting Makes Your Code More Professional](https://www.youtube.com/watch?v=BzBUagNkX1E)
- [ArjanCodes - 5 Reasons Why You Should Use Type Hints in Python](https://www.youtube.com/watch?v=dgBCEB2jVU0)
- [Real Python - Type Checking](https://realpython.com/python-type-checking/#playing-with-python-types-part-2)
