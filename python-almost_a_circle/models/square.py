#!/usr/bin/python3
"""import Rectangle from models.rectangle."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherite from class Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize attributes."""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get the size of the square."""

        return self.width

    @size.setter
    def size(self, value):
        """set the size value."""

        self.width = value
        self.height = value

    def __str__(self):
        """Return the string representation."""

        return "[Square] ({}) {}/{} - {}". \
            format(self.id, self.x, self.y, self.size)
