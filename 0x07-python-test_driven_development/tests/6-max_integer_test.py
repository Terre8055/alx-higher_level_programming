#!/usr/bin/pyrhon3
'''Unittest for max_integer([..])
'''
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        # Test finding max integer in an empty list
        self.assertEqual(max_integer([]), None)

        # Test finding max integer in a list with one element
        self.assertEqual(max_integer([4]), 4)

        # Test finding max integer in a list with multiple elements
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([5, 2, 7, 3, 8, 1, 4, 9, 6]), 9)
        self.assertEqual(max_integer([9, 8, 7, 6, 5, 4, 3, 2, 1]), 9)

    def test_docstring(self):  # tests to see if doc exists
        self.assertIsNotNone(max_integer.__doc__)


if __name__ == '__main__':
    unittest.main()

