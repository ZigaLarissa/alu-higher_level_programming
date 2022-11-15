#!/usr/bin/python3
"""checking the subclasses only"""


def inherits_from(obj, a_class):
    """rTrue if the object is an instance of a class that is inherited"""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
