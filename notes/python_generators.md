# Python Generators

- `Generators` allow us to generate a sequence of values over time
- `Generators` allow us to use special keywords `pause` and `resume`
- `Generators` are a subset of `iterables`
- `Generators` are much more memory efficient than lists and other iterables.

The `range()` function is actually an example of a generator. It does not actually create an iterable sequence of values, instead, it returns a single incrementing value each time it is called

```python
# Define a generator function
def generator_func(num):
    for i in range(num):
       # Return i and pause function
       #  until function is invoked again by "next()"
        yield i

# Every time we invoke generator_func(1000) in the for loop
# the generator_func will return a new value
for item in generator_func(1000):
    print(item)
```

```python
# Define a generator function
def generator_func(num):
    for i in range(num):
        # Return i * 2 and pause function
        #  until function is invoked again by "next()"
        yield i * 2


g = generator_func(100)
print(g)  # <generator object generator_func at 0x7ff914f1f780>

# Each time the next() method is invoked on the generator function
#  the value that the generator function returns is incremented

a = next(g)  # increment the value returned by generator_func
print(a)  # 0 (since 0 * 2 = 0)

b = next(g)  # increment the value returned by generator_func
print(b)  # 2 (since 1 * 2 = 2)

c = next(g)  # increment the value returned by generator_func
print(c)  # 4 (since 2 * 2 = 4)

d = next(g)  # increment the value returned by generator_func
print(d)  # 6 (since 3 * 2 = 6)
```

```python
# Define a generator function which mimics a for loop
# This mimics how a for loop runs under the hood
def iter_for(iterable):
    # "iter" enables the invocation of "next()" in the passed in iterable
    iterator = iter(iterable)

    while True:
        try:
            # Add additional logic to execute here
            print(iterator)
            next(iterator)
        except StopIteration:
            # StopIteration is thrown by a generator when end of range is reached
            break


iter_for([1, 2, 3])
```

```python
# This class, when instantiated, mimics the logic of the range generator function
class CustomRange:
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    # Invoke this method when the next() method on the class instance is called
    def __next__(self):
        if CustomRange.current < self.last:
            num = CustomRange.current
            CustomRange.current += 1
            return num
        raise StopIteration


# Instantiate the CustomRange function
custom_range = CustomRange(0, 100)

# Use the generator instance to mimic the range function
for i in custom_range:
    print(i)  # prints sequence of values from 0 through 99
```

```python
# Use generators to create the fibonacci sequence
def fib(number):
    # Devine initial values
    a = 0
    b = 1

    for i in range(number):
        yield a  # return value of a when "next()" function is invoked

        # Update values of a and b
        temp = a
        a = b
        b = temp + b


# Use the fib generator function to generate 20 values of the fibonacci sequence
for x in fib(20):
    print(x)


# Use lists to generate the fibonacci sequence
def fib2(number):
    a = 0
    b = 1
    result = []
    for i in range(number):
        result.append(a)
        # Update values of a and b
        temp = a
        a = b
        b = temp + b
    return result


print(fib2(20))
```

## Resources / References

- [Real Python - How to Use Generators and Yield in Python](https://realpython.com/introduction-to-python-generators/)
