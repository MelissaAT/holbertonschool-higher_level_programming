#!/usr/bin/python3
"""comment module"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Initialization"""
    def setUp(self):
        """setup method"""
        Base._Base__nb_objects

    def test_id(self):
        b_a = Base()
        b_b = Base()
        b_c = Base()
        b_d = Base()
        b_e = Base(100)
        self.assertEqual(b_a.id, 1)
        self.assertEqual(b_b.id, 2)
        self.assertEqual(b_c.id, 3)
        self.assertEqual(b_d.id, 4)
        self.assertEqual(b_e.id, 100)
   
