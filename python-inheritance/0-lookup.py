#!/usr/bin/python3
"""returns the list of available attributes and methods of an object"""


def lookup(obj):
    """returns available attibutes and methods of an object as a list"""
    return dir(obj)
