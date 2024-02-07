#!/usr/bin/python3
"""Define function that returns the dictionary description with simple data structure"""
import json


def class_to_json(obj):
    """function returns dictionary desc with simple data structure"""
    dictionnaire = {}
    if hasattr(obj, "__dic__"):
        dictionnaire = obj.__dic__.copy()
    return dictionnaire
