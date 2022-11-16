#!/usr/bin/python3
"""define a function that tells the number of characters written"""


def write_file(filename="", text=""):
    """Access the file and append some line to it"""

    with open(filename, 'w') as handle:
        return handle.write(text)
