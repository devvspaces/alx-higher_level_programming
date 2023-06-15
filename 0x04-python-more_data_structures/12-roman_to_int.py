#!/usr/bin/python3

def roman_to_int(roman_string):
    """
    Convert roman numeral to number

    :param roman_string: roman numeral
    :type roman_string: string
    :return: number
    :rtype: int
    """
    mapping = {
        "M": 1000,
        "C": 100,
        "X": 10,
        "I": 1,
        "D": 500,
        "L": 50,
        "V": 5
    }

    def get_val(idx):
        return mapping[roman_string[idx]]

    idx = 0
    sum = 0
    lth = len(roman_string)
    while (idx < lth):
        if (idx + 1 < lth):
            if (get_val(idx) < get_val(idx + 1)):
                sum += (get_val(idx + 1) - get_val(idx))
                idx += 1
            else:
                sum += get_val(idx)
        else:
            sum += mapping[roman_string[idx]]
        idx += 1

    return sum


if __name__ == "__main__":
    roman_number = "X"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "VII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "CIX"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "LXXXVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "DCCVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))
