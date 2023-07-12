#!/usr/bin/python3
"""
IO Module
"""


def print_stats(size, status_codes):
    """
    Printing accumulated metrics.
    """
    print("File size: {}".format(size))
    for keyed in sorted(status_codes):
        print("{}: {}".format(keyed, status_codes[keyed]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    counting_lines = 0

    try:
        for readline in sys.stdin:
            if counting_lines == 10:
                print_stats(size, status_codes)
                counting_lines = 1
            else:
                counting_lines += 1

            readline = readline.split()

            try:
                size += int(readline[-1])
            except (IndexError, ValueError):
                pass

            try:
                if readline[-2] in valid_codes:
                    if status_codes.get(readline[-2], -1) == -1:
                        status_codes[readline[-2]] = 1
                    else:
                        status_codes[readline[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except keyedboardInterrupt:
        print_stats(size, status_codes)
        raise
