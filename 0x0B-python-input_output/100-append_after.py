#!/usr/bin/python3
"""
IO module
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file,
    after each line containing a specific string.
    """
    result = ""

    with open(filename, 'r') as file:
        for readline in file:
            result += readline
            if search_string in readline:
                result += new_string

    with open(filename, "w") as file:
        file.write(result)
