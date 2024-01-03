#!/usr/bin/python3

def is_lower(c):
    if ord('a') <= ord(c) <= ord('z'):
        return True
    else:
        return False


def uppercase(s):
    for char in s:
        print("{:c}".format(ord(char) if not is_lower(char) else ord(char)
        - 32), end="")
    print("")
