#!/usr/bin/python3
"""Module for testing the Base class"""
import os
import unittest
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestBaseMethods(unittest.TestCase):
    """Suite to test the Base class"""

    def setUp(self):
        """Method invoked for each test"""
        Base._Base__nb_objects = 0

    def test_id_default(self):
        """Test default id"""
        new = Base()
        self.assertEqual(new.id, 1)

    def test_id_assigned(self):
        """Test assigned id"""
        new = Base(1)
        self.assertEqual(new.id, 1)

    def test_id_increment(self):
        """Test nb_objects attribute"""
        new = Base()
        new2 = Base()
        new3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.id, 2)
        self.assertEqual(new3.id, 3)

    def test_id_mix(self):
        """Test nb_objects attributes and assigned id"""
        new = Base()
        new2 = Base(1024)
        new3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.id, 1024)
        self.assertEqual(new3.id, 2)

    def test_string_id(self):
        """Test string id"""
        new = Base('1')
        self.assertEqual(new.id, '1')

    def test_more_args_id(self):
        """Test passing more args to init method"""
        with self.assertRaises(TypeError):
            new = Base(1, 1)

    def test_access_private_attrs(self):
        """Test accessing private attributes"""
        new = Base()
        with self.assertRaises(AttributeError):
            new.__nb_objects

    def test_save_to_file_square(self):
        """Test save_to_file method for Square"""
        Square.save_to_file(None)
        res = "[]\n"
        with open("Square.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)

        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_rectangle(self):
        """Test save_to_file method for Rectangle"""
        Rectangle.save_to_file(None)
        res = "[]\n"
        with open("Rectangle.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")


if __name__ == "__main__":
    unittest.main()
