#!/usr/bin/python3
def uppercase(s):
    for char in s:
        #check of the char is a lowercase letter
        if 'a' <= char <= 'z':
            #convertision of lower to upper
            uppercase_char = "{0}".format(chr(ord(char) - ord('a') + ord('A')))
            print(uppercase_char, end='')
        else:
            print(char, end='')
    #print newline
    print()
