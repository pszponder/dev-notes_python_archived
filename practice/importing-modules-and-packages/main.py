"""
Project entry point
"""

# Import Adjacent module
import helper

# Import modules from package a (one at a time)
import package_a.mod_a1 as ma1
import package_a.mod_a2 as ma2
import package_a.mod_a3 as ma3

# Import modules from package b (using from..import syntax)
from package_b import mod_b1, mod_b2, mod_b3

# Import modules from package c (nested package inside package b)
from package_b.package_c import mod_c1
from package_b.package_c import (
    mod_c2 as mc2,
    mod_c3 as mc3,
)  # Create aliases for imported modules

if __name__ == "__main__":
    # Run code from adjacent module
    helper.say_hello()

    # Run code from package a
    ma1.a1_func()
    ma2.a2_func()
    ma3.a3_func()

    ma1.a1_func_helper()
    ma1.a1_func_mb1()
    ma1.a1_func_mc1()

    # Run code from package b
    mod_b1.b1_func()
    mod_b2.b2_func()
    mod_b3.b3_func()

    # Run code from package c (nested package inside package b)
    mod_c1.c1_func()
    mc2.c2_func()
    mc3.c3_func()
