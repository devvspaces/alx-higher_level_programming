#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """
    Deletes keys with a specific value in a dictionary

    :param a_dictionary: dictionary
    :type a_dictionary: dict
    :param value: value to search
    :type value: any
    :return: mutated dictionary
    :rtype: dict
    """
    keys = [k for k in a_dictionary if a_dictionary[k] == value]
    for key in keys:
        a_dictionary.pop(key)
    return a_dictionary


if __name__ == "__main__":
    print_sorted_dictionary = \
        __import__('6-print_sorted_dictionary').print_sorted_dictionary

    a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}
    new_dict = complex_delete(a_dictionary, 'C')
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)

    print("--")
    print("--")
    new_dict = complex_delete(a_dictionary, 'c_is_fun')
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)
