#!/usr/bin/python3
"""Unittest for Base, Rectangle, and Square classes"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for Base class"""

    def test_id(self):
        """Test id attribute"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
        b3 = Base()
        self.assertEqual(b3.id, 2)
        b4 = Base(-3)
        self.assertEqual(b4.id, -3)


if __name__ == '__main__':
    unittest.main()