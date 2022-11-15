#!/usr/bin/python3
"""same class or inherit from same class"""


def is_kind_of_class(obj, a_class):
    """is object an instance of the class or it's subclass"""

    if isinstance(obj, a_class):
        return True
    return False
