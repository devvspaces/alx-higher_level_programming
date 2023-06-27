#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Print all the items in my_list safely
    """
    i = -1
    for i in range(x):
        try:
            print(my_list[i], end="")
        except IndexError:
            i -= 1
            break
    print()
    i += 1
    return (i)


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list(my_list, 0)
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))
