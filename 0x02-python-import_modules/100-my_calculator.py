#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv
    from calculator_1 import add, sub, mul, div

    argc = len(argv) - 1

    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if argv[2] not in "+*-/":
        print(argv[2])
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])

    ops = {
        "+": lambda a, b: print("{} + {} = {}".format(a, b, add(a, b))),
        "-": lambda a, b: print("{} - {} = {}".format(a, b, sub(a, b))),
        "*": lambda a, b: print("{} * {} = {}".format(a, b, mul(a, b))),
        "/": lambda a, b: print("{} / {} = {}".format(a, b, div(a, b))),
    }

    ops.get(op)(a, b)