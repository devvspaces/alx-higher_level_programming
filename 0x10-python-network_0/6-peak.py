#!/usr/bin/python3

"""
Find a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    finds a peak in a list of unsorted integers
    """
    for idx, val in enumerate(list_of_integers):
        if idx + 1 < len(list_of_integers) - 1:
            if val > list_of_integers[idx+1]:
                return val
        else:
            return val
    return None
