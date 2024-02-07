#!/usr/bin/python3
"""define function that writes an Object to a text file"""
import json



def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file, using a json

    Args:
        my_obj (object): _description_
        filename (str): _description_
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)

