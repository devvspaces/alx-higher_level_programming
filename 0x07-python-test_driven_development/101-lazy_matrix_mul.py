#!/usr/bin/python3
"""
This module contains a function that multiplies 2 matrices
Uses the module NumPy
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply 2 matrix

    :param m_a: first matrix
    :type m_a: list of lists of integers or floats
    :param m_b: second matrix
    :type m_b: list of lists of integers or floats
    :return: new matrix
    """
    return numpy.matmul(m_a, m_b)
