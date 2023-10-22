# Variables in Python

What is a Variable? - Variables are like labels for values.

We can store a value and give it a name so that we can:

- Refer back to it later
- Use that value to do ... stuff
- Change it later

## Defining a Variable in Python

```python
# variable_name = value
age = 48
score = 0
full_name = "Arthur Pendragon"
```

**NOTE:** Python Variables don't use any types or keywords

- Unlike JavaScript or C#, Python variables do not need to start with `const`, `let`, or `var`.
- Python variables don't need a type specified either.
- All you need to do is to create a new variable name and initialize it.

## Multiple Variable Assignment on one line

You can assign multiple variables on the same line in Python using the following trick:

```python
# Assign a to 1, b to 2, c to 3
a, b, c = 1, 2, 3

print(a) # 1
print(b) # 2
print(c) # 3
```

This is the same as:

```python
a = 1
b = 2
c = 3

print(a) # 1
print(b) # 2
print(c) # 3
```

## Python Variable Naming Conventions

Python variables:

- snake_case
- Start with lowercase or underscore
- Letters, number, underscores
- Case sensitive

Python variables **CANNOT**:

- Begin with numbers
- Contain spaces (use underscores, a.k.a., snake-case)
- Use reserved words / keywords ([Python Keywords](https://www.w3schools.com/python/python_ref_keywords.asp)) such as `False`, `True`, etc.

**NOTE:** Look up list of python reserved keywords

- `help("keywords")`

## Constants

By convention, a constant is written in all capital letters.

```python
# This is a constant
# the program should not change the value of this variable
PI = 3.14
```

## Assignment expression (Walrus) Operator

The `walrus` operator is defined by `:=`

```python
(<var_name> := <value>)
```

It can be used to assign a value to a variable within an expression and can be useful in conditional logic.

**NOTE:** `Walrus Operator` (`:=`)

- The `walrus operator` is a way to assign a value to a variable as part of an expression, rather than as a separate statement.
- The `walrus operator` was introduced in Python v3.8

**NOTE:** When to use the `walrus operator`

1. Simplifying code that would otherwise require multiple lines or variables.
2. Avoiding the repetition of expensive or complex computations.
3. Improving the readability of code by making the relationship between values and variables more explicit.

Case 1: Simplifying code:

```python
# without walrus operator
x = input()
if x.isdigit():
    x = int(x)
else:
    x = None

# with walrus operator
if (x := input()).isdigit():
    x = int(x)
else:
    x = None
```

Case 2: Avoiding Repetition:

```python
# without walrus operator
while True:
    x = input()
    if not x:
        break
    if len(x) > 10:
        print("Too long!")
        continue
    # do something with x

# with walrus operator
while (x := input()):
    if len(x) > 10:
        print("Too long!")
        continue
    # do something with x
```

Case 3: Improving Readability:

```python
# without walrus operator
for i in range(10):
    x = i * 2
    if x > 5:
        print(x)

# with walrus operator
for i in range(10):
    if (x := i * 2) > 5:
        print(x)
```

## References

- [Real Python - Walrus Operator](https://realpython.com/python-walrus-operator/)
