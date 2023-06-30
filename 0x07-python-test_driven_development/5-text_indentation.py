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

    text = text.replace("?", "?\n\n")
    text = text.replace(".", ".\n\n")
    text = text.replace(":", ":\n\n")

    for _ in text:
        text = text.replace(" \n", "\n")
        text = text.replace("\n ", "\n")

    text = text.strip(" ")

    print(text, end="")
