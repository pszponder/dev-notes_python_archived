# Managing Python Versions

## Pyenv

```bash
# Find latest stable version of python
pyenv install --list | awk '{print $1}' | grep -v - | grep -v 'a\|b\|c\|m' | tail -1
```

```bash
# Install python version
pyenv install <python-version>
```

```bash
# Use a specific version of python globally
pyenv global <python-version>
```

## Resources / References

- [pyenv](https://github.com/pyenv/pyenv)
- [RealPython - Managing Multiple Python Versions w/ pyenv](https://realpython.com/intro-to-pyenv/)
