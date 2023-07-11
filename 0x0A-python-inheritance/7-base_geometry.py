#!/usr/bin/python3

"""
Geometry module
"""


class BaseGeometry:
    """
    BaseGeometry Class
    """

    def area(self):
        """
        Calcualate area of object
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value

        :param name: name of the value
        :type name: str
        :param value: value of the name
        :type value: int
        :raises TypeError: <name> must be an integer
        :raises ValueError: <name> must be greater than 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
