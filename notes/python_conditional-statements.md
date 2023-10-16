# Conditional Statements in Python

Python supports the usual logical conditions from mathematics:

- Equals: `a == b`
- Not Equals: `a != b`
- Less than: `a < b`
- Less than or equal to: `a <= b`
- Greater than: `a > b`
- Greater than or equal to: `a >= b`

```python
if condition_1:
    # Code for condition 1
elif condition_2:
    # Code for condition 2
else:
    # Code if nothing else above triggered
```

```python
age = 18

if age < 20:
    print("You're a teenager!")
elif age == 20:
    print("You just hit 20!")
else:
    print("You're above 20!")
```
