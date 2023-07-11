#!/usr/bin/python3

"""
MyInt module
"""


class MyInt(int):
    """
    MyInt Class
    """

    def __eq__(self, __value: object) -> bool:
        """
        Inverted ==
        """
        return not super().__eq__(__value)

    def __ne__(self, __value: object) -> bool:
        """
        Inverted !=
        """
        return not super().__ne__(__value)
