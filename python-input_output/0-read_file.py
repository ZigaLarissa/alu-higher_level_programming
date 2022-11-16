#!/usr/bin/python3
"""Create a file that reads contents of another."""


def read_file(filename=""):
    """Open and read the said file"""

    with open(filename, encoding='UTF8') as f:
        print(f.read(), end="")
