#!/usr/bin/python3
"""Unit testing for the base class"""


import os
from unittest import TestCase
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(TestCase):
    """The Test class for the Base class in models."""

    def test_ba(self):
        """Test the starting point of creation of Base"""

        base = Base()
        base_1 = Base()
        base_89 = Base(89)
        self.assertEqual(base.id, 1)
        self.assertEqual(base_1.id, 2)
        self.assertEqual(base_89.id, 89)

    def test_to_json_string(self):
        """Test the converting of lists to dicts"""

        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([{'id': 10}]), '[{"id": 10}]')
        self.assertEqual(type(Base.to_json_string([{'id': 10}])), str)
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_save_to_file(self):
        """Test that the file saves list objects to  file"""

        Base._Base__nb_objects = 0
        Square.save_to_file(None)

        self.assertTrue(os.path.isfile("Square.json"))

        with open("Square.json") as my_file:
            self.assertEqual(my_file.read(), '[]')

        Square.save_to_file([])

        with open("Square.json") as my_file:
            self.assertEqual(my_file.read(), '[]')
            self.assertEqual(type(my_file.read()), str)

        Square.save_to_file([Square(2)])
        with open("Square.json") as my_file:
            self.assertEqual(my_file.read(),
                             '[{"id": 1, "size": 2, "x": 0, "y": 0}]')
        Base._Base__nb_objects = 0

        Rectangle.save_to_file(None)
        self.assertTrue(os.path.isfile("Rectangle.json"))

        with open("Rectangle.json") as my_file:
            self.assertEqual(my_file.read(), '[]')

        Rectangle.save_to_file([])
        with open("Rectangle.json") as my_file:
            self.assertEqual(my_file.read(), '[]')
            self.assertEqual(type(my_file.read()), str)

        Rectangle.save_to_file([Rectangle(2, 4)])
        with open("Rectangle.json") as my_file:
            self.assertEqual(my_file.read(),
                             '[{"id": 1, "width": 2, '
                             '"height": 4, "x": 0, "y": 0}]')

    def test_from_json_string(self):
        """Test the converting of a file from JSON string representation."""

        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string('[{"id": 89}]'), [{'id': 89}])
        self.assertEqual(type(Base.from_json_string('[{"id": 89}]')), list)
        self.assertEqual(Base.from_json_string("[]"), [])
