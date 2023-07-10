#!/usr/bin/python3

"""
Lookup module
"""


def lookup(obj):
    """
    lookup - returns the list of available attributes and methods of an object

    :param obj: object to be checked
    :type obj: object
    :return: list of available attributes and methods
    :rtype: list
    """
    return dir(obj)
