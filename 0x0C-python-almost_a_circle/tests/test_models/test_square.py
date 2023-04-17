#!/usr/bin/python3
"""Defines unittests for models/square.py.
"""
import io
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def setUp(self):
        """Reset the id counter to 0 before each test."""
        Base._Base__nb_objects = 0

    def test_create(self):
        """Test creating a new Square."""
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertEqual(s.id, 1)

        s = Square(10, 2, 3, 20)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 20)

    def test_size(self):
        """Test the size property."""
        s = Square(5)
        self.assertEqual(s.size, 5)
        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_update(self):
        """Test updating a Square."""
        s = Square(5)
        s.update(2)
        self.assertEqual(s.id, 2)
        s.update(3, 10)
        self.assertEqual(s.id, 3)
        self.assertEqual(s.size, 10)
        s.update(4, 20, 2, 3)
        self.assertEqual(s.id, 4)
        self.assertEqual(s.size, 20)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        s.update(id=5, size=15, x=5, y=6)
        self.assertEqual(s.id, 5)
        self.assertEqual(s.size, 15)
        self.assertEqual(s.x, 5)
        self.assertEqual(s.y, 6)

    def test_to_dictionary(self):
        """Test the to_dictionary method."""
        s = Square(5, 2, 3, 20)
        d = s.to_dictionary()
        self.assertIsInstance(d, dict)
        self.assertEqual(d['id'], 20)
        self.assertEqual(d['size'], 5)
        self.assertEqual(d['x'], 2)
        self.assertEqual(d['y'], 3)

if __name__ == '__main__':
    unittest.main()

