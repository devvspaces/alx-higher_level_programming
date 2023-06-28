#!/usr/bin/python3

class Square:
    """A Square class."""

    def __init__(self, size=0):
        """
        Initialize a new Square.

        :param size: The size of the new square.
        :type size: int
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Get the current area of the square."""
        return self.__size * self.__size
