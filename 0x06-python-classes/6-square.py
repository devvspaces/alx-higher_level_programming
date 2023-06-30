#!/usr/bin/python3

"""Defining a square class"""


class Square:
    """A Square class."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square.

        :param size: The size of the new square.
        :type size: int
        :param position: The position of the new square.
        :type position: tuple
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the current size of the square."""
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

    @property
    def position(self):
        """Get the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        :param value: The new position of the square.
        :type value: tuple
        :raises TypeError: _position must be a tuple of 2 positive integers_
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Get the current area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Display the square with the # character."""
        if self.__size == 0:
            print()
            return

        for _ in range(0, self.__position[1]):
            print()

        for _ in range(0, self.__size):
            for _ in range(0, self.__position[0]):
                print(" ", end="")
            for _ in range(0, self.__size):
                print("#", end="")
            print()
