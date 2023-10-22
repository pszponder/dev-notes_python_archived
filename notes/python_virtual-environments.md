# Python Virtual Environments

**NOTE:** Always create a project `virtual environment`!

- Any time you’re working on a Python project that uses external dependencies that you’re installing with pip, it’s best to first create a virtual environment:

`Virtual environments` are a common and effective technique used in Python development.

`Virtual Environments` exist so that we can separate the dependencies of one project from the dependencies of another. This enables having different versions of the same dependency from one project to another.

**CAUTION:** Installing packages with `pip` without a `virtual environment` installs the package globally

Every `Virtual Environment` has:

- Python version that it runs on
- A directory of installed 3rd party libraries from `pipy`

Every `Virtual Environment` can be created with a different version of python and a different set of dependencies

## venv

The `venv` command is the built-in way for creating and managing virtual environments in Python

### venv Quickstart

```bash
# Create new python virtual environment
python -m venv .venv --upgrade-deps --clear
```

```bash
# Activate Virtual Environment
. .venv/bin/activate
```

```bash
# Deactivate Virtual Environment
deactivate
```

### Creating a New Virtual Environment w/ venv

```bash
# Create a new python virtual environment in current directory
python -m venv <virtual-env-name>
```

**NOTE:** Naming Conventions for `virtual environment` directories

- Most commonly used directory names for `virtual environments`
- `venv` (most common)
- `.venv`
- `env`

Recommended CLI command w/ options:

```bash
python -m venv .venv --upgrade-deps --clear
```

- `--upgrade-deps` installs the latest version of `pip` in your virtual env (avoids `outdated version of pip` error when trying to install packages)
- `--clear` deletes the contents of an existing virtual env before creating a new virtual environment

Using the above command creates a new virtual environment directory inside the current directory.

### Activating & Using Virtual Environment w/ venv

Once a virtual environment is created, it can be activated using the following command (NOTE: Make sure that you use the correct directory name for your `virtual environment`)

```bash
# NOTE: Before running this command, make sure you're in the parent folder that contains the virtual environment
. .venv/bin/activate
```

Alternatively, use `source` instead of `.`

```bash
source .venv/bin/activate
```

Upon successful activation of the python virtual environment, you should see the name of the virtual environment in your command prompt in parenthesis

**NOTE:** Install packages via `pip` after activating a `virtual environment`

- Once you activate a `virtual environment`, you’re all set and ready to install your external packages via `pip`
- Any packages installed using `pip install` when a `virtual environment` is active will be installed within the `virtual environment` directory instead of being installed globally

### Deactivating a venv Virtual Environment

Use the `deactivate` command to deactivate the currently active `virtual environment`

```bash
# Deactivate currently active virtual environment
deactivate
```

If the name of the `virtual environment` is removed from your command line, then deactivation of the `virtual environment` was successful

## 3rd Party Virtual Env Managers

### pipenv

[Real Python - Pipenv: A Guide to the New Python Packaging Tool](https://realpython.com/pipenv-guide/)

### pyenv

- [Real Python - Managing Multiple Python Versions with pyenv](https://realpython.com/intro-to-pyenv/)
- [K0zne builds - How to Install and Run Multiple Python Verions on macOS | Pyenv & virtualenv Setup Tutorial](https://www.youtube.com/watch?v=31WU0Dhw4sk)

### poetry

[ArjanCodes - How to Create and Use Virtual Environments in Python with Poetry](https://www.youtube.com/watch?v=0f3moPe_bhk)

### rye

[Github - rye](https://github.com/mitsuhiko/rye)

### Anaconda

- [Anaconda](https://www.anaconda.com/)
- [Conda User Guide](https://conda.io/projects/conda/en/latest/user-guide/index.html)

[Github - rye](https://github.com/mitsuhiko/rye)

## References

- [Real Python - Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/)
- [teclado - The Complete Guide to Python Virtual Environments](https://www.youtube.com/watch?v=KxvKCSwlUv8)
- [ArjanCodes - How to Create and Use Virtual Environments in Python With Poetry](https://www.youtube.com/watch?v=0f3moPe_bhk)
- [Real Python - Managing Multiple Python Versions with pyenv](https://realpython.com/intro-to-pyenv/)
- [ArjanCodes - How to Create and Use Virtual Environments in Python with Poetry](https://www.youtube.com/watch?v=0f3moPe_bhk)
- [Real Python - Pipenv: A Guide to the New Python Packaging Tool](https://realpython.com/pipenv-guide/)
- [Github - rye](https://github.com/mitsuhiko/rye)
