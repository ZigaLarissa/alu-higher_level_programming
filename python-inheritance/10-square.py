#!/usr/bin/python3
"""Inherit from the Rectangle class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """create a subclass Square from Rectangle"""

    def __init__(self, size):
        """make the size implementation"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
