# Python Files and Input / Output

Python has several built-in modules and functions for handling files. These functions are spread out over several modules such as `os`, `os.path`, `shutil`, and `pathlib`, to name a few.

## Opening and Closing Files

### open() and close() functions

> It is recommended to use [`with open(...) as ... :`](python_files_io.md#with-open-as) pattern instead of above

> **ALWAYS** close a file (via `close(<file_object>)`) after file operations are complete!

Use the `open()` function to open up a file in Python

- Returns a file object which can be used to read, write, or append to the file

```python
open(filename, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
```

Let's break down the parameters:

1. **filename**: The name of the file you want to open.
2. **mode**: Specifies the mode in which the file should be opened. The common modes are:

   - `'r'`: Read mode (default). Open the file for reading.
   - `'w'`: Write mode. Open the file for writing (creates a new file or truncates an existing file).
   - `'a'`: Append mode. Open the file for writing (creates a new file or appends to an existing file).
   - `'b'`: Binary mode. Read or write the file in binary format, e.g., `'rb'` or `'wb'`.
   - `'x'`: Exclusive creation mode. Opens the file for exclusive creation, failing if the file already exists.
   - `'t'`: Text mode (default). This is used in combination with other modes, like `'rt'`.

   Modes can be combined. For instance, `'rb'` means read in binary mode.

3. **buffering**: Optional. If set to 0, no buffering will take place. If set to 1, line buffering will be performed while accessing the file. If set to a number > 1, buffering will happen with the indicated buffer size. If negative (default), the system default is used.
4. **encoding**: Optional. The name of the encoding used to decode or encode the file. E.g., `'utf-8'`, `'latin-1'`, etc. If not specified, the default system encoding is used.
5. **errors**: Optional. Specifies the action to take upon decoding error. Common values are `'strict'`, `'ignore'`, and `'replace'`.
6. **newline**: Optional. Controls how universal newlines mode works. Can be `None`, `''`, `'\n'`, `'\r'`, or `'\r\n'`.
7. **closefd**: If set to `False` and a file descriptor rather than a filename was given, the underlying file descriptor will be kept open when the file is closed. This parameter is irrelevant if a filename is given.
8. **opener**: Optional. A custom opener can be used by passing an `opener` function. The underlying file descriptor for the file object is then obtained by calling the opener with `(filename, flags)`.

```python
# =======================
# Open a file for reading
# =======================
f = open('filename.txt', 'r')
```

```python
# =======================
# Open a file for writing
# =======================
f = open('filename.txt', 'w')
```

```python
# ==============================
# Open a binary file for reading
# ==============================
f = open('filename.bin', 'rb')
```

```python
# ==================================
# Open a file with a custom encoding
# ==================================
f = open('filename.txt', 'r', encoding='utf-8')
```

**IMPORTANT:** After performing operations on the file, it's important to close it using the `close()` method:

```python
# =====================
# Closing a file object
# =====================
f.close()
```

However, it's a best practice to use the [`with`](python_files_io.md#with-open-as) statement when working with files

### with open(...) as ... :

Using the `with` statement alongside the `open()` function is a best practice in Python for file handling.

- Ensures that the file is properly and safely handled, even if exceptions occur within the `with` block.
- This pattern is called a _context manager_.

Benefits of using `with open()...`:

1. **Automatic File Closing**: The file is automatically closed when the `with` block is exited, even if the block is exited due to an error. This ensures that resources are freed up and reduces the risk of file corruption.

2. **Exception Handling**: If an exception occurs within the `with` block, the file is still safely closed, ensuring that the code is more robust and less prone to leaving files open unintentionally.

3. **Readability**: The use of the `with` statement clearly delineates the scope where the file is being accessed, making it easier to understand the context of file operations.

```python
# ==============
# Reading a file
# ==============
with open('filename.txt', 'r') as file:
    content = file.read()
    # process content or perform other operations
# file is automatically closed here
```

```python
# =================
# Writing to a file
# =================
with open('filename.txt', 'w') as file:
    file.write("Hello, World!")
# file is automatically closed here
```

You can open multiple files in the same `with` block:

```python
# =======================
# Handling multiple files
# =======================
with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    data = infile.read()
    # maybe process or transform data
    outfile.write(data)
# both infile and outfile are automatically closed here
```

Files are iterable, meaning you can loop through each line in a file:

```python
# ========================
# Iterating through a file
# ========================
with open('filename.txt', 'r') as file:
    for line in file:
        print(line.strip())  # strip() removes the newline character at the end
```

## Reading Files

### Iterating through the File Object

The file object returned by the `open()` function is iterable

- Use it to iterate through each line of the file

```python
with open('filename.txt', 'r') as file:
    for line in file:
        print(line.strip())  # strip() removes newline characters and trailing/leading whitespaces
```

### Reading Methods

There are several methods which can be used to read data from a file object

- `read()` => Reads entire file content and returns it as a single string
- `readline()` => Reads the next line from the file. Invoking the method again will read the subsequent line.
- `readlines()` => Reads entire file content and returns a list of line strings

```txt
Line 1
Line 2
Line 3
```

```python
# ===================================
# Read entire file contents w/ read()
# ===================================
with open('filename.txt', 'r') as f:
    content = f.read()
    print(content)  # 'Line 1\nLine 2\nLine 3\n'
```

```python
# ===================================
# Read individual lines w/ readline()
# ===================================
with open('filename.txt', 'r') as f:
    line1 = f.readline()
    line2 = f.readline()
    line3 = f.readline()
    print(line1, end='')  # Line 1
    print(line2, end='')  # Line 2
    print(line3, end='')  # Line 3
```

```python
# =============
# f.readlines()
# =============
with open('filename.txt', 'r') as f:
    lines = f.readlines()
    print(lines)  # ['Line 1\n', 'Line 2\n', 'Line 3\n']
```

```python
# ========================
# Iterating w/ readlines()
# ========================
with open('filename.txt', 'r') as f:
    lines = f.readlines()

    for line in lines:
        print(line.strip())  # strip() removes newline characters and trailing/leading whitespaces
```

### Example of Reading Files w/ open()

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

### Example of reading files w/ with statement

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

## Changing File Position w/ seek()

The `seek()` method is used to change the current file position and takes two parameters:

- `offset` -> The number of bytes to move the cursor
- `whence` -> (optional) determines from where the offset is calculated (defaults to 0)
  - `0` (default): Offset is calculated from the beginning of the file
  - `1`: Offset is calculated from the current file position
  - `2`: Offset is calculated from the end of the file

When you use `file.seek(0)`, you are moving the file's current cursor position back to the beginning of the file.

- Useful when you've read a file to the end and want to read it again from the start

```python
with open('filename.txt', 'r') as file:
    content1 = file.read()
    file.seek(0)  # Move cursor back to the start of the file.
    content2 = file.read()

# content1 and content2 will have the same content in this case.
```

## Writing to Files

To write to a file, use the `open()` function with the `w` mode to open the file, then use the `write(<file_object>)` method to write to the file object

**CAUTION:** Using `w` mode will overwrite the contents of the entire file.

- If you want to append to the file, use `a` mode instead

```python
# =========================================
# Write to (and overwrite contents of) file
# =========================================
with open('filename.txt', 'w') as file:
    file.write('Hello, World!')  # Existing file contents are overwritten
```

```python
# =========================
# Append contents to a file
# =========================
with open('filename.txt', 'a') as file:
    file.write('\nAppended text.')
```

## Read / Write Data to .txt Files

```python
FILE_NAME = "lotr_characters.txt"

def create_character(name, race, role):
    """
    Create a new character in the TXT file.

    Args:
    - name (str): Name of the character.
    - race (str): Race of the character.
    - role (str): Role of the character in the story.
    """
    with open(FILE_NAME, 'a') as file:
        file.write(f"{name},{race},{role}\n")

def read_characters():
    """
    Read and display all the characters from the TXT file.
    """
    try:
        with open(FILE_NAME, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No characters found.")

def update_character(name, new_name, new_race, new_role):
    """
    Update the details of an existing character.

    Args:
    - name (str): Name of the character to update.
    - new_name (str): New name for the character.
    - new_race (str): New race for the character.
    - new_role (str): New role for the character.
    """
    characters = []
    found = False

    try:
        with open(FILE_NAME, 'r') as file:
            for line in file:
                char_name, char_race, char_role = line.strip().split(',')
                if char_name == name:
                    characters.append(f"{new_name or char_name},{new_race or char_race},{new_role or char_role}")
                    found = True
                else:
                    characters.append(line.strip())

        if not found:
            print(f"Character with name {name} not found.")
            return

        with open(FILE_NAME, 'w') as file:
            for char in characters:
                file.write(f"{char}\n")

    except FileNotFoundError:
        print(f"Character with name {name} not found.")

def delete_character(name):
    """
    Delete a character from the TXT based on the name.

    Args:
    - name (str): Name of the character to delete.
    """
    characters = []
    found = False

    try:
        with open(FILE_NAME, 'r') as file:
            for line in file:
                char_name = line.strip().split(',')[0]
                if char_name != name:
                    characters.append(line.strip())
                else:
                    found = True

        if not found:
            print(f"Character with name {name} not found.")
            return

        with open(FILE_NAME, 'w') as file:
            for char in characters:
                file.write(f"{char}\n")

    except FileNotFoundError:
        print(f"Character with name {name} not found.")

if __name__ == "__main__":
    # Main loop for user interactions.
    while True:
        choice = input("Choose an operation (C: Create, R: Read, U: Update, D: Delete, Q: Quit): ").upper()

        if choice == "C":
            name = input("Enter character name: ")
            race = input("Enter character race: ")
            role = input("Enter character role: ")
            create_character(name, race, role)

        elif choice == "R":
            read_characters()

        elif choice == "U":
            name = input("Enter character name to update: ")
            new_name = input("Enter new name or leave blank to keep the same: ")
            new_race = input("Enter new race or leave blank to keep the same: ")
            new_role = input("Enter new role or leave blank to keep the same: ")
            update_character(name, new_name or name, new_race or race, new_role or role)

        elif choice == "D":
            name = input("Enter character name to delete: ")
            delete_character(name)

        elif choice == "Q":
            break
```

## Read / Write JSON Data

Python has a built-in module called `json` that lets you encode and decode JSOn data

```python
# ===========================
# Writing Data to a JSON file
# ===========================
import json

data = {'name': 'John', 'age': 30, 'city': 'New York'}
with open('data.json', 'w') as file:
    json.dump(data, file)
```

```python
# ====================
# Reading in JSON data
# ====================
import json

with open('data.json', 'r') as file:
    data = json.load(file) # reads file and turns it into a dictionary
    print(data)
```

```python
import json

FILE_NAME = "lotr_characters.json"

def create_character(name, race, role):
    """
    Create a new character in the JSON file.

    Args:
    - name (str): Name of the character.
    - race (str): Race of the character.
    - role (str): Role of the character in the story.
    """
    characters = []
    try:
        with open(FILE_NAME, 'r') as file:
            characters = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        pass

    characters.append({
        "name": name,
        "race": race,
        "role": role
    })

    with open(FILE_NAME, 'w') as file:
        json.dump(characters, file)

def read_characters():
    """
    Read and display all the characters from the JSON file.
    """
    try:
        with open(FILE_NAME, 'r') as file:
            characters = json.load(file)
            for char in characters:
                print(char)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No characters found.")

def update_character(name, new_name, new_race, new_role):
    """
    Update the details of an existing character.

    Args:
    - name (str): Name of the character to update.
    - new_name (str): New name for the character.
    - new_race (str): New race for the character.
    - new_role (str): New role for the character.
    """
    try:
        with open(FILE_NAME, 'r') as file:
            characters = json.load(file)

        for char in characters:
            if char['name'] == name:
                char['name'] = new_name or char['name']
                char['race'] = new_race or char['race']
                char['role'] = new_role or char['role']

        with open(FILE_NAME, 'w') as file:
            json.dump(characters, file)
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"Character with name {name} not found.")

def delete_character(name):
    """
    Delete a character from the JSON based on the name.

    Args:
    - name (str): Name of the character to delete.
    """
    try:
        with open(FILE_NAME, 'r') as file:
            characters = json.load(file)

        characters = [char for char in characters if char['name'] != name]

        with open(FILE_NAME, 'w') as file:
            json.dump(characters, file)
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"Character with name {name} not found.")

if __name__ == "__main__":
    # Main loop for user interactions.
    while True:
        choice = input("Choose an operation (C: Create, R: Read, U: Update, D: Delete, Q: Quit): ").upper()

        if choice == "C":
            name = input("Enter character name: ")
            race = input("Enter character race: ")
            role = input("Enter character role: ")
            create_character(name, race, role)

        elif choice == "R":
            read_characters()

        elif choice == "U":
            name = input("Enter character name to update: ")
            new_name = input("Enter new name or leave blank to keep the same: ")
            new_race = input("Enter new race or leave blank to keep the same: ")
            new_role = input("Enter new role or leave blank to keep the same: ")
            update_character(name, new_name or name, new_race or race, new_role or role)

        elif choice == "D":
            name = input("Enter character name to delete: ")
            delete_character(name)

        elif choice == "Q":
            break
```

## Read / Write CSV Data

Python's `csv` module helps in reading from and writing to CSV files

- [Teclado - CSV Files w/ Python - Reading and Writing](https://www.youtube.com/watch?v=W7QByFjVom8)
- [Real Python - Reading and Writing CSV Files in Python](https://realpython.com/python-csv/)

```python
# =========================
# Writing data to CSV files
# =========================
import csv

rows = [['Name', 'Age'], ['Alice', 28], ['Bob', 24]]

with open('data.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(rows)
```

```python
# ===========================
# Reading data from CSV files
# ===========================
import csv

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

```python
import csv
import os

FILE_NAME = "lotr_characters.csv"

def create_character(name, race, role):
    """
    Create a new character in the CSV file.

    Args:
    - name (str): Name of the character.
    - race (str): Race of the character.
    - role (str): Role of the character in the story.
    """
    with open(FILE_NAME, mode="a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, race, role])

def read_characters():
    """
    Read and display all the characters from the CSV file.
    """
    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def update_character(name, new_name, new_race, new_role):
    """
    Update the details of an existing character.

    Args:
    - name (str): Name of the character to update.
    - new_name (str): New name for the character.
    - new_race (str): New race for the character.
    - new_role (str): New role for the character.
    """
    characters = []
    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == name:
                characters.append([new_name, new_race, new_role])
            else:
                characters.append(row)

    with open(FILE_NAME, mode="w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(characters)

def delete_character(name):
    """
    Delete a character from the CSV based on the name.

    Args:
    - name (str): Name of the character to delete.
    """
    characters = []
    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != name:
                characters.append(row)

    with open(FILE_NAME, mode="w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(characters)

if __name__ == "__main__":
    # Main loop for user interactions.
    while True:
        choice = input("Choose an operation (C: Create, R: Read, U: Update, D: Delete, Q: Quit): ").upper()

        if choice == "C":
            name = input("Enter character name: ")
            race = input("Enter character race: ")
            role = input("Enter character role: ")
            create_character(name, race, role)

        elif choice == "R":
            read_characters()

        elif choice == "U":
            name = input("Enter character name to update: ")
            new_name = input("Enter new name or leave blank to keep the same: ")
            new_race = input("Enter new race or leave blank to keep the same: ")
            new_role = input("Enter new role or leave blank to keep the same: ")
            update_character(name, new_name or name, new_race or race, new_role or role)

        elif choice == "D":
            name = input("Enter character name to delete: ")
            delete_character(name)

        elif choice == "Q":
            break
```

## Read / Write Binary Files

Use the `rb` or `wb` modes with `open()` to work with binary data

```python
# ============================
# Writing data to binary files
# ============================
with open('data.bin', 'wb') as file:
    file.write(b'Binary data here')
```

```python
# ==============================
# Reading data from binary files
# ==============================
with open('data.bin', 'rb') as file:
    data = file.read()
print(data)
```

## Handling Exceptions when Working w/ Files

When dealing with file operations, it's crucial to handle exceptions that may occur, like `FileNotFoundError`. Use [`try-except`](python_error-handling.md#try--except--else--finally) blocks for handling these types of errors.

```python
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
    print(content)
except FileNotFoundError:
    print("The file does not exist.")
```

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
- [Teclado - CSV Files w/ Python - Reading and Writing](https://www.youtube.com/watch?v=W7QByFjVom8)
- [Real Python - Reading and Writing CSV Files in Python](https://realpython.com/python-csv/)
