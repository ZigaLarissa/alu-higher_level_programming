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

    def update(self, *args, **kwargs):
        """Assign attributes to arguments."""
        if len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass

        elif len(kwargs) != 0:
            self.id = kwargs["id"] if "id" in kwargs else self.id
            self.size = kwargs["size"] if "size" in kwargs else self.size
            self.x = kwargs["x"] if "x" in kwargs else self.x
            self.y = kwargs["y"] if "y" in kwargs else self.y

    def to_dictionary(self):
        """Returns a dictionary representation of the square."""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
            }
