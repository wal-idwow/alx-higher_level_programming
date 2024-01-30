#!/usr/bin/python3
"""
    Unittest for max_integer module
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test for max_integer function."""

    def test_regular(self):
        """Test regular list of ints/ return: the max result"""
        l = [1, 2, 3, 4, 5]
        result = max_integer(l)
        self.assertEqual(result, 5)

    def test_none(self):
        """Test None as parameter/ raise: a TypeError"""
        self.assertRaises(TypeError, max_integer, None)

    def test_empty(self):
        """Test empty list/return: None"""
        l = []
        result = max_integer(l)
        self.assertEqual(result, None)

    def test_identical(self):
        """Test list of identical values/ return: the value"""
        l = [8, 8, 8, 8, 8]
        result = max_integer(l)
        self.assertEqual(result, 8)

    def test_negative(self):
        """Test list of negative values/ return: the max"""
        l = [-2, -6, -1]
        result = max_integer(l)
        self.assertEqual(result, -1)

    def test_float(self):
        """Test list of mixed ints and floats/ return: the max"""
        l = [3, 4.5, 2]
        result = max_integer(l)
        self.assertEqual(result, 4.5)

    def test_not_int(self):
        """Test list of non-ints and ints:
        raise: a TypeError exception"""
        l = ["a", "b", 9]
        self.assertRaises(TypeError, max_integer, l)

    def test_not_list(self):
        """Test parameter that's not a list/raise: a TypeError"""
        self.assertRaises(TypeError, max_integer, 7)

    def test_unique(self):
        """Test list of one int/ return: the value of this int"""
        l = [45]
        result = max_integer(l)
        self.assertEqual(result, 45)

    def test_strings(self):
        """Test list of strings/ return: te first string"""
        l = ["hi", "hello"]
        result = max_integer(l)
        self.assertEqual(result, "hi")

if __name__ == '__main__':
    unittest.main()
