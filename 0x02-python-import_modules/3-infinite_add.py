#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv
    from functools import reduce

    sum = reduce(lambda a, b: a + int(b), argv[1:], 0)
    print(sum)
