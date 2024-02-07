#!/usr/bin/python3
"""Define JSON representation of an object function"""
import json


def to_json_string(my_obj):
    """return JSON representation of a string object"""
    return json.dumps(my_obj)
