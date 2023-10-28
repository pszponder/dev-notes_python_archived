"""
package_b/package_c/mod_c1.py

In order to run mod_c1.py directly:
1. Make sure you are in the package root directory
2. Run the script as a module using the `-m` flag => `python -m package_b.package_c.mod_c1`
"""

# Absolute Imports are always relative to project root directory

# Import modules from root directory
import helper

# Import adjacent modules
import package_b.package_c.mod_c2 as mc2
import package_b.package_c.mod_c3 as mc3

# Import modules from parent package (package_b)
from package_b import mod_b1 as mb1, mod_b2 as mb2, mod_b3 as mb3

# Import modules from package_a
from package_a import mod_a1 as ma1, mod_a2 as ma2, mod_a3 as ma3


def c1_func():
    """Logs console message"""
    print("printing from Module C1")


if __name__ == "__main__":
    # Invoke code from root directory module (helper)
    helper.say_hello()

    # Invoke code from adjacent modules
    mc2.c2_func()
    mc3.c3_func()

    # Invoke code from parent package (package_b)
    mb1.b1_func()
    mb2.b2_func()
    mb3.b3_func()

    # Invoke code from an outer package (package_a)
    ma1.a1_func()
    ma1.a1_func_helper()
    ma1.a1_func_mb1()
    ma1.a1_func_mc1()
    ma2.a2_func()
    ma3.a3_func()
