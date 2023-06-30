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
        self.size = size

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """test"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """test"""
        return self.__size * self.__size

    def __eq__(self, other):
        """test"""
        return self.area() == other.area()

    def __ne__(self, other):
        """test"""
        return self.area() != other.area()

    def __lt__(self, other):
        """test"""
        return self.area() < other.area()

    def __le__(self, other):
        """test"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """test"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Compare the area of the square to another."""
        return self.area() >= other.area()
