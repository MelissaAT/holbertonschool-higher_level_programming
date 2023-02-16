#!/usr/bin/python3
"""comment module"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """ Initialization"""
    def setUp(self):
        """setup method"""
        Base._Base__nb_objects

    def test_id(self):
        """test id"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 1)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        r3 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r3.id, 5)
        self.assertEqual(r3.width, 1)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 3)
        self.assertEqual(r3.y, 4)
