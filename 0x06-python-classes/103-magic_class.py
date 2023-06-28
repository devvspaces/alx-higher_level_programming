#!/usr/bin/python3
import math


class MagicClass:
    """A MagicClass class for a circle."""

    def __init__(self, radius=0):
        """
        Initialize a new MagicClass.

        :param radius: The radius of the new MagicClass
        , defaults to 0
        :type radius: int, optional
        :raises TypeError: radius must be a number
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        return (2 * math.pi * self.__radius)
