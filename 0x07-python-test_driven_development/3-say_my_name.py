#!/usr/bin/python3
"""
Speaking
"""


def say_my_name(first_name, last_name=""):
    """
    Says my name

    :param first_name: first name
    :type first_name: str
    :param last_name: last name, defaults to ""
    :type last_name: str, optional
    :raises TypeError: first_name must be a string
    :raises TypeError: last_name must be a string
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is", first_name, last_name)
