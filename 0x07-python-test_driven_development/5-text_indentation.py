#!/usr/bin/python3
"""
This module contains a function that prints a text with 2 new lines after each
of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    :param text: text to be printed
    :type text: str
    :raises TypeError: text must be a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    flag_num = 0
    for char in text:
        if flag_num == 0:
            if char == ' ':
                continue
            else:
                flag_num = 1

        if flag_num == 1:
            if char == '?' or char == '.' or char == ':':
                print(char)
                print()
                flag_num = 0
            else:
                print(char, end="")
