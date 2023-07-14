#!/usr/bin/python3

"""Unittest for base.py
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for Base class
    """

    def test_docs(self):
        """Test docstrings
        """
        self.assertIsNotNone(Base.__doc__)
        self.assertIsNotNone(Base.__init__.__doc__)
        self.assertIsNotNone(Base.to_json_string.__doc__)
        self.assertIsNotNone(Base.from_json_string.__doc__)
        self.assertIsNotNone(Base.save_to_file.__doc__)
        self.assertIsNotNone(Base.create.__doc__)

    def test_init(self):
        """Test init
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b1 = Base()
        self.assertEqual(b1.id, 2)

        b1 = Base(12)
        self.assertEqual(b1.id, 12)

        b1 = Base()
        self.assertEqual(b1.id, 3)

    def test_to_json_string(self):
        """Test to_json_string
        """
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'x': 2}]), '[{"x": 2}]')
        self.assertEqual(type(Base.to_json_string([{'x': 2}])), str)

    def test_from_json_string(self):
        """Test from_json_string
        """
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"x": 2}]'), [{'x': 2}])
        self.assertEqual(type(Base.from_json_string('[{"x": 2}]')), list)

    def tearDown(self) -> None:
        """Tear down
        """
        Base._Base__nb_objects = 0
