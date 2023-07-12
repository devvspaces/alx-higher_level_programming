#!/usr/bin/python3

"""
IO module
"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and
    returns the number of characters written"""
    len = 0
    with open(filename, mode='w', encoding="utf-8") as f:
        len = f.write(text)
    return len


if __name__ == "__main__":
    len = write_file("files/my_first_file.txt", "This School is so cool!\n")
    print(len)
