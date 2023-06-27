#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """
    Returns a new dictionary with all
    values multiplied by 2

    :param a_dictionary: dictionary to calculate
    :type a_dictionary: dict
    """
    new_dict = {}
    for key in a_dictionary:
        new_dict[key] = a_dictionary[key] * 2
    return new_dict


if __name__ == "__main__":
    print_sorted_dictionary = \
        __import__('6-print_sorted_dictionary').print_sorted_dictionary

    a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
    new_dict = multiply_by_2(a_dictionary)
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)