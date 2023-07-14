#!/usr/bin/python3

"""
Square class module
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """init method """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Get the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size

        :param value: value to set
        :type value: int
        """
        self.width = value
        self.height = value
        self.__size = value

    def __str__(self):
        """Square string representation
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """
        Update the square
        """
        if args:
            keys = ["id", "size", "x", "y"]
            for key, value in zip(keys, args):
                setattr(self, key, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Dictionary representation of a Square
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }
