#!/usr/bin/python3
"""Write an Object to text file using JSON"""
import json


def save_to_json_file(my_obj, filename):
    """Write object in text file using JSON representation"""

    with open(filename, 'w+') as handle:
        return handle.write(json.dumps(my_obj))
