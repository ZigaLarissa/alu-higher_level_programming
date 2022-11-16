#!/usr/bin/python3
"""Define a function that converts to json from python"""
import json


def to_json_string(my_obj):
    """Translate to json."""

    return json.dumps(my_obj)
