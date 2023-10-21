# Python Command Line Arguments

A [**command-line interface (CLI)**](https://en.wikipedia.org/wiki/Command-line_interface) provides a way for a user to interact with a program running in a text-based [shell](https://en.wikipedia.org/wiki/Shell_%28computing%29) interpreter.

Some examples of shell interpreters are [Bash](https://en.wikipedia.org/wiki/Bash_%28Unix_shell%29) on Linux or [Command Prompt](https://en.wikipedia.org/wiki/Cmd.exe) on Windows.

A command-line interface is enabled by the shell interpreter that exposes a [command prompt](https://en.wikipedia.org/wiki/Command-line_interface#Command_prompt).

A command line interface can be characterized by the following elements:

- A **command** or program
- Zero or more command line **arguments**
- An **output** representing the result of the command
- Textual documentation referred to as **usage** or **help**

## Reading CLI Arguments w/ sys.argv

`sys.argv` returns a list of CLI arguments

- `argv[0]` contains the name of the program passed into Python
- `argv[1:]` (the rest of the list), contains any and all Python command-line arguments passed to the program

**NOTE:** To use `sys.argv`, you need to `import sys` from the Python Standard Library.

```python
# argv.py
import sys # Import Internal Python module "sys"

# Extract name of the python program by accessing 1st element of the sys.argv list
program_name = sys.argv[0]
print(f"Name of the script      : sys.argv[0]={program_name}")

# Display Python CLI args passed to the executing Python script
args = sys.argv[1:]
print(f"Arguments of the script : sys.argv[1:]={args}")
```

```bash
# Execute above argv.py Python script
python argv.py un deux trois quatre

# CLI Output
# Name of the script      : sys.argv[0]='argv.py'
# Arguments of the script : sys.argv[1:]=['un', 'deux', 'trois', 'quatre']
```

## Escaping Whitespace Characters

On Linux, whitespaces can be escaped by doing one of the following:

1. **Surrounding** the arguments with single quotes (`'`)
2. **Surrounding** the arguments with double quotes (`"`)
3. **Prefixing** each space with a backslash (`\`)

## Handling CLI Errors

It is a good idea to use a `try / except` block to handle exceptions in case an expected CLI argument is not passed during execution

```python
# reverse_exec.py
import sys

try:
    arg = sys.argv[1]
except IndexError:
    # If argument is not passed in, then IndexError is raised
    raise SystemExit(f"Usage: {sys.argv[0]} <string_to_reverse>")

# Print reversed argument to console
print(arg[::-1])
```

## Methods for Parsing Python Command Line Arguments

### Parsing CLI Arguments w/ array methods

```python
# cul.py

import sys

# Collect all options by filtering on any Python CLI arguments starting with a hyphen (-)
opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]

# Assemble python programming arguments by filtering out the options
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

if "-c" in opts:
    # Capitalize arguments
    print(" ".join(arg.capitalize() for arg in args))
elif "-u" in opts:
    # Convert the arguments to uppercase
    print(" ".join(arg.upper() for arg in args))
elif "-l" in opts:
    # Conver the arguments to lowercase
    print(" ".join(arg.lower() for arg in args))
else:
    raise SystemExit(f"Usage: {sys.argv[0]} (-c | -u | -l) <arguments>...")
```

```bash
$ python cul.py -c un deux trois
Un Deux Trois
```

### Parsing CLI Arguments w/ Regular Expressions

```python
# main.py

import sys
import re

# Define a function to parse cli arguments from a string
def parse_cli_args(cli_args):
    pattern = r'(?:-{1,2}(\w+)(?:=(\w+))?)'
    args = {}
    matches = re.findall(pattern, cli_args)
    for match in matches:
        arg, value = match
        args[arg] = value or True
    return args

if __name__ == '__main__':
    # Join the cli arguments into a string
    cli_args = ' '.join(sys.argv[1:])
    parsed_args = parse_cli_args(cli_args)
    print(parsed_args)
```

```bash
$ python main.py -f foo.txt --bar=123 --baz
# {'f': 'foo.txt', 'bar': '123', 'baz': True}
```

## CLI Parsers from Python Standard Library

The `argparse` Python Standard Library can be used to parse CLI arguments from the command line

[Python Docs - argparse](https://docs.python.org/3/library/argparse.html)

## References

- [Real Python - Python Command-Line Arguments](https://realpython.com/python-command-line-arguments/)
- [Python Docs - argparse](https://docs.python.org/3/library/argparse.html)
- [The many ways to pass code to Python from the terminal](https://snarky.ca/the-many-ways-to-pass-code-to-python-from-the-terminal/)

## APPENDIX A: Anatomy of Python Command-Line Arguments

Python command-line arguments are a subset of the command-line interface. They can be composed of different types of arguments:

1. **Options** modify the behavior of a particular command or program.
2. **Arguments** represent the source or destination to be processed.
3. **Subcommands** allow a program to define more than one command with the respective set of options and arguments.

### Standards

A few available **standards** provide some definitions and guidelines to promote consistency for implementing commands and their arguments. These are the main UNIX standards and references:

- [POSIX Utility Conventions](http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap12.html)
- [GNU Standards for Command Line Interfaces](https://www.gnu.org/prep/standards/standards.html#Command_002dLine-Interfaces)
- [docopt](http://docopt.org/)

The standards above define guidelines and nomenclatures for anything related to programs and Python command-line arguments. The following points are examples taken from those references:

- **POSIX**:
  - A program or utility is followed by options, option-arguments, and operands.
  - All options should be preceded with a hyphen or minus (`-`) delimiter character.
  - Option-arguments should not be optional.
- **GNU**:
  - All programs should support two standard options, which are `--version` and `--help`.
  - Long-named options are equivalent to the single-letter Unix-style options. An example is `--debug` and `-d`.
- **docopt**:
  - Short options can be stacked, meaning that `-abc` is equivalent to `-a -b -c`.
  - Long options can have arguments specified after a space or the equals sign (`=`). The long option `--input=ARG` is equivalent to `--input ARG`.

### Options

An **option**, sometimes called a **flag** or a **switch**, is intended to modify the behavior of the program

Example. `ls -la` => `-l` & `-a` are options which modify the output of the `ls` command

An **option** can take an argument, which is called an **option-argument**

### Arguments

The **arguments** are also called **operands** or [parameters](https://en.wikipedia.org/wiki/Parameter#Computing) in the POSIX standards. The arguments represent the source or the destination of the data that the command acts on. For example, the command [`cp`](https://en.wikipedia.org/wiki/Cp_%28Unix%29), which is used to copy one or more files to a file or a directory, takes at least one source and one target (these are the arguments):

```bash
$ ls main
main

$ cp main main2

$ ls -lt
main
main2
...
```
