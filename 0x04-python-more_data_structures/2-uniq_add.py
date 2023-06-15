#!/usr/bin/python3

def uniq_add(my_list=[]):
    seen = {}
    sum = 0
    for i in my_list:
        if (seen.get(i) is None):
            seen[i] = True
            sum += i
    return sum


if __name__ == "__main__":
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result: {:d}".format(result))
