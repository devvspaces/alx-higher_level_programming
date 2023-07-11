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
