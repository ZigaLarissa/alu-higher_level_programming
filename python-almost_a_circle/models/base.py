#!/usr/bin/python3
"""Create a new class."""

import json
import csv
import turtle


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

    @classmethod
    def create(cls, **dictionary):
        """Returns instance with all attr already set.by creating a dummy."""

        if cls.__name__ == "Rectangle":
            dummy = cls(3, 2)
        if cls.__name__ == "Square":
            dummy = cls(3)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of loaded instances."""

        filename = cls.__name__ + ".json"

        try:
            with open(filename, "r") as my_file:
                handle = my_file.read()
        except FileNotFoundError:
            return []
        handle_load = cls.from_json_string(handle)
        my_list = []
        for object_dict in handle_load:
            my_list.append(cls.create(**object_dict))
        return my_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serialize in a CSV file """

        filename = cls.__name__ + ".csv"

        if filename == "Rectangle.csv":
            fields = ["id", "width", "height", "x", "y"]
        else:
            fields = ["id", "size", "x", "y"]

        with open(filename, mode="w", newline="") as my_File:
            if list_objs is None:
                writer = csv.writer(my_File)
                writer.writerow([[]])
            else:
                writer = csv.DictWriter(my_File, fieldnames=fields)
                writer.writeheader()
                for x in list_objs:
                    writer.writerow(x.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ Load from a CSV file """

        try:
            filename = cls.__name__ + ".csv"

            with open(filename, mode="r", newline="") as my_File:
                reader = csv.DictReader(my_File)
                lst = []
                for x in reader:
                    for i, n in x.items():
                        x[i] = int(n)
                    lst.append(x)
                return ([cls.create(**objt) for objt in lst])
        except FileNotFoundError:
            return ([])

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Draw the rectangles and squares """

        shapes = []
        if list_rectangles:
            shapes.extend(list_rectangles)
        if list_squares:
            shapes.extend(list_squares)
        pen = turtle.Turtle()
        pen.pen(pencolor='black', pendown=False, pensize=2, shown=False)
        for shape in shapes:
            pen.penup()
            pen.setpos(shape.x, shape.y)
            pen.pendown()
            pen.forward(shape.width)
            pen.right(90)
            pen.forward(shape.height)
            pen.right(90)
            pen.forward(shape.width)
            pen.right(90)
            pen.forward(shape.height)
            pen.right(90)
