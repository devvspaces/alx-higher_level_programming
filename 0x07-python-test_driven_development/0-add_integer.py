#!/usr/bin/python3

"""
Adding integers
"""


def add_integer(a, b=98):
    """
    Adding a and b

    :param a: a
    :type a: int or float
    :param b: b, defaults to 98
    :type b: int or float, optional
    :raises TypeError: a/b must be an integer
    :return: added value
    :rtype: int
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
