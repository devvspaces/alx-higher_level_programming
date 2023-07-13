#!/usr/bin/python3

"""
Square module
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square Class
    """

    def __init__(self, size):
        """
        Initialize a square
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """Human readable string
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
