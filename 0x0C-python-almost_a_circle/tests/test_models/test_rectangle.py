#!/usr/bin/python3
"""Defines unittests for models/rectangle.py.
"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class"""

    def test_init(self):
        """Test constructor"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10, 0, 0, 12)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r2.id, 12)

    def test_width(self):
        """Test width property"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        r1.width = 15
        self.assertEqual(r1.width, 15)

    def test_height(self):
        """Test height property"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.height, 2)
        r1.height = 5
        self.assertEqual(r1.height, 5)

    def test_x(self):
        """Test x property"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.x, 0)
        r1.x = 3
        self.assertEqual(r1.x, 3)

    def test_y(self):
        """Test y property"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.y, 0)
        r1.y = 5
        self.assertEqual(r1.y, 5)

    def test_area(self):
        """Test area method"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.area(), 20)

    def test_display(self):
        """Test display method"""
        r1 = Rectangle(2, 2)
        expected_output = '##\n##\n'
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_str(self):
        """Test __str__ method"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

    def test_update(self):
        """Test update method"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 

if __name__ == "__main__":
    unittest.main()
