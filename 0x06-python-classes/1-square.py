#!/usr/bin/python3

"""Defining a square class"""


class Square:
    """Represent a square."""

    def __init__(self, size):
        """
        Initialize a new Square.

        :param size: The size of the new square.
        :type size: int
        """
        self.__size = size
