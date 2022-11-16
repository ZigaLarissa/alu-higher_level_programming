#!/usr/bin/python3
"""class Rectangle that inherites from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherit the class BaseGeometry"""

    def __init__(self, width, height):
        """validate width and height"""

        self.integer_validator("height", height)
        self.__height = height
        self.integer_validator("width", width)
        self.__width = width

    def area(self):
        """The area of the rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""

        return str("[Rectangle] {}/{}".format(self.__width, self.__height))
