#!/usr/bin/python3

"""Defining a square class"""


class Square:
    """A Square class."""

    def __init__(self, size=0):
        """
        Initialize a new Square.

        :param size: The size of the new square.
        :type size: int
        """
        self.__size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        :param value: The new size of the square.
        :type value: int
        :raises TypeError: _size must be an integer_
        :raises ValueError: _size must be >= 0_
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Get the current area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square to stdout
        using the # character.
        """
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
