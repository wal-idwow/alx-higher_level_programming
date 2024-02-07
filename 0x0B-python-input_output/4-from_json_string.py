#!/usr/bin/python3
"""define function that returns an object"""
import json


def from_json_string(my_str):
    """function that returns Python data rep by json"""
    return json.loads(my_str)
