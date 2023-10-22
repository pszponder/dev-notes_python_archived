# Setting up a Python Project

## Quick Start Summary

```bash
# Create Virtual Environment
python -m venv .venv --upgrade-deps --clear

# Activate Virtual Environment
. .venv/bin/activate

# Create requirements.txt (after installing dependencies)
pip freeze > requirements.txt

# Create a new main.py file
echo -e 'if __name__ == "__main__":\n    pass' > main.py
```

If you are starting work on an existing project...

```python
# Activate Virtual Environment
. .venv/bin/activate

# Install python dependencies (as applicable)
pip install -r requirements.txt
```

Once you are done working with your project...

```bash
# Deactivate Virtual Environment
deactivate
```

## Setup a Virtual Environment

Always setup a [virtual environment](python_virtual-environments.md) when creating a new python project which will be using external dependencies.

## Project Entry Point

A typical Python project will have a `main.py` file which will serve as the project entry point.

In conjunction with this, the `main.py` file will typically have an special if statement to execute code only if the `main.py` is actually executed.

- [More info on `__name__ == __main__`](python_modules-and-packages.md#__name__--__main__)

```python
# main.py

if __name__ == '__main__':
    # Your logic here
    # This logic only runs if main.py is invoked directly
    # using "python main.py"
```

## Create requirements.txt file

If you install 3rd party packages, create a `requirements.txt` file to hold a list of installed modules

```bash
pip freeze > requirements.txt
```

You will need to re-run this command whenever you add or remove a package

Use the following command to install all dependencies from `requirements.txt` file

```bash
pip install -r requirements.txt
```
