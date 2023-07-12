#!/usr/bin/python3

"""
IO module
"""


def append_write(filename="", text=""):
    """Appends a string to a text file (UTF8) and
    returns the number of characters written"""
    with open(filename, mode='+a', encoding="utf-8") as f:
        return f.write(text)


if __name__ == "__main__":
    len = append_write("files/file_append.txt", "This School is so cool!\n")
    print(len)
