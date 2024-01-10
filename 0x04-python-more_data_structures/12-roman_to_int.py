#!/usr/bin/python3

def value(DECI):
    if DECI == 'I':
        return 1
    if DECI == 'V':
        return 5
    if DECI == 'X':
        return 10
    if DECI == 'L':
        return 50
    if DECI == 'C':
        return 100
    if DECI == 'D':
        return 500
    if DECI == 'M':
        return 1000
    return 0


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    result = 0
    i = 0

    while i < len(roman_string):
        vl1 = value(roman_string[i])

        if i + 1 < len(roman_string):
            vl2 = value(roman_string[i + 1])

            if vl1 >= vl2:
                result = result + vl1
                i = i + 1
            else:
                result = result + vl2 - vl1
                i = i + 2
        else:
            result = result + vl1
            i = i + 1
    return result
