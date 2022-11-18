#!/usr/bin/python3
# function that inserts a line of text to a file,
# after each line containing a specific string (see example)2
"""
    define a 'append_after'
"""


def append_after(filename="", search_string="", new_string=""):
    """
        insert line of text to file after each line containing a string
    """

    with open(filename, 'r+', encoding='utf-8') as f:
        lines = []
        for line in f:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)
        f.seek(0)
        for line in lines:
            f.write(line)
