#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_x = 0
    
    if not isinstance(roman_string, str) or roman_string is None:
        return result
    
    for i in reversed(roman_string):
            x = rom_num.get(i, 0)
            if x < prev_x:
                result -= x
            else:
                result += x
            prev_x = x
    
    return result if 1 <= result <= 3999 else 0
