#!/usr/bin/python3

def max_integer(my_list=[]):
    maximum = None
    for n in my_list:
        if maximum is None:
            maximum = n
        else:
            maximum = n if n > maximum else maximum
    return maximum
