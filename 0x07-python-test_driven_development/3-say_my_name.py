#!/usr/bin/python3
"""
This is the "3-say_my_name" module.
The 3-say_my_name module supplies one function, say_my_name().
For example,
say_my_name("Abel", "Solomon") returns My name is Abel Solomon
"""


def say_my_name(first_name, last_name=""):
    """Prints the full name of the user."""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is", first_name, last_name)
