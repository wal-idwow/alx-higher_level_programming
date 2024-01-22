#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except BaseException as err:
        res = None
        print("Exception: {}".format(err), file=sys.stderr)
    finally:
        return result
