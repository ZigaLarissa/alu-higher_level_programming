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

    @property
    def height(self):
        """Get the height attr."""

        return self.__height

    @property
    def x(self):
        """Get the x attr."""

        return self.__x

    @property
    def y(self):
        """Get the y attr."""

        return self.__y
