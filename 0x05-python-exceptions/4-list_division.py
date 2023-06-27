#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        calc = 0
        try:
            a = my_list_1[i]
            b = my_list_2[i]

            if type(a) not in [int, float]:
                raise TypeError
            if type(b) not in [int, float]:
                raise TypeError

            if (b == 0):
                print("division by 0")

            calc = a / b

        except IndexError:
            print("out of range")

        except TypeError:
            print("wrong type")

        finally:
            result.append(calc)
            continue

    return result


if __name__ == "__main__":
    my_l_1 = [10, 8, 4]
    my_l_2 = [2, 4, 4]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)

    print("--")

    my_l_1 = [10, 8, 4, 4]
    my_l_2 = [2, 0, "H", 2, 7]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)
