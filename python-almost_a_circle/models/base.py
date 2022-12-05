#!/usr/bin/python3
"""Create a new class."""

import json


class Base:
    """A class with a private class attribute."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize id."""

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON represantation of list_ditionaries."""

        if list_dictionaries is None or list_dictionaries == 0:
            return "[]"
        return json.dumps(list_dictionaries)
