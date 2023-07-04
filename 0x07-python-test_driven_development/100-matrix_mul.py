#!/usr/bin/python3
"""
This module contains a function that multiplies 2 matrices
Making sure that all elements are integers or floats
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices.

    Validations:
        - m_a and m_b must be lists of lists of integers or floats
        - m_a and m_b can't be empty
        - m_a and m_b must be of the same size
        - m_a and m_b must contain only integers or floats

    :param m_a: first matrix
    :type m_a: list of lists of integers or floats
    :param m_b: second matrix
    :type m_b: list of lists of integers or floats
    :return: new matrix
    """

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for a in m_a:
        if type(a) is not list:
            raise TypeError("m_a must be a list of lists")
    for a in m_b:
        if type(a) is not list:
            raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    for a in m_a:
        if len(a) == 0:
            raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    for a in m_b:
        if len(a) == 0:
            raise ValueError("m_b can't be empty")

    for a in m_a:
        for b in a:
            if type(b) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for a in m_b:
        for b in a:
            if type(b) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")

    m_a_row = len(m_a[0])
    m_b_row = len(m_b[0])
    for a in m_a[1:]:
        if (len(a) != m_a_row):
            raise TypeError("each row of m_a must be of the same size")
    for a in m_b[1:]:
        if (len(a) != m_b_row):
            raise TypeError("each row of m_b must be of the same size")

    if len(m_b) != m_a_row:
        raise ValueError("m_a and m_b can't be multiplied")

    inverted_b = []
    for row in range(len(m_b[0])):
        new_row = []
        for column in range(len(m_b)):
            new_row.append(m_b[column][row])
        inverted_b.append(new_row)

    new_matrix = []
    for row in m_a:
        new_row = []
        for col in inverted_b:
            prod = 0
            for i in range(len(inverted_b[0])):
                prod += row[i] * col[i]
            new_row.append(prod)
        new_matrix.append(new_row)

    return new_matrix
