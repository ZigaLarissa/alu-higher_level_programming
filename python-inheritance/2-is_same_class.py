#!/usr/bin/python3
"""returns true if object is an instance of a specified class"""


def is_same_class(obj, a_class):
    """returns true if object is an instance of a specified class"""

    if type(obj) == a_class:
        return True
    return False
