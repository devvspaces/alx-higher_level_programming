#!/usr/bin/python3
"""
IO Module
"""


def print_stats(size, status_codes):
    """
    Printing accumulated metrics.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for readline in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1

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

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
