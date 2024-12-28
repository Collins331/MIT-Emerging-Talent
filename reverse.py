#!/usr/bin/env python3
# -*- coding: utf-8 -*-


""" Functions

Functions allow you to package blocks of code to reuse with different arguments.
Calling a function creates a new scope with your arguments and local variables.
Functions can return a value to the main scope for later use.

Passing a str, bool, int or float to a function does not modify the variable's value.

Python Tutor is very helpful for visualizing functions *

"""


# --- function declaration ---
def reverse(to_reverse: str) -> str:
    """Reverses a string."""

    # variables declared in the function are local variables
    #   they are only available inside the function call
    backwards = ""

    for char in to_reverse:
        backwards = char + backwards

    return backwards


# --- function calls and assertion tests ---
# try stepping over this function call
_1_arg = "Bori"
_1_return_value = reverse(_1_arg)
assert _1_return_value == "iroB", "reverse: Test 1"

# try stepping all the way through this function call
_2_arg = "<[+]>"
_2_return_value = reverse(_2_arg)
assert _2_return_value == ">]+[<", "reverse: Test 2"

# try stepping into this function call
#   then stepping out of it before the function returns
_3_arg = "racecar"
_3_return_value = reverse(_3_arg)
assert _3_return_value == "racecar", "reverse: Test 3"


print("end of script")
