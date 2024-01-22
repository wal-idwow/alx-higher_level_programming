#!/usr/bin/python3
def magic_calculation(a, b):
    nb = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            nb += (a ** b) / i
        except Exception:
            nb = b + a
            break
    return nb
