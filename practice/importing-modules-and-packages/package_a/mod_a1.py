"""
package_a/mod_a1.py

In order to run mod_a1.py directly:
1. Make sure you are in the package root directory
2. Run the script as a module using the `-m` flag => `python -m package_a.mod_a1`
"""

# Absolute Imports are always relative to project root directory

# Importing modules from a root directory
import helper

# Import modules from the same directory (package)
import package_a.mod_a2 as ma2
import package_a.mod_a3 as ma3

# Import modules from an adjacent package (package_b)
import package_b.mod_b1 as mb1  # using standard import syntax
from package_b import mod_b2 as mb2, mod_b3 as mb3  # Using from..import syntax

# Import modules from a sub-directory / sub-package (package_c)
import package_b.package_c.mod_c1 as mc1  # using standard import syntax
from package_b.package_c import (
    mod_c2 as mc2,
    mod_c3 as mc3,
)  # using from..import syntax


def a1_func():
    """Logs console message"""
    print("printing from Module A1")


def a1_func_helper():
    """Invokes function imported from a module in the root-directory"""
    print("printing next line from Module A1...")
    helper.say_hello()


def a1_func_mb1():
    """Invokes function imported from an adjacent package (package_b)"""
    print("printing next line from Module A1...")
    mb1.b1_func()


def a1_func_mc1():
    """invokes function imported from a child package (package_c)"""
    print("printing next line from Module A1...")
    mc1.c1_func()


if __name__ == "__main__":
    # Invoke code from helper module (in root directory)
    helper.say_hello()

    # Invoke code from the same package (package_a)
    ma2.a2_func()
    ma3.a3_func()

    # Invoke code from adjacent package (package_b)
    mb1.b1_func()
    mb2.b2_func()
    mb3.b3_func()

    # Invoke code from a sub-directory / sub-package (package_c)
    mc1.c1_func()
    mc2.c2_func()
    mc3.c3_func()
