#!/usr/bin/python3

"""
IO module
"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")


if __name__ == "__main__":
    read_file("files/test.txt")
