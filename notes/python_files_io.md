# Python Files and Input / Output

Python has several built-in modules and functions for handling files. These functions are spread out over several modules such as `os`, `os.path`, `shutil`, and `pathlib`, to name a few.

## Reading Files w/ open & close function

**CAUTION:** It is recommended to use [`with open(...) as ...:`](python_files_io.md#read--write--edit-with-the-with-open-as--pattern) pattern instead of above

```python
# Create a file object from the passed in file
# NOTE1: pass in the relative file path to the file
# NOTE2: After completing file operations, don't forget to close the file!
my_file = open("hello.txt")

# Read in the contents of the file
# NOTE: Once the item is read, it cannot be re-read without resetting the cursor position
file_contents = my_file.read()
print(file_contents)  # hello world...

# Attempt to read the file again
print(my_file.read())  # Doesn't print anything (cursor is at end of file object)

# Reset the cursor to the start of the file object (enables to re-read file)
my_file.seek(0)  # reset cursor position back to the start

print(my_file.read())  # hello world...

# Read the file one line at a time
# NOTE: after we get to the end of the file, need to reset the cursor position if we want to re-read
line1 = my_file.readline()
line2 = my_file.readline()
line3 = my_file.readline()
print(line1)  # hello world
print(line2)  # how
print(line3)  # are you?

my_file.seek(0)  # reset cursor position back to the start

# Read in the entire contents of a file, line by line
#  and return an array of lines
lines = my_file.readlines()
print(lines)  # ['hello world\n', 'how\n', 'are you?']

# Close the opened file
my_file.close()
```

## Read / Write / Edit with the "with open(...) as ...:" pattern

Reading and writing data to files using Python is pretty straightforward.

To do this, you must first open files in the appropriate mode. `open()` takes a filename and a mode as its arguments

Use the `with open(...) as ...:` pattern to open a file as a specified file object, perform any operations and automatically close the file when complete

```python
# Create a file object (named my_file) from the passed in file
# NOTE: pass in the relative file path to the file
with open("hello.txt", mode="r") as my_file:
    # Read in the contents of the file
    # NOTE: Once the item is read,
    # it cannot be re-read without resetting the cursor position
    file_contents = my_file.read()
    print(file_contents)  # hello world...

    # Attempt to read the file
    # Doesn't print anything
    # (cursor is at end of file object) again
    print(my_file.read())

    # Reset the cursor to the start of the file object
    # (enables to re-read file)
    my_file.seek(0)  # reset cursor position back to the start
    print(my_file.read())  # hello world...

    # Read the file one line at a time
    # NOTE: after we get to the end of the file,
    #  need to reset the cursor position if we want to re-read
    line1 = my_file.readline()
    line2 = my_file.readline()
    line3 = my_file.readline()
    print(line1)  # hello world
    print(line2)  # how
    print(line3)  # are you?

    my_file.seek(0)  # reset cursor position back to the start

    # Read in the entire contents of a file, line by line
    #  and return an array of lines
    lines = my_file.readlines()
    print(lines)  # ['hello world\n', 'how\n', 'are you?']
```

### Reading from a file

To open a file in `read-only` mode, pass in the `r` argument into the `open()` function

```python
# Pass in 'r' argument to open the file in read only mode
with open('data.txt', mode='r') as f:
    data1 = f.read()
    f.seek(0)

    data2 = f.readline()
    f.seek(0)

    data3 = f.readlies()
```

### Writing to a file

To open a file in `write` mode, pass in the `w` argument into the `open()` function

```python
# Write data to the specified file
with open('data.txt', mode='w') as f:
    data = 'some data to be written to the file'
    f.write(data)
```

**CAUTION:** Consecutive writes overwrite current file contents

### Read & Write to a file

To open a file in `read + write` mode, pass in the `r+` argument into the `open()` function

```python
# Read and write the specified file
with open('data.txt', mode='r+') as f:
    # Read from file
    print(f.read())
    print(f.read())

    # Write to the file
    data = 'some data to be written to the file'
    f.write(data)

    # Re-read the file
    f.seek(0)
    print(f.read())
```

**CAUTION:** Consecutive writes overwrite current file contents

### Append to the end of the file

Use the `a` mode to allow file appending. Consecutive writes add to the file instead of overwriting it

```python
# Appen data to the specified file in append mode
with open('data.txt', mode='a') as f:
    data = 'some data to be written to the file'
    f.write(data)
```

## File Paths

The `pathlib` python core library module can be used to work with file paths

[Object-Oriented filesystem paths - pathlib](https://docs.python.org/3/library/pathlib.html)

## File IO Errors

Can use [try/except blocks](python_error-handling.md#try--except--else--finally) to handle errors such as `FileNotFoundError` or `IOError`

```python
try:
    with open('you_cant_see_me.txt', mode='r') as my_file:
        print(myfile.read())
except FileNotFoundError as err:
    print('file does not exist')
    raise err
except IOError as err:
    print('IO Error')
    raise err
```

## References

- [Real Python - Working with Files in Python](https://realpython.com/working-with-files-in-python/)
- [Real Python - Reading and Writing Files in Python](https://realpython.com/read-write-files-python/)
- [Dan Bader - Working with File I/O in Python](https://dbader.org/blog/python-file-io)
- [Object-Oriented filesystem paths - pathlib](https://docs.python.org/3/library/pathlib.html)
- [Why you should be using pathlib instead of os.path](https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/)
