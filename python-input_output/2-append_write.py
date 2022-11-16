#!/usr/bin/python3
"""Define a function that appends a line on a file"""


def append_write(filename="", text=""):
    """Append new on a file"""

    with open(filename, 'a+') as handle:
        return handle.write(text)
