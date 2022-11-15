#!/usr/bin/python3
"""inhertes the built-in list class"""


class MyList(list):
    """prints the sorted version of the list"""

    def print_sorted(self):
        print(sorted(self))
