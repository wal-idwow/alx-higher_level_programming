#!/usr/bin/python3
"""define function that creates an Object from a “JSON file” """
import json


def load_from_json_file(filename):
    """function creates an object from ajson file"""
    with open(filename, "r", encoding='utf-8') as f:
        return json.load(f)
