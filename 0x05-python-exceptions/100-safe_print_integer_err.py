#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        obj = int(value)
        print("{:d}".format(obj))
        return True
    except ValueError as ve:
        print("Exception: {}".format(ve), file=sys.stderr)
        return False
    except TypeError as te:
        print("Exception: {}".format(te), file=sys.stderr)
        return False
