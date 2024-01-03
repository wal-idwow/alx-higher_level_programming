#!/usr/bin/python3
def is_lower(c):
     if ord(c) >= ord('a') and ord(c) <= ord('z'):
          return True
     else:
          return False


def uppercase(str):
    for c in str:
         print("{:c}"
               .format(ord(c) if not is_lower(c) else ord(c) - 32),
               end="")
    print("")
    