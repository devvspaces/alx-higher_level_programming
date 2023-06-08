#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv

    argc = len(argv) - 1
    plural = '' if argc == 1 else 's'
    punc = ':' if argc > 0 else '.'

    print("{} argument{}{}".format(argc, plural, punc))

    idx = 1
    for arg in argv[1:]:
        print(f"{idx}: {arg}")
        idx += 1
