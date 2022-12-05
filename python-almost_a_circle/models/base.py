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

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the json representation of list_objs to a file."""

        filename = cls.__name__ + ".json"
        temp_list = []

        if list_objs:
            for i in list_objs:
                temp_list.append(cls.to_dictionary(i))

        with open(filename, "w") as my_file:
            my_file.write(cls.to_json_string(temp_list))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string represantation."""

        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
