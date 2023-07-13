#!/usr/bin/python3

"""
Add attribute
"""


def validate(obj):
    """
    Check if obj is immutable
    """
    if type(obj) in [tuple, str, int, frozenset]:
        raise TypeError("can't add new attribute")
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")


def add_attribute(obj, name, value):
    """
    Add new attribute to obj
    """
    slots = getattr(obj, "__slots__", None)
    if slots is None:
        validate(obj)
        if getattr(obj, name, None) is None:
            raise TypeError("can't add new attribute")
        setattr(obj, name, value)

    if name not in slots:
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
