#!/usr/bin/python3

"""
is_same_class module
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of
    the specified class, otherwise False.

    :param obj: obj to check
    :param a_class: class
    :return: true or false
    :rtype: bool
    """
    return getattr(obj, "__class__") is a_class
