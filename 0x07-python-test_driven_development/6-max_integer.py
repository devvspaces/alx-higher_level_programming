#!/usr/bin/python3
"""
This module contains a function that finds the biggest integer of a list
"""


def max_integer(list=[]):
    """
    Finds the max integer in a list

    :param list: list of integers
    :type list: list
    :return: max integer in list
    """

    if len(list) == 0:
        return

    result = list[0]
    index = 1

    while index < len(list):
        if list[index] > result:
            result = list[index]
        index += 1

    return result
