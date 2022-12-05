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
            self._id = Base.__nb_objects
