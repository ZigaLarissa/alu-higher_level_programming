#!/usr/bin/python3
"""Add all arguments to a Python list, and then save them to a file"""


import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file') \
        .load_from_json_file

    try:
        loadfile = load_from_json_file("add_item.json")
    except FileNotFoundError:
        loadfile = []

    arg = len(sys.argv)
    for i in range(1, arg):
        loadfile.append(sys.argv[i])
    save_to_json_file(loadfile, "add_item.json")
