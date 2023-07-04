#!/usr/bin/

"""Unittest for max_integer([..])
"""

import unittest

module = __import__('6-max_integer')
max_integer = module.max_integer


class TestMaxInt(unittest.TestCase):
    """
    Class for testing max_integer function

    :param unittest: unittest
    :type unittest: unittest.TestCase
    """

    def test_working(self):
        """Test working case
        """
        data = [1, 2, 4, 5]
        self.assertEqual(max_integer(data), 5)

    def test_none(self):
        """
        Test None case
        """
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_empty(self):
        """
        Test empty list case
        """
        self.assertIsNone(max_integer([]))

    def test_negative(self):
        """
        Test negative elements case
        """
        data = [-1, -2, -4, -5]
        self.assertEqual(max_integer(data), -1)

    def test_zero(self):
        """
        Test when zero is the max element
        """
        data = [0, -1]
        self.assertEqual(max_integer(data), 0)

    def test_single_element(self):
        """
        Test when list has only one element
        """
        data = [0]
        self.assertEqual(max_integer(data), 0)

    def test_equal(self):
        """
        Test when all elements are equal
        """
        data = [5, 5, 5, 5]
        self.assertEqual(max_integer(data), 5)

    def test_max_at_beginning(self):
        """
        Test when max element is at the beginning
        """
        data = [5, 1, 2, 3]
        self.assertEqual(max_integer(data), 5)

    def test_max_at_end(self):
        """
        Test when max element is at the end
        """
        data = [1, 2, 4, 5]
        self.assertEqual(max_integer(data), 5)

    def test_max_at_center(self):
        """
        Test when max element is at the center
        """
        data = [1, 2, 14, 5, 10]
        self.assertEqual(max_integer(data), 14)

    def test_module_doc(self):
        """
        Test when the module has a docstring
        """
        self.assertGreater(len(module.__doc__), 0)

    def test_function_doc(self):
        """
        Test when the function has a docstring
        """
        self.assertGreater(len(max_integer.__doc__), 0)

    def test_many_args(self):
        """
        Test when the function is called with many arguments
        """
        with self.assertRaises(TypeError):
            max_integer([], [], [])

    def test_with_invalid_list_types(self):
        """
        Test when the function is called with invalid list types
        """
        data = [1, 2, "4", 5]
        with self.assertRaises(TypeError):
            max_integer(data)


if __name__ == "__main__":
    unittest.main()
