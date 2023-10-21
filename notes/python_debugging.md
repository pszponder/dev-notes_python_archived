# Python Debugging

```python
import pdb # import the python debugger (built-in python module)

def add(num1, num2):
    # instead of printing,
    #  open up interactive cli at this position
    pdb.set_trace()
    return num1 + num2

add(4, 'asdfs')
```

When inside the `pdb` console, type `help` to get a list of commands you can use for debugging

## References

- [Official Docs - Python Debugger](https://docs.python.org/3/library/pdb.html)
