#!/usr/bin/python3

"""Unittest for base.py
"""

import unittest
from os import remove

from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for Square class
    """

    def setUp(self) -> None:
        """Set up
        """
        Base._Base__nb_objects = 0

    def test_docs(self):
        """Test docstrings
        """
        self.assertIsNotNone(Square.__doc__)
        self.assertIsNotNone(Square.__init__.__doc__)
        self.assertIsNotNone(Square.__str__.__doc__)
        self.assertIsNotNone(Square.update.__doc__)
        self.assertIsNotNone(Square.to_dictionary.__doc__)
        self.assertIsNotNone(Square.size.__doc__)

    def test_init(self):
        """Test first
        """
        s1 = Square(10, 2)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 0)

    def test_init2(self):
        """Test setting size private attribute
        """
        s1 = Square(10)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 1)

    def test_set_size(self):
        """
        Test setting size private attribute
        """
        s1 = Square(10)
        s1.size = 20
        self.assertEqual(s1.size, 20)
        self.assertEqual(s1.width, 20)
        self.assertEqual(s1.height, 20)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 1)

    def test_str(self):
        """Test string representation
        """
        s1 = Square(4, 2, 1, 12)
        self.assertEqual(str(s1), "[Square] (12) 2/1 - 4")

    def test_update(self):
        """Test update method
        """
        s1 = Square(10, 10, 10)
        s1.update(89)
        self.assertEqual(str(s1), "[Square] (89) 10/10 - 10")

        s1.update(89, 2)
        self.assertEqual(str(s1), "[Square] (89) 10/10 - 2")

        s1.update(89, 2, 3)
        self.assertEqual(str(s1), "[Square] (89) 3/10 - 2")

        s1.update(89, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (89) 3/4 - 2")

        s1.update(x=12)
        self.assertEqual(str(s1), "[Square] (89) 12/4 - 2")

        s1.update(size=7, y=1)
        self.assertEqual(str(s1), "[Square] (89) 12/1 - 7")

        s1.update(size=7, id=90, y=1)
        self.assertEqual(str(s1), "[Square] (90) 12/1 - 7")

        s1.update(1, 2, 3, 4, 5, 6, 7, 8)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")

        s1.update(91, size=9)
        self.assertEqual(str(s1), "[Square] (91) 3/4 - 2")

    def test_to_dictionary(self):
        """Test to_dictionary method
        """
        s1 = Square(10, 2, 1)
        self.assertEqual(str(s1), "[Square] (1) 2/1 - 10")
        s1_dictionary = s1.to_dictionary()
        self.assertDictEqual(
            s1_dictionary, {'x': 2, 'y': 1, 'id': 1, 'size': 10})
        self.assertEqual(type(s1_dictionary), dict)

        s2 = Square(1, 1)
        self.assertEqual(str(s2), "[Square] (2) 1/0 - 1")
        s2.update(**s1_dictionary)
        self.assertEqual(str(s2), "[Square] (1) 2/1 - 10")
        self.assertNotEqual(s1, s2)

    def test_create(self):
        """
        Test create method
        """
        s1 = Square(3, 5, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))
        self.assertNotEqual(s1, s2)

    def test_load_from_file(self):
        """Test Load from file
        """
        s1 = Square(10, 7, 2, 8)
        s2 = Square(2, 4, 2, 9)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(list_squares_output[0]), str(s1))
        self.assertEqual(str(list_squares_output[1]), str(s2))
        self.assertNotEqual(list_squares_output[0], s1)
        self.assertNotEqual(list_squares_output[1], s2)
        self.assertIsNot(list_squares_output[0], s1)
        self.assertIsNot(list_squares_output[1], s2)

    def tearDown(self) -> None:
        """Tear down
        """
        try:
            remove("Square.json")
            remove("Square.csv")
        except OSError:
            pass
