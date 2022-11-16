#!/usr/bin/python3
"""Define a function that convert from JSON to Python."""
import json


def from_json_string(my_str):
    """from json to python."""

    return json.loads(my_str)
