# Python Generators

Generators in Python are a powerful tool for handling large amounts of data without consuming a lot of memory.

A generator is a type of iterable, like a list or tuple. However, unlike lists, it does not store all its values in memory; instead, it generates them on the fly.

The main advantage of generators is that they can be used to produce items one at a time and only when required, consuming less memory.

Generators...

- Allow us to generate a sequence of values over time
- Allow us to use special keywords `pause` and `resume`
- Are a subset of `iterables`
- Are much more memory efficient than lists and other iterables.

## Basic Generator Syntax

To create a generator, you use a function with the `yield` keyword instead of `return`.

- When the generator is executed in a `next()` function, the generator returns the value at `yield` and pauses.
- The next time the generator is invoked, it resumes execution from the `yield` and continues its execution

Let's imagine a simple generator that simulates a journey through Middle Earth, yielding names of places as Frodo and Sam go on their quest:

```python
def middle_earth_journey():
    yield "Hobbiton"
    yield "Bree"
    yield "Rivendell"
    yield "Moria"
    yield "Lothlorien"
    yield "Mordor"

# Create the generator object
journey = middle_earth_journey()

# Using the generator
for place in journey:
    print(place)
```

```python
def is_prime(num):
    """Checks if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_generator():
    """Generator to yield prime numbers one by one."""
    num = 2
    while True:
        if is_prime(num):
            yield num  # This is a prime number, so yield it
        num += 1

# Usage
primes = prime_generator()
for _ in range(10):  # Get first 10 prime numbers
    print(next(primes))
```

```python
def fibonacci_generator():
    """Generator to yield Fibonacci numbers one by one."""
    a, b = 0, 1
    while True:
        yield a  # Yield the current Fibonacci number
        a, b = b, a + b  # Calculate the next Fibonacci number

# Usage
fib = fibonacci_generator()
for _ in range(10):  # Get first 10 Fibonacci numbers
    print(next(fib))
```

```python
def geometric_progression(a, r):
    """Generator to yield terms of a geometric progression."""
    while True:
        yield a  # Yield the current term
        a *= r  # Calculate the next term

# Usage
geo_prog = geometric_progression(1, 2)  # Start with 1 and common ratio 2
for _ in range(10):  # Get first 10 terms
    print(next(geo_prog))
```

## Generator Expressions

You can also create a generator using a syntax similar to [list comprehensions](python_data-types_lists.md#list-comprehensions). Here's an example to create a generator of squares for even numbers in a given range:

```python
squares = (x*x for x in range(10) if x % 2 == 0)

for square in squares:
    print(square)
```

## `send` and `throw`

Generators have methods to interact with the values they produce:

- `send`: Resumes the generator and sends a value that becomes the result of the current `yield` expression.
- `throw`: Used to raise an exception inside the generator.

Imagine a generator for a D&D adventure where a character encounters various creatures:

```python
def dnd_adventure():
    encounter = yield "You enter a dark cave."
    while encounter:
        if encounter == "dragon":
            yield "You face a mighty dragon!"
        elif encounter == "goblin":
            yield "A goblin jumps out!"
        else:
            yield "Unknown creature!"
        encounter = yield None

adventure = dnd_adventure()
print(next(adventure))  # Starts the generator

response = adventure.send("dragon")
print(response)

response = adventure.send("goblin")
print(response)
```

## Why Use Generators?

1. **Memory Efficiency**: Since generators produce items only one at a time, they can represent an infinite stream of data.
2. **Lazy Evaluation**: Data is only generated when required, which can lead to performance improvements.

## Generator Limitations

1. Generators can only be iterated once.
2. You cannot access elements by index, like you would in a list.

## Resources / References

- [Real Python - How to Use Generators and Yield in Python](https://realpython.com/introduction-to-python-generators/)
