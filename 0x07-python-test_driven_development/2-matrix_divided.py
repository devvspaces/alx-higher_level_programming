#!/usr/bin/python3

"""
Matrix divided
"""


def matrix_divided(matrix, div):
    """
    Divide matrix by div
    """
    new_matrix = []

    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    size = len(matrix[0])

    for row in matrix:
        for col in row:
            if type(col) not in [int, float]:
                raise TypeError(
                    "matrix must be a matrix (list of lists) \
of integers/floats")

        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")

        if div == 0:
            raise ZeroDivisionError("division by zero")

        new_matrix.append([round(i/div, 2) for i in row])

    return new_matrix
