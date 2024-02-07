#!/usr/bin/python3
"""Define script that adds all arguments to a Python list"""
import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    try:
        js_list = load_from_json_file('add_item.json')
    except FileNotFoundError:
        js_list = []

    for i in range(1, len(sys.argv)):
        js_list.append(sys.argv[i])
    save_to_json_file(js_list, "add_item.json")
