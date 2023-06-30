#!/usr/bin/python3
"""
print_square function
"""


def print_square(size):
    """
    print_square: prints a square with the character #.

    :param size: size of the square.
    :type size: int.
    :return: None.
    :raises: TypeError: if size is not an integer.
    :raises: ValueError: if size is less than 0.
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size > 0:
        print(("#" * size + "\n") * size, end="")
