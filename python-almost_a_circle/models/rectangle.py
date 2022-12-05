#!/usr/bin/python3
"""import base from models."""

from models.base import Base


class Rectangle(Base):
    """A new class that inherites from base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the attributes."""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Access the width."""

        return self.__width

    @width.setter
    def width(self, value):
        """set the value of width"""

        if type(value) != int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """Get the height attr."""

        return self.__height

    @height.setter
    def height(self, value):
        """set the value of height"""

        if type(value) != int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """Get the x attr."""

        return self.__x

    @x.setter
    def x(self, value):
        """set the value of x"""

        if type(value) != int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """Get the y attr."""

        return self.__y

    @y.setter
    def y(self, value):
        """set the value of y"""

        if type(value) != int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """calc the area of a rectangle."""

        return self.__width * self.__height

    def display(self):
        """Return the rectangle made from #."""

        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end='')
            print("\n", end='')
