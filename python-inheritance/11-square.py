#!/usr/bin/python3
"""Inherit from RQectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Initialize the subclass"""
    def __init__(self, size):
        """call the integer validator method"""
        self.integer_validator("size", size)
        """call the parent class methods and attributes"""
        super().__init__(size, size)
        self.__size = size

    """Create the user string represantation"""
    def __str__(self):
        return str("[Square] {}/{}".format(self.__size, self.__size))
