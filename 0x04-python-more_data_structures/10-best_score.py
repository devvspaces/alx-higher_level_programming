#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Get key with the biggest integer value.

    :param a_dictionary: scores
    :type a_dictionary: dict | None
    :return: key
    :rtype: string | None
    """

    if a_dictionary is None:
        a_dictionary = {}

    best = None
    for key, value in a_dictionary.items():
        if best is None:
            best = key
        elif value > a_dictionary[best]:
            best = key
    return best


if __name__ == "__main__":
    a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
    best_key = best_score(a_dictionary)
    print("Best score: {}".format(best_key))

    best_key = best_score(None)
    print("Best score: {}".format(best_key))

    best_key = best_score({})
    print("Best score: {}".format(best_key))
