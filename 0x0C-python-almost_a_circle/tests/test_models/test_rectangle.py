#!/usr/bin/python3

"""Unittest for base.py
"""

import json
import unittest
from os import remove

from models.base import Base
from models.rectangle import Rectangle
from tests.utils import extract_stdout


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class
    """

    def setUp(self) -> None:
        """Set up
        """
        Base._Base__nb_objects = 0

    def test_docs(self):
        """Test docstrings
        """
        self.assertIsNotNone(Rectangle.__doc__)
        self.assertIsNotNone(Rectangle.__init__.__doc__)
        self.assertIsNotNone(Rectangle.__str__.__doc__)
        self.assertIsNotNone(Rectangle.update.__doc__)
        self.assertIsNotNone(Rectangle.to_dictionary.__doc__)
        self.assertIsNotNone(Rectangle.area.__doc__)
        self.assertIsNotNone(Rectangle.display.__doc__)
        self.assertIsNotNone(Rectangle.width.__doc__)
        self.assertIsNotNone(Rectangle.height.__doc__)
        self.assertIsNotNone(Rectangle.x.__doc__)
        self.assertIsNotNone(Rectangle.y.__doc__)

    def test_first(self):
        """Test first
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_validations(self):
        """Test setter validations
        """
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle("10", 2)

        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(10, "2")

        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(10, 2, "0", 0, 12)

        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle(10, 2, 0, "0", 12)

        r1 = Rectangle(10, 2)

        with self.assertRaises(ValueError, msg="width must be > 0"):
            r1.width = -10

        with self.assertRaises(ValueError, msg="height must be > 0"):
            r1.height = -2

        with self.assertRaises(ValueError, msg="x must be >= 0"):
            r1.x = -10

        with self.assertRaises(ValueError, msg="y must be >= 0"):
            r1.y = -2

    def test_area(self):
        """Test area
        """
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        """Test display
        """
        r1 = Rectangle(4, 6)
        computed = extract_stdout(r1.display)
        expected = "####\n####\n####\n####\n####\n####\n"
        self.assertEqual(computed, expected)

        r2 = Rectangle(2, 2)
        computed = extract_stdout(r2.display)
        expected = "##\n##\n"
        self.assertEqual(computed, expected)

        r3 = Rectangle(2, 3, 2, 2)
        computed = extract_stdout(r3.display)
        expected = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(computed, expected)

        r4 = Rectangle(3, 2, 1, 0)
        computed = extract_stdout(r4.display)
        expected = " ###\n ###\n"
        self.assertEqual(computed, expected)

    def test_str(self):
        """Test __str__
        """
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")

    def test_update(self):
        """Test update
        """
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")

        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")

        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")

        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")

        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")

        r1.update(y=1, width=2, x=3, id=89, height=4)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/4")

        r1.update(1, 1, 1, 1, 1, 1, 1, 1)
        self.assertEqual(str(r1), "[Rectangle] (1) 1/1 - 1/1")\

        r1.update(90, 12, 13, width=14, height=15, x=16, y=17)
        self.assertEqual(str(r1), "[Rectangle] (90) 1/1 - 12/13")

    def test_to_dictionary(self):
        """Test to_dictionary
        """
        r1 = Rectangle(10, 2, 1, 9)
        self.assertEqual(str(r1), "[Rectangle] (1) 1/9 - 10/2")
        r1_dictionary = r1.to_dictionary()
        self.assertDictEqual(
            r1_dictionary,
            {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        )
        self.assertEqual(type(r1_dictionary), dict)

        r2 = Rectangle(1, 1)
        self.assertEqual(str(r2), "[Rectangle] (2) 0/0 - 1/1")
        r2.update(**r1_dictionary)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/9 - 10/2")
        self.assertNotEqual(r1, r2)

    def test_save_to_file(self):
        """Test save_to_file
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as f:
            computed = json.loads(f.read())
            expected = '[{"y": 8, "x": 2, "id": 1, "width": \
                10, "height": 7}, ' \
                '{"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]'
            self.assertListEqual(computed, json.loads(expected))

    def test_save_to_file_empty(self):
        """Test save_to_file empty
        """
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_None(self):
        """Test save_to_file None
        """
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_create(self):
        """Test create
        """
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertNotEqual(r1, r2)
        self.assertIsNot(r1, r2)

    def test_load_from_file(self):
        """Test Load from file
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        computed = Rectangle.load_from_file()
        self.assertEqual(str(computed[0]), str(r1))
        self.assertEqual(str(computed[1]), str(r2))
        self.assertNotEqual(computed[0], r1)
        self.assertNotEqual(computed[1], r2)
        self.assertIsNot(computed[0], r1)
        self.assertIsNot(computed[1], r2)

    def test_load_from_file_csv(self):
        """Test Load from file csv
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([r1, r2])
        computed = Rectangle.load_from_file_csv()
        self.assertEqual(str(computed[0]), str(r1))
        self.assertEqual(str(computed[1]), str(r2))
        self.assertNotEqual(computed[0], r1)
        self.assertNotEqual(computed[1], r2)
        self.assertIsNot(computed[0], r1)
        self.assertIsNot(computed[1], r2)

    def tearDown(self) -> None:
        """Tear down
        """
        try:
            remove("Rectangle.json")
            remove("Rectangle.csv")
        except OSError:
            pass
