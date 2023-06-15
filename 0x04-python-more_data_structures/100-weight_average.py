#!/usr/bin/python3

def weight_average(my_list=[]):
    """
    Calculate the weighted average of all
    integers tuple (<score>, <weight>)

    :param my_list: list of tuple, defaults to []
    :type my_list: list, optional
    :return: weighted average
    :rtype: int
    """
    if not my_list:
        return 0
    numerator = sum([x[0] * x[1] for x in my_list])
    denominator = sum([x[1] for x in my_list])
    return numerator / denominator


if __name__ == "__main__":
    my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
    # = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
    result = weight_average(my_list)
    print("Average: {:0.2f}".format(result))
