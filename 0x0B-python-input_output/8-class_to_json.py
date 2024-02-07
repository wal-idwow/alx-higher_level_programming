#!/usr/bin/python3
"""Define function that returns the dictionary description"""
import json


def class_to_json(obj):
    """function returns dictionary desc"""
    lt = {}
    if hasattr(obj, "__dict__"):
        lt = obj.__dict__.copy()
    return lt
